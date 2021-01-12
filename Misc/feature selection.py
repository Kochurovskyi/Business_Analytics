import numpy as np
import pandas as pd
from xgboost import XGBClassifier
import matplotlib.pyplot as plt

df = pd.read_csv('model_1.csv', index_col='customer_id')
lst = ['age', 'age_youngest_child', 'debt_equity', 'gender',
        'bad_payment', 'gold_card', 'pension_plan', 'household_debt_to_equity_ratio',
        'income', 'members_in_household', 'months_current_account',
        'months_customer', 'call_center_contacts', 'loan_accounts',
        'number_products', 'number_transactions', 'non_worker_percentage',
        'white_collar_percentage', 'rfm_score']
X = df[lst]
y = df['Savings'] #['Mortgage', 'Pension', 'Savings']
print(y)
model = XGBClassifier()
model.fit(X,y)
# feature importance
print(model.feature_importances_)
# plot
plt.figure(figsize=(16,8))
plt.bar(range(len(model.feature_importances_)), model.feature_importances_)
plt.xticks(range(len(lst)), lst, rotation=90)
plt.show()
