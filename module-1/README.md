# Student Performance Analysis

A simple mini project using **Python + Pandas** to practice basic data analysis.

## Features
- Handle missing values using mean
- Create `average_score` column
- Find top student
- Filter weak students (<60)
- Calculate class average

## Dataset
Columns: `name`, `math`, `science`, `attendance`

## How it works
- Fill missing values with column mean
- Compute:
  average_score = (math + science) / 2
- Sort to find top student
- Filter students below 60
- Calculate overall average

## Run
```bash
pip install pandas
python mdoule_1_mini_project.py
