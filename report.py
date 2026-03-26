import pandas as pd

df = pd.read_csv("Attendance.csv", names=["Name","Time","Date"])

summary = df.groupby("Name").count()["Date"]

print("\n📊 Attendance Report:")
print(summary)

summary.to_csv("Report.csv")

print("✅ Report Saved (Report.csv)")