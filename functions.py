import numpy as np
import pandas as pd

SUBJECTS = ["Maths", "Science", "English", "Computer"]
PASS_MARK = 40   # pass condition: at least 40 in every subject

def load_data(path):
    return pd.read_csv(path)

def calculate_totals(df):
    marks = df[SUBJECTS].to_numpy()                 # NumPy array
    df["Total"] = np.sum(marks, axis=1)             # row-wise total
    df["Average"] = np.round(np.mean(marks, axis=1), 2)
    return df

def assign_grade(avg):
    if avg >= 90: return "A+"
    elif avg >= 80: return "A"
    elif avg >= 70: return "B"
    elif avg >= 60: return "C"
    elif avg >= 40: return "D"
    else: return "F"

def add_grades(df):
    grades = []
    for avg in df["Average"]:                       # loop
        grades.append(assign_grade(avg))
    df["Grade"] = grades
    return df

def add_result(df):
    passed = (df[SUBJECTS] >= PASS_MARK).all(axis=1)
    df["Result"] = np.where(passed, "Pass", "Fail")
    return df

def subject_analysis(df):
    for subject in SUBJECTS:                        # loop
        print(f"{subject:<10} Avg: {df[subject].mean():6.2f} | "
              f"Highest: {df[subject].max()} | Lowest: {df[subject].min()}")

def top_performers(df, n=3):
    return df.nlargest(n, "Average")[["Student_ID", "Name", "Total", "Average", "Grade"]]