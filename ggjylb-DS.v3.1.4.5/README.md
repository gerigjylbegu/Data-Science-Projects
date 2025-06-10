# Coursera Data Analysis Project

This project involves exploratory data analysis (EDA) of a Coursera dataset. The analysis includes data pre-processing, visualization, and correlation analysis to understand the relationships between different features of the dataset.

## Project Structure

- **coursera_data.csv**: The dataset containing information about various Coursera courses.
- **functions.py**: Python module containing helper functions for outlier detection and correlation analysis.
- **coursera_data.ipynb**: Jupyter notebook containing the EDA process, including data loading, cleaning, visualization, and analysis.
- **requirements.txt**: List of Python packages required to run the Jupyter notebook and perform the analysis.

## Installation

To install the required packages, run:
```bash
pip install -r requirements.txt
```

## Usage

Open the Jupyter notebook and run the cells to perform the analysis:
```bash
jupyter notebook coursera_data.ipynb
```

## Analysis Overview

1. **Data Loading**: Importing necessary libraries and loading the dataset.
2. **Data Pre-processing**: Checking for missing values, duplicates, and outliers. Converting data types where necessary.
3. **Visualization**: Creating visual representations of the data distributions and relationships using libraries like Matplotlib, Seaborn, and Plotly.
4. **Correlation Analysis**: Analyzing the relationships between numerical features using scatter plots and correlation matrices.
5. **Comparative Analysis**: Comparing different organizations and courses based on ratings and participation.

## Results

The analysis provides insights into:
- The distribution of course ratings and student enrollments.
- The relationship between course ratings and the number of students enrolled.
- The impact of course difficulty and certificate type on ratings and enrollments.

## Conclusion

This project demonstrates how to perform exploratory data analysis on a Coursera dataset, providing valuable insights into the factors that influence course ratings and student enrollments.
