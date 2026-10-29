from functions import *

df = load_data("students.csv")

print("=== DATA OVERVIEW ===")
print(df.head())
print("Columns:", list(df.columns))
print("Total records:", len(df))
df.info()

df = calculate_totals(df)
df = add_grades(df)
df = add_result(df)

print("\n=== FULL RESULT TABLE ===")
print(df[["Student_ID", "Name", "Total", "Average", "Grade", "Result"]])

print("\n=== CLASS ANALYSIS ===")
best = df.loc[df["Average"].idxmax()]
worst = df.loc[df["Average"].idxmin()]
print(f"Highest average: {best['Name']} ({best['Average']})")
print(f"Lowest average : {worst['Name']} ({worst['Average']})")
print(f"Overall class average: {df['Average'].mean():.2f}")
print(f"Passed: {(df['Result']=='Pass').sum()} | Failed: {(df['Result']=='Fail').sum()}")

print("\n=== GRADE DISTRIBUTION ===")
print(df["Grade"].value_counts())

print("\n=== SUBJECT-WISE ANALYSIS ===")
subject_analysis(df)
avgs = df[SUBJECTS].mean()
print("Best subject:", avgs.idxmax(), "| Weakest subject:", avgs.idxmin())

print("\n=== TOP 3 PERFORMERS ===")
print(top_performers(df, 3))

# Optional extras: department-wise average, low-attendance students
print("\n=== DEPARTMENT AVERAGES ===")
print(df.groupby("Department")["Average"].mean().round(2))
print("\n=== ATTENDANCE BELOW 75% ===")
print(df[df["Attendance"] < 75][["Name", "Attendance"]])

df.to_csv("results.csv", index=False)   # optional: save processed data