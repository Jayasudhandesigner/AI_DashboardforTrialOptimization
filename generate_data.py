import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)
n_patients = 500
start_date = datetime(2025, 1, 1)

data = {
    'patient_id': range(1, n_patients + 1),
    'enrollment_date': [start_date + timedelta(days=np.random.randint(0, 180)) for _ in range(n_patients)],
    'age': np.random.randint(18, 81, n_patients),
    'treatment_group': np.random.choice(['A', 'B'], n_patients),
    'dropout': np.random.choice([0, 1], n_patients, p=[0.8, 0.2]),  # 20% dropout rate
    'outcome': np.random.choice([0, 1], n_patients)
}
df = pd.DataFrame(data)
df.to_csv('trial_dashboard_data.csv', index=False)
print("Synthetic dataset saved as 'trial_dashboard_data.csv'")
print(df.head())