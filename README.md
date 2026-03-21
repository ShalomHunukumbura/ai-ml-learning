# AI/ML Learning Journey

This repository tracks my hands-on AI/ML learning progress, starting with Python data analysis fundamentals using Pandas and NumPy.

## Progress So Far

### Module 1 - Foundations with Pandas and NumPy

#### Day 1 - Pandas Basics and Intro Data Tasks
- Built and explored DataFrames (`head`, `info`, `describe`)
- Practiced filtering, sorting, grouping, and basic feature engineering
- Worked on student-performance and product-value exercises
- Added derived fields like grades and total value

Files:
- `module-1/day-1/module_1_practice_pandas_intro.py`
- `module-1/day-1/module_1_mini_project.py`
- `module-1/day-1/README.md`

#### Day 2 - Data Cleaning and CSV Workflow
- Loaded datasets from CSV files
- Handled missing values and duplicates
- Standardized text values (like names)
- Converted messy numeric columns with `pd.to_numeric(..., errors="coerce")`
- Cleaned real-world style messy data and exported cleaned output
- Added ranking/performance features after cleaning

Files:
- `module-1/day-2/module_1_day_2_practice.py`
- `module-1/day-2/module_1_day_2_mini_project.py`
- `module-1/day-2/students.csv`
- `module-1/day-2/messy_students.csv`
- `module-1/day-2/attendance_bonus.csv`
- `module-1/day-2/cleaned_students.csv`

#### Day 3 - NumPy Fundamentals and Simple Prediction
- Practiced NumPy array creation, shapes, and indexing
- Performed element-wise operations and broadcasting
- Used dot product for a simple prediction calculation
- Built a small mini project to predict scores from two input features

Files:
- `module-1/day-3/module_1_day_3_practice.py`
- `module-1/day-3/module_1_day_3_mini_project.py`

## Repository Structure

```text
ai-ml/
  module-1/
    day-1/
      README.md
      module_1_practice_pandas_intro.py
      module_1_mini_project.py
    day-2/
      students.csv
      messy_students.csv
      attendance_bonus.csv
      cleaned_students.csv
      module_1_day_2_practice.py
      module_1_day_2_mini_project.py
    day-3/
      module_1_day_3_practice.py
      module_1_day_3_mini_project.py
```

## Run the Code

From project root:

```bash
source .venv/bin/activate
```

Day 1:

```bash
python module-1/day-1/module_1_practice_pandas_intro.py
python module-1/day-1/module_1_mini_project.py
```

Day 2:

```bash
cd module-1/day-2
python module_1_day_2_practice.py
python module_1_day_2_mini_project.py
```

Day 3:

```bash
python module-1/day-3/module_1_day_3_practice.py
python module-1/day-3/module_1_day_3_mini_project.py
```

## Next Learning Goals
- Strengthen EDA workflow and visualization (Matplotlib/Seaborn)
- Improve data validation and reusable cleaning functions
- Start basic machine learning models after data prep fundamentals
