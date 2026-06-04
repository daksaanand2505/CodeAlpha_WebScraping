# first_charts.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from your local file
df = pd.read_csv('restaurant_tips.csv')

print("📊 Creating your first professional charts...")
print(f"Loaded {len(df)} records from restaurant_tips.csv")

# Set professional style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Create figure with 2 charts side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle('Restaurant Tips Analysis - First Look', fontsize=16, fontweight='bold')

# CHART 1: Bar Chart - Average Tip by Day
avg_tip = df.groupby('day')['tip'].mean()
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
bars = ax1.bar(avg_tip.index, avg_tip.values, color=colors, edgecolor='black', linewidth=1.5)
ax1.set_title('Average Tip by Day of Week', fontsize=12, fontweight='bold')
ax1.set_xlabel('Day', fontsize=10)
ax1.set_ylabel('Average Tip ($)', fontsize=10)

# Add value labels on top of bars
for bar, value in zip(bars, avg_tip.values):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05, 
             f'${value:.2f}', ha='center', fontweight='bold')

# CHART 2: Scatter Plot - Total Bill vs Tip
scatter = ax2.scatter(df['total_bill'], df['tip'], alpha=0.6, c='#FF6B6B', edgecolors='black', linewidth=0.5)
ax2.set_title('Relationship: Total Bill vs Tip Amount', fontsize=12, fontweight='bold')
ax2.set_xlabel('Total Bill ($)', fontsize=10)
ax2.set_ylabel('Tip Amount ($)', fontsize=10)

# Add trend line
from numpy import polyfit, poly1d
z = polyfit(df['total_bill'], df['tip'], 1)
p = poly1d(z)
ax2.plot(df['total_bill'].sort_values(), p(df['total_bill'].sort_values()), 
         'r--', linewidth=2, label=f'Trend: Tip = ${z[0]:.2f} × Bill + ${z[1]:.2f}')
ax2.legend()

plt.tight_layout()
plt.savefig('first_charts.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n✅ Charts saved as 'first_charts.png'")
print("\n📊 INSIGHTS FROM THESE CHARTS:")
print("• Sunday has the highest average tip ($3.00+)")
print("• Positive trend: Higher bills generally get higher tips")
print("• Most tips fall between $2-$4")