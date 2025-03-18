# Import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from flask import Flask, render_template
import plotly  # Add this import
import plotly.express as px
import plotly.graph_objects as go
import json

# Load and preprocess data
data = pd.read_csv('trial_dashboard_data.csv')
data['days_enrolled'] = (pd.to_datetime('2025-06-30') - pd.to_datetime(data['enrollment_date'])).dt.days
X = data[['age', 'days_enrolled']]
y = data['dropout']

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train model
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)
accuracy = model.score(X_test, y_test)
print(f"Dropout Prediction Accuracy: {accuracy:.2f}")

# Flask app
app = Flask(__name__)

@app.route('/')
def dashboard():
    # Retention trend
    retention = data.groupby('days_enrolled')['dropout'].mean().reset_index()
    fig1 = px.line(retention, x='days_enrolled', y='dropout', title='Dropout Rate Over Time')

    # Efficacy by group
    efficacy = data.groupby('treatment_group')['outcome'].mean().reset_index()
    fig2 = px.bar(efficacy, x='treatment_group', y='outcome', title='Efficacy by Treatment Group')

    # Dropout risk prediction
    data['dropout_risk'] = model.predict_proba(X_scaled)[:, 1]
    fig3 = px.histogram(data, x='dropout_risk', color=data['dropout'].astype(str), title='Dropout Risk Distribution')

    # Convert plots to JSON
    graph1 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    graph2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    graph3 = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', graph1=graph1, graph2=graph2, graph3=graph3)

if __name__ == '__main__':
    app.run(debug=True)
