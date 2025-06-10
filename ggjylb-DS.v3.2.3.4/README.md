# DS.v3.2.3.4

# Wine Quality Analysis Project

## Overview
This project analyzes the quality of red wine using regression analysis on physicochemical properties. The dataset contains 1599 samples of red wine with 12 features including the quality rating.

## Dataset Features
- Fixed acidity
- Volatile acidity
- Citric acid
- Residual sugar
- Chlorides
- Free sulfur dioxide
- Total sulfur dioxide
- Density
- pH
- Sulphates
- Alcohol
- Quality (target variable)

## Installation

1. Clone this repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Activate the virtual environment if not already active:
```bash
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Launch Jupyter Lab:
```bash
jupyter lab
```

3. Open `wine_quality.ipynb` in Jupyter Lab and run the cells sequentially to:
   - Load and preprocess the data
   - Perform exploratory data analysis
   - Train and evaluate the GLM model
   - View visualization results

Note: Ensure you have the wine quality dataset (`winequality-red.csv`) in the project root directory

## Analysis Methodology
- Data preprocessing and cleaning
- Exploratory data analysis with correlation analysis
- Binary classification of wine quality (good vs not good)
- Generalized Linear Model (GLM) with logistic regression
- Feature importance analysis
- Model evaluation using pseudo R-squared and visualization

## Tools Used
- Python
- Pandas
- NumPy
- Statsmodels
- Seaborn
- Matplotlib

## Project Structure
- `wine_quality.ipynb`: Main analysis notebook
- `winequality-red.csv`: Dataset (not included in repository)

## Key Findings

### Statistical Analysis
- The GLM model achieved a pseudo R-squared of 0.2009, explaining about 20% of variance in wine quality
- All selected features showed statistical significance (p < 0.05)
- Confidence intervals for all coefficients exclude zero, confirming their significance

### Chemical Properties Impact
1. **Alcohol Content (Most Significant)**
   - Strong positive correlation (r = 0.41) with wine quality
   - Higher alcohol content (>11%) significantly increases quality probability
   - Shows most reliable relationship with narrow confidence intervals
   - Optimal range: 11-14% by volume

2. **Volatile Acidity (Second Most Important)**
   - Significant negative correlation (r = -0.27)
   - Lower values (<0.5 g/L) strongly associated with better quality
   - Higher levels lead to undesirable vinegar taste
   - Optimal range: 0.2-0.4 g/L of acetic acid

3. **Sulphates (Third Most Important)**
   - Moderate positive correlation (r = 0.20)
   - Acts as wine preservative (antimicrobial and antioxidant)
   - Higher levels correlate with better quality
   - Optimal range: 0.6-0.8 g/L of potassium sulphate

### Model Insights
- The relationship between chemical properties and quality is non-linear
- Combined effect of optimal levels in key properties yields highest quality probability
- Alternative models using backward selection did not significantly improve explanatory power
- Model performance suggests existence of unmeasured factors affecting wine quality

### Limitations
- Model explains only 20% of variance, indicating other important unmeasured factors
- Wide confidence bands for volatile acidity and sulphates suggest some uncertainty
- Binary classification might oversimplify the original 0-10 quality scale
