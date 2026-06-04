# submission_checklist.py
import os

print("=" * 50)
print("SUBMISSION CHECKLIST")
print("=" * 50)

# Check all required files
files_to_check = [
    'final_dashboard.png',
    'first_charts.png',
    'restaurant_tips.csv',
    'final_dashboard.py',
    'first_charts.py',
    'data_exploration.py',
    'README.md',
    'submission_report.html'
]

print("\nFiles in your submission package:")
print("-" * 40)

all_exist = True
for file in files_to_check:
    if os.path.exists(file):
        size = os.path.getsize(file)
        print(f"✓ {file} ({size:,} bytes)")
    else:
        print(f"✗ {file} - MISSING")
        all_exist = False

print("-" * 40)

if all_exist:
    print("\n✅ All files are ready for submission!")
    print("\n📦 TO CREATE ZIP FILE:")
    print("1. Select all 8 files listed above")
    print("2. Right-click and choose 'Send to' > 'Compressed (zipped) folder'")
    print("3. Name it: YourName_DataVisualization_Submission.zip")
    print("4. Attach the ZIP file to your internship email/application")
else:
    print("\n⚠️ Some files are missing. Run final_dashboard.py first.")

print("\n" + "=" * 50)