# Travel Insurance Prediction

## Project Structure
The project consists of the following main files:

- `Travel_insurance.ipynb`: Main Jupyter notebook containing the full analysis, including EDA, statistical testing, and model development
- `TravelInsurancePrediction.csv`: Dataset containing customer information and insurance purchase data
- `functions.py`: Helper functions used in the analysis for statistical testing and model evaluation
- `requirements.txt`: List of Python dependencies required to run the project
- `README.md`: Documentation of the project (this file)

## Installation & Usage
```python
# Install required packages
pip install -r requirements.txt

# Run the notebook
jupyter notebook Travel_insurance.ipynb
```

## Project Overview
This project analyzes customer data to predict travel insurance purchases. Using machine learning models, we identify key factors influencing insurance buying decisions and develop a predictive model to help target potential customers effectively.

## Dataset Description
The dataset contains information from 1,987 customers who were offered travel insurance in 2019. Features include:

- **Age**: Customer's age (25-35 years)
- **Employment Type**: Customer's employment sector 
- **GraduateOrNot**: Whether the customer is a college graduate
- **AnnualIncome**: Yearly income (Indian Rupees, rounded to nearest 50,000)
- **FamilyMembers**: Number of family members (2-9)
- **ChronicDiseases**: Whether the customer has any major diseases
- **FrequentFlyer**: Whether customer booked flights at least 4 times in last 2 years 
- **EverTravelledAbroad**: Whether customer has traveled internationally
- **TravelInsurance**: Whether customer purchased travel insurance (target variable)

## Key Findings

### Customer Profile Analysis
- Majority are employed in private sector/self-employed
- Average annual income: ₹932,763
- Median family size: ~5 members
- Target variable is imbalanced (64% did not purchase insurance)

### Most Influential Predictors
1. **Previous Travel Experience**: International travel history strongly correlates with insurance purchase
2. **Annual Income**: Higher income customers more likely to buy insurance
3. **Frequent Flyer Status**: Regular travelers show higher propensity to purchase
4. **Age**: Slight preference for insurance among customers over 33 years
5. **Family Size**: Larger families tend to purchase more frequently
6. **Employment Type**: Private sector employees show higher insurance purchase rates

### Model Performance
Random Forest classifier achieved the best results:
- Accuracy: 81%
- Precision: 79.1%
- Recall: 61.3%
- F1 Score: 69.1%
- ROC AUC: 77.4%

These metrics significantly outperform the baseline model (64% accuracy).

## Implementation Details

### Data Preprocessing
1. Feature encoding:
   - Categorical variables converted to binary 
   - Numerical features normalized using MinMaxScaler
2. Feature selection based on statistical significance:
   - Chi-squared tests for categorical features
   - Mann-Whitney U tests for numerical features

### Model Development
1. Model Selection:
   - SVM with RBF kernel
   - Random Forest
   - Gradient Boosting
2. Hyperparameter Tuning:
   - RandomizedSearchCV with 5-fold cross-validation
   - Optimized for recall while maintaining precision

## Recommendations

### For Business Implementation
1. Prioritize marketing to customers with:
   - International travel history
   - Higher income levels
   - Frequent flyer status
2. Consider age-specific marketing strategies
3. Develop family-oriented insurance packages

### For Model Improvement
1. Collect additional features:
   - Travel frequency details
   - Risk perception metrics
   - Previous insurance claims
2. Address class imbalance using advanced techniques
3. Implement continuous model monitoring and updates