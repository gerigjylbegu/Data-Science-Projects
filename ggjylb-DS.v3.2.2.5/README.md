# DS.v3.2.2.5 - A/B Testing Project

This repository contains analysis of two A/B testing scenarios using Python and data visualization tools.

## Installation

1. Download the content of the repository.

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Jupyter Notebooks:
   - Launch Jupyter Lab/Notebook:
   ```bash
   jupyter lab
   ```
   - Open either notebook:
     - `cookie_cats.ipynb`: Analysis of gate placement impact
     - `Fast_Food_Marketing_Campaign.ipynb`: Marketing strategy evaluation

2. Dashboard:
   - Open `A_B_test_project_dashboard.pdf`

## Project Structure

- `cookie_cats.ipynb`: Analysis of gate placement impact in Cookie Cats mobile game
- `Fast_Food_Marketing_Campaign.ipynb`: Evaluation of marketing strategies for a fast-food chain
- `A_B_test_project_dashboard.pdf`: PDF version of the project dashboard

## Key Findings

### Cookie Cats Mobile Game A/B Test
Analyzed impact of gate placement (level 30 vs 40) on player retention and engagement:

- No significant difference in total gameplay rounds between versions
- Gate at level 30 showed significantly higher 7-day retention rates
- Recommendation: Implement gate at level 30 for better long-term player retention

### Fast Food Marketing Campaign Analysis
Evaluated three different marketing strategies for a new menu item:

- Promotion Strategy 1 demonstrated highest sales performance
- Promotion Strategy 3 showed moderate results
- Promotion Strategy 2 had lowest impact
- Results consistent across different market sizes and store conditions
- Recommendation: Implement Promotion Strategy 1 for new menu item launch

## Dashboard Access 
The interactive project dashboard can be accessed [here](https://lookerstudio.google.com/embed/reporting/606fa7b1-ab96-4eb1-9883-9f96525a7965/page/0T8HF).
A PDF version is also available in this repository.