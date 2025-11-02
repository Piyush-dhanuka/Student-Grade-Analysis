import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

INPUT_FILE = "student_grades.csv"
OUTPUT_FILE = "analysis_report_comprehensive.txt"

SUBJECT_COLS = ['Math_Marks', 'Science_Marks', 'English_Marks']

def load_and_process_data(file_path):
    """Loads CSV data, cleans data, calculates total average, and assigns status."""
    print(f"--- 1. Loading and Processing data from {file_path} ---")
    try:
        df = pd.read_csv(file_path)
        
        for col in SUBJECT_COLS:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        
        df[SUBJECT_COLS] = df[SUBJECT_COLS].fillna(df[SUBJECT_COLS].mean())
        
        df['Overall_Average'] = df[SUBJECT_COLS].mean(axis=1) 

        PASS_MARK = 70
        df['Status'] = np.where(df['Overall_Average'] >= PASS_MARK, 'Pass', 'Fail')
        
        print("Data Loaded, Cleaned, and Enhanced:")
        print(df[['RollNumber', 'Name', 'Overall_Average', 'Status']].head())
        
        return df
    except FileNotFoundError:
        print(f"Error: Input file '{file_path}' not found. Please create it.")
        return None

def calculate_key_stats(df):
    """Calculates key overall statistics and subject-wise means."""
    print("\n--- 2. Calculating Key Statistics (NumPy/Pandas) ---")
    
    stats = {}
    
    stats['Total_Students'] = len(df)
    stats['Overall_Class_Average'] = df['Overall_Average'].mean()
    stats['Pass_Count'] = len(df[df['Status'] == 'Pass'])
    
    stats['Subject_Averages'] = {
        col: df[col].mean() for col in SUBJECT_COLS
    }
    
    stats['Unique_Statuses'] = set(df['Status'])
    
    return stats

def generate_visualization(df):
    """Creates a simple visualization comparing subject averages."""
    print("\n--- 4. Generating Simple Visualization (Seaborn) ---")
    
    subject_means = df[SUBJECT_COLS].mean().reset_index()
    subject_means.columns = ['Subject', 'Average_Mark']
    
    plt.figure(figsize=(7, 5))
    sns.barplot(x='Subject', y='Average_Mark', data=subject_means, palette='viridis')
    plt.title('Subject-wise Average Marks')
    plt.ylim(60, 100)
    plt.xlabel('Subject')
    plt.ylabel('Average Mark (%)')
    plt.show()

def generate_report(stats_dict):
    """Writes the statistical summary to an output file."""
    print(f"\n--- 3. Generating Report to {OUTPUT_FILE} ---")
    
    with open(OUTPUT_FILE, 'w') as file:
        file.write("===== Comprehensive Student Performance Report =====\n\n")
        file.write(f"Total Students Analyzed: {stats_dict['Total_Students']}\n")
        file.write(f"Overall Class Average Mark: {stats_dict['Overall_Class_Average']:.2f}\n")
        file.write(f"Total Students Passed: {stats_dict['Pass_Count']}\n")
        file.write("----------------------------------------------\n")
        file.write("Subject-wise Averages:\n")
        
        for subject, avg in stats_dict['Subject_Averages'].items():
            file.write(f"- {subject}: {avg:.2f}\n")
        
    print(f"✅ Detailed analysis report saved to {OUTPUT_FILE}")

def main():
    """Main function to run the project pipeline."""
    
    data_frame = load_and_process_data(INPUT_FILE)
    
    if data_frame is not None:
        stats = calculate_key_stats(data_frame)
        generate_report(stats)
        generate_visualization(data_frame)

if __name__ == "__main__":
    main()