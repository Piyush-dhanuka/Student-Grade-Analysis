Student Grades Analysis

This project analyzes student performance data from a CSV file, generates statistical summaries, and visualizes subject-wise averages.

Files

project.py – Main Python script that loads, cleans, analyzes, and visualizes student grade data.

student_grades.csv – Input dataset containing student marks in Math, Science, and English.

analysis_report_comprehensive.txt – Auto-generated output report summarizing overall and subject-wise performance.

Features

Loads and cleans CSV data using pandas

Handles missing values by filling them with column averages

Calculates each student’s overall average and pass/fail status

Generates statistical summaries using NumPy/Pandas

Exports a formatted text report

Creates bar chart visualization of subject averages using Seaborn/Matplotlib

Requirements

Install the required dependencies:

pip install pandas numpy seaborn matplotlib

Usage

Run the main script:

python project.py


This will:

Load data from student_grades.csv

Process and analyze grades

Save a detailed report to analysis_report_comprehensive.txt

Display a visualization of average marks per subject

Example Output
===== Comprehensive Student Performance Report =====
Total Students Analyzed: 60
Overall Class Average Mark: 74.23
Total Students Passed: 45
----------------------------------------------
Subject-wise Averages:
- Math_Marks: 68.61
- Science_Marks: 74.96
- English_Marks: 79.12

Author

Developed as a simple data analysis and visualization pipeline using Python.
