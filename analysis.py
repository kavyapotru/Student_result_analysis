import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import os

# ── 1. Load CSV into SQLite Database ──
conn = sqlite3.connect("students.db")
df = pd.read_csv("students.csv")
df.to_sql("students", conn, if_exists="replace", index=False)
print("✅ Data loaded into database successfully!")

# ── 2. SQL Queries for Analysis ──

# Average score per subject
avg_query = """
SELECT 
    ROUND(AVG(Maths), 2) AS Avg_Maths,
    ROUND(AVG(Physics), 2) AS Avg_Physics,
    ROUND(AVG(Chemistry), 2) AS Avg_Chemistry,
    ROUND(AVG(Python), 2) AS Avg_Python,
    ROUND(AVG(English), 2) AS Avg_English
FROM students
"""
avg_df = pd.read_sql_query(avg_query, conn)
print("\n📊 Subject-wise Average Scores:")
print(avg_df.to_string(index=False))

# Calculate total and percentage for each student
df["Total"] = df[["Maths", "Physics", "Chemistry", "Python", "English"]].sum(axis=1)
df["Percentage"] = (df["Total"] / 500 * 100).round(2)
df["Result"] = df["Percentage"].apply(lambda x: "Pass" if x >= 50 else "Fail")

# Pass/Fail count
pass_fail = df["Result"].value_counts()
print(f"\n✅ Pass: {pass_fail.get('Pass', 0)} students")
print(f"❌ Fail: {pass_fail.get('Fail', 0)} students")

# Top 3 students
top3 = df.nlargest(3, "Percentage")[["Name", "Percentage", "Result"]]
print("\n🏆 Top 3 Students:")
print(top3.to_string(index=False))

# ── 3. Visualizations ──
os.makedirs("charts", exist_ok=True)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Student Result Analysis Dashboard", fontsize=16, fontweight="bold")

# Chart 1 - Subject Average Bar Chart
subjects = ["Maths", "Physics", "Chemistry", "Python", "English"]
averages = [avg_df[f"Avg_{s}"].values[0] for s in subjects]
axes[0, 0].bar(subjects, averages, color=["#4C72B0","#DD8452","#55A868","#C44E52","#8172B2"])
axes[0, 0].set_title("Subject-wise Average Scores")
axes[0, 0].set_ylabel("Average Score")
axes[0, 0].set_ylim(0, 100)
for i, v in enumerate(averages):
    axes[0, 0].text(i, v + 1, str(v), ha="center", fontsize=9)

# Chart 2 - Pass/Fail Pie Chart
axes[0, 1].pie(pass_fail.values, labels=pass_fail.index,
               autopct="%1.1f%%", colors=["#55A868", "#C44E52"], startangle=90)
axes[0, 1].set_title("Pass / Fail Ratio")

# Chart 3 - Student Percentage Bar Chart
colors = ["#55A868" if r == "Pass" else "#C44E52" for r in df["Result"]]
axes[1, 0].bar(df["Name"], df["Percentage"], color=colors)
axes[1, 0].set_title("Student-wise Percentage")
axes[1, 0].set_ylabel("Percentage (%)")
axes[1, 0].set_xticklabels(df["Name"], rotation=45, ha="right", fontsize=8)
axes[1, 0].axhline(y=50, color="black", linestyle="--", linewidth=1, label="Pass Line (50%)")
axes[1, 0].legend()

# Chart 4 - Top 5 Students
top5 = df.nlargest(5, "Percentage")
axes[1, 1].barh(top5["Name"], top5["Percentage"], color="#4C72B0")
axes[1, 1].set_title("Top 5 Students")
axes[1, 1].set_xlabel("Percentage (%)")
axes[1, 1].set_xlim(0, 100)
for i, v in enumerate(top5["Percentage"]):
    axes[1, 1].text(v + 0.5, i, f"{v}%", va="center", fontsize=9)

plt.tight_layout()
plt.savefig("charts/dashboard.png", dpi=150, bbox_inches="tight")
print("\n📈 Dashboard saved to charts/dashboard.png")

# ── 4. Auto Report ──
with open("report.txt", "w") as f:
    f.write("=" * 50 + "\n")
    f.write("   STUDENT RESULT ANALYSIS REPORT\n")
    f.write("=" * 50 + "\n\n")
    f.write(f"Total Students  : {len(df)}\n")
    f.write(f"Pass            : {pass_fail.get('Pass', 0)}\n")
    f.write(f"Fail            : {pass_fail.get('Fail', 0)}\n")
    f.write(f"Pass Percentage : {round(pass_fail.get('Pass',0)/len(df)*100, 2)}%\n\n")
    f.write("Subject-wise Averages:\n")
    for s in subjects:
        f.write(f"  {s:12}: {avg_df[f'Avg_{s}'].values[0]}\n")
    f.write("\nTop 3 Students:\n")
    for _, row in top3.iterrows():
        f.write(f"  {row['Name']:10}: {row['Percentage']}%\n")

print("📄 Report saved to report.txt")
print("\n✅ Analysis Complete!")

conn.close()
