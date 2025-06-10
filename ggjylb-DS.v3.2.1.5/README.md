# Mental health in the Tech industry Project

This project analyzes mental health trends in the tech industry using survey data and various data science techniques.

## Analysis Overview

- **Data Import & Preprocessing**: Load and clean data from an SQLite database.
- **Demographic Analysis**: Examine gender, age, and geographic distributions.
- **Mental Health Conditions**: Assess prevalence rates and confidence intervals for mental disorders.
- **Correlation Studies**: Explore relationships between family history, treatment seeking, workplace wellness programs, and company size.
- **Visualizations**: Generate insights using Matplotlib, Seaborn, and Plotly.

## Installation

To set up the environment for this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ggjylb-DS.v3.2.1.5
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

- README.md: Project overview.
- mental_health.ipynb: Main analysis notebook.
- mental_health.sqlite: Database used for the analysis.
- OECD_emplyment_rate.csv: Dataset containing data on worldwide age-group specific emplyment rate.
- requirements.txt: List of required Python packages for the project.

## Data Sources

- Survey and questionnaire data stored in an SQLite database.
- OECD employment data for comparison.

## Usage

Open the Jupyter notebook and run the cells to perform the analysis:
```bash
jupyter notebook mental_health.ipynb
```

## Conclusion

This project highlights several important insights into mental health within the tech industry:

1. **Demographics**: The survey data reveals a significant gender imbalance, with males being overrepresented. However, the age distribution aligns closely with global employment trends, while geographic representation is predominantly skewed toward the United States.

2. **Mental Health Prevalence**: Mental health conditions such as mood disorders, anxiety disorders, and ADHD are the most common among respondents. The tech industry exhibits a notably higher prevalence of mental health issues compared to other industries.

3. **Workplace Dynamics**: Employees are generally open to discussing mental health with both coworkers and employers, with minimal negative repercussions reported. Larger companies tend to foster environments where employees are more likely to seek mental health treatment.

4. **Family History**: There is a moderate association between family history and the likelihood of experiencing mental health conditions, though causation cannot be definitively established.

5. **Wellness Programs**: While workplace wellness programs show a weak positive correlation with reducing mental health stigma, they are not the sole determinant of whether mental health is taken seriously in the workplace.

Overall, the findings underscore the need for more inclusive sampling, better mental health support systems, and continued efforts to reduce stigma in the workplace, particularly in the tech industry.