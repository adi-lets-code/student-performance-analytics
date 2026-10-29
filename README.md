# Student Performance Analytics System

## 1. Project Title
**Student Performance Analytics System**

- **Student Name:** Adithya Gupta
- **Course:** Python with AI, EWB Courses
- **Submitted on:** 29 oct 2026

## 2. Objective
Teachers often have to calculate totals, averages, grades and pass/fail results for every student by hand, which is slow and error-prone. This project automates that process. It reads student records from a CSV file, calculates the results with Python, and shows class-level and subject-level analysis, so the performance of a class can be understood quickly.

## 3. Technologies Used
- Python 3
- NumPy (numerical calculations)
- Pandas (loading and analysing data)
- Git and GitHub (version control and submission)

## 4. Dataset Description
The file `students.csv` contains **20 student records** with 8 columns:

| Column | Description |
|---|---|
| Student_ID | Unique ID of the student |
| Name | Student name |
| Department | CSE, ECE, IT or ME |
| Maths, Science, English, Computer | Marks out of 100 in each subject |
| Attendance | Attendance percentage |

## 5. Implementation
1. **Load data:** `pd.read_csv()` reads `students.csv` into a Pandas DataFrame. The columns, number of records and basic info are displayed.
2. **Total and average:** the subject marks are converted to a NumPy array. `np.sum()` and `np.mean()` with `axis=1` give each student's total and average.
3. **Grades:** a function checks each student's average and assigns a grade, using a loop.
   - A+ : 90 and above
   - A : 80 to 89
   - B : 70 to 79
   - C : 60 to 69
   - D : 40 to 59
   - F : below 40
4. **Pass/Fail:** a student passes only if they score at least 40 in every subject. This is applied with `np.where()`.
5. **Analysis:** the program finds the highest and lowest average, the overall class average, the pass/fail count, the grade distribution, subject-wise statistics, the top 3 performers, department-wise averages and students with attendance below 75%.

## 6. Key Features
- `load_data()` loads the CSV file
- `calculate_totals()` calculates total and average marks with NumPy
- `assign_grade()` and `add_grades()` assign grades
- `add_result()` finds pass/fail status
- `subject_analysis()` shows the highest, lowest and average marks for each subject
- `top_performers()` lists the top students
- Department-wise analysis and a low-attendance report

## 7. Output / Screenshots

![Output 1] <img width="756" height="637" alt="image" src="https://github.com/user-attachments/assets/8b642d56-771f-468e-841f-1369512a3c1a" />

![Output 2] <img width="865" height="647" alt="image" src="https://github.com/user-attachments/assets/75f9f6dc-f25c-4cbf-a42c-305e28c39dd4" />


## 8. Final Outcome
The project reads the student dataset and produces a complete performance report: individual totals, averages, grades and results, plus class statistics, subject-wise analysis and top performers. All of it is displayed clearly in the terminal without needing to read the code.

## 9. Challenges & Learning

**1. Understanding the `axis` parameter in NumPy**
At first I was not sure whether `np.sum()` and `np.mean()` were adding up the marks of each student or of each subject. I tested with `axis=0` and `axis=1` on a small array and printed the results. I learned that `axis=1` calculates across a row (one student's subjects) and `axis=0` calculates down a column (one subject for all students).

**2. Deciding the pass/fail condition**
I first thought of using only the average marks to decide pass or fail. But then a student could fail a subject and still pass overall. So I defined a clearer rule: a student passes only if they score at least 40 in every subject. I used `.all(axis=1)` and `np.where()` to apply it.

**3. Column names not matching**
I got a `KeyError` because the column names in my code did not exactly match the headers in `students.csv`. I fixed it by checking `df.columns` and using the same spelling and capital letters. Now I keep the subject names in one `SUBJECTS` list, so they only need to be changed in one place.

**4. Uploading the project to GitHub**
My repository had only the README at first, and I had to upload `main.py`, `functions.py` and `students.csv` separately. I learned how to create a repository, upload files, commit changes and check that everything is visible in the browser.

**What I learned**
- How to use NumPy and Pandas together for data analysis
- How to write reusable functions and use loops where needed
- How to turn a requirement (grading rule, pass condition) into working code
- How to organise a project and submit it on GitHub with documentation

## 10. GitHub Repository
https://github.com/adi-lets-code/student-performance-analytics

## How to Run
```
pip install numpy pandas
python main.py
```
