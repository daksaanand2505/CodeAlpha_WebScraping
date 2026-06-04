# final_dashboard.py - WITH HTML REPORT GENERATION
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Load the data
df = pd.read_csv('restaurant_tips.csv')

# Set style
plt.style.use('default')
sns.set_style("whitegrid")

# Create figure
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Restaurant Tips Analytics Dashboard', fontsize=16, fontweight='bold')

# Chart 1
sns.barplot(data=df, x='day', y='tip', hue='time', ax=axes[0, 0])
axes[0, 0].set_title('Average Tip by Day & Meal Time')
axes[0, 0].set_xlabel('Day')
axes[0, 0].set_ylabel('Average Tip ($)')

# Chart 2
axes[0, 1].hist(df['tip'], bins=20, color='steelblue', edgecolor='black', alpha=0.7)
axes[0, 1].axvline(df['tip'].mean(), color='red', linestyle='--', label=f'Mean: ${df["tip"].mean():.2f}')
axes[0, 1].set_title('Tip Distribution')
axes[0, 1].set_xlabel('Tip Amount ($)')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].legend()

# Chart 3
party_avg = df.groupby('size')['tip'].mean()
axes[1, 0].bar(party_avg.index, party_avg.values, color='coral', edgecolor='black')
axes[1, 0].set_title('Average Tip by Party Size')
axes[1, 0].set_xlabel('Party Size')
axes[1, 0].set_ylabel('Average Tip ($)')

# Chart 4
gender_smoker = df.groupby(['sex', 'smoker'])['tip'].mean().unstack()
gender_smoker.plot(kind='bar', ax=axes[1, 1], color=['#FF8C42', '#4A90E2'])
axes[1, 1].set_title('Tips: Gender vs Smoking')
axes[1, 1].set_xlabel('Gender')
axes[1, 1].set_ylabel('Average Tip ($)')
axes[1, 1].legend(title='Smoker?')

plt.tight_layout()
plt.savefig('final_dashboard.png', dpi=300, bbox_inches='tight')
plt.close(fig)

print("SUCCESS: Dashboard saved as final_dashboard.png")

# Generate HTML Report
html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Data Visualization Internship Submission</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        h1 {{ color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }}
        h2 {{ color: #34495e; margin-top: 30px; }}
        .insight {{ background-color: #ecf0f1; padding: 15px; border-left: 4px solid #3498db; margin: 15px 0; }}
        .chart {{ margin: 20px 0; text-align: center; }}
        .chart img {{ max-width: 100%; border: 1px solid #ddd; border-radius: 5px; }}
        table {{ width: 100%; border-collapse: collapse; margin: 15px 0; }}
        th, td {{ border: 1px solid #ddd; padding: 10px; text-align: left; }}
        th {{ background-color: #3498db; color: white; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Data Visualization Internship Task</h1>
        <p><strong>Submission Date:</strong> {datetime.now().strftime("%B %d, %Y")}</p>
        
        <h2>Key Insights Dashboard</h2>
        <div class="chart">
            <img src="final_dashboard.png" alt="Dashboard">
            <p><em>Figure 1: Complete Analytics Dashboard</em></p>
        </div>
        
        <h2>Key Findings</h2>
        <div class="insight">
            <strong>Financial Insights:</strong><br>
            Average Tip: ${df['tip'].mean():.2f}<br>
            Average Bill: ${df['total_bill'].mean():.2f}<br>
            Average Tip Percentage: {(df['tip'].sum() / df['total_bill'].sum() * 100):.1f}%
        </div>
        
        <div class="insight">
            <strong>Day-wise Analysis:</strong><br>
            Best Day: {df.groupby('day')['tip'].mean().idxmax()} (${df.groupby('day')['tip'].mean().max():.2f} average tip)<br>
            Worst Day: {df.groupby('day')['tip'].mean().idxmin()} (${df.groupby('day')['tip'].mean().min():.2f} average tip)
        </div>
        
        <div class="insight">
            <strong>Customer Behavior:</strong><br>
            Most Common Party Size: {df['size'].mode()[0]} people<br>
            Smokers average tip: ${df[df['smoker']=='Yes']['tip'].mean():.2f}<br>
            Non-smokers average tip: ${df[df['smoker']=='No']['tip'].mean():.2f}
        </div>
        
        <h2>Tools Used</h2>
        <table>
            <tr><th>Tool</th><th>Purpose</th></tr>
            <tr><td>Python 3.14</td><td>Programming Language</td></tr>
            <tr><td>Pandas</td><td>Data Manipulation</td></tr>
            <tr><td>Matplotlib</td><td>Visualizations</td></tr>
            <tr><td>Seaborn</td><td>Statistical Charts</td></tr>
        </table>
        
        <h2>Task Requirements Checklist</h2>
        <ul>
            <li>Transform raw data into visual formats - DONE</li>
            <li>Use Matplotlib, Seaborn for creating visuals - DONE</li>
            <li>Design visuals that enhance understanding - DONE</li>
            <li>Craft compelling data stories - DONE</li>
            <li>Build portfolio-ready visualizations - DONE</li>
        </ul>
        
        <hr>
        <p style="text-align: center;">Prepared for Data Visualization Internship Position</p>
    </div>
</body>
</html>
"""

with open("submission_report.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("SUCCESS: HTML report saved as submission_report.html")
print("\n" + "="*50)
print("FILES READY FOR SUBMISSION:")
print("="*50)
print("1. final_dashboard.png - Your dashboard")
print("2. README.md - Documentation")
print("3. submission_report.html - Open in browser")
print("="*50)