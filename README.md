# Healthcare AI Dashboard for Trial Optimization

## Overview
This project builds an AI-powered dashboard for visualizing and predicting clinical trial outcomes, such as patient retention and efficacy trends. Inspired by Pfizer's AWS PACT trial optimization efforts, the dashboard integrates predictive modeling with interactive visuals to provide actionable insights for trial management.

## Features
- **Predicts Patient Dropout**: Uses logistic regression to estimate the risk of patient dropout.
- **Interactive Data Visualizations**: Retention trends, treatment efficacy comparisons, and dropout risk distribution.
- **Real-time Analytics**: Provides insights that align with Pfizer's data-driven approach to trial monitoring.

## Tech Stack
- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Frontend**: Plotly, HTML, JavaScript

## Project Architecture
1. **Input Layer**: Synthetic trial dataset with patient enrollment and outcome metrics.
2. **Preprocessing**: Data cleaning, encoding categorical variables, and feature engineering.
3. **Predictive Model**: Logistic Regression to analyze dropout risk.
4. **Dashboard**: Flask-based web interface displaying Plotly visualizations.
5. **Output Layer**: Web-accessible analytics for real-time insights.

## Installation
### Prerequisites
Ensure you have Python 3 installed. Then, install dependencies:
```sh
pip install pandas numpy scikit-learn flask plotly
```

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/healthcare-ai-dashboard.git
   cd healthcare-ai-dashboard
   ```
2. Generate synthetic dataset:
   ```sh
   python generate_data.py
   ```
3. Run the application:
   ```sh
   python app.py
   ```
4. Open your browser and visit: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## File Structure
```
healthcare-ai-dashboard/
│── app.py                   # Flask application with AI model integration
│── generate_data.py         # Script to create synthetic trial dataset
│── trial_dashboard_data.csv # Generated dataset
│── templates/
│   └── dashboard.html       # HTML template for dashboard
│── static/
│   └── style.css            # Optional CSS file for styling
│── README.md                # Documentation
```

## Usage
- **Retention Trend Analysis**: Identifies patient dropout rates over time.
- **Treatment Efficacy**: Compares outcomes between treatment and placebo groups.
- **Dropout Risk Prediction**: Estimates individual patient dropout probability.

## Expected Outcomes
- **>75% Accuracy** in dropout prediction using Logistic Regression.
- **Improved Trial Management** by providing early dropout risk warnings.
- **Potential Pfizer Application** for real-time trial optimization.

## References
1. Pfizer. (2025). "AWS PACT for Clinical Trials." pfizer.com.
2. Flask Documentation: [https://flask.palletsprojects.com](https://flask.palletsprojects.com)
3. Plotly Documentation: [https://plotly.com/python](https://plotly.com/python)

## License
This project is open-source and available under the MIT License.

---
### Contribute
Feel free to fork the repo, submit issues, or suggest improvements!

