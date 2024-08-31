import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Number of customers
n_customers = 1000

# Generate customer IDs
customer_ids = range(1, n_customers + 1)

# Generate ages (between 18 and 80)
ages = np.random.randint(18, 81, n_customers)

# Generate annual incomes (between $20,000 and $200,000)
annual_incomes = np.random.randint(20000, 200001, n_customers)

# Generate spending scores (1-100)
spending_scores = np.random.randint(1, 101, n_customers)

# Generate total purchases (between 1 and 100)
total_purchases = np.random.randint(1, 101, n_customers)

# Generate average purchase values (between $10 and $1000)
avg_purchase_values = np.random.uniform(10, 1000, n_customers).round(2)

# Calculate customer lifetime value (a function of total purchases and avg purchase value)
customer_lifetime_values = (total_purchases * avg_purchase_values * np.random.uniform(0.8, 1.2, n_customers)).round(2)

# Generate registration dates (within the last 5 years)
end_date = datetime.now()
start_date = end_date - timedelta(days=5*365)
registration_dates = [start_date + timedelta(days=np.random.randint(0, (end_date - start_date).days)) for _ in range(n_customers)]

# Generate last purchase dates (after registration date but before current date)
last_purchase_dates = [reg_date + timedelta(days=np.random.randint(0, (end_date - reg_date).days)) for reg_date in registration_dates]

# Generate customer types
customer_types = np.random.choice(['New', 'Regular', 'VIP'], n_customers, p=[0.3, 0.5, 0.2])

# Generate preferred product categories
product_categories = ['Electronics', 'Clothing', 'Home & Garden', 'Books', 'Sports', 'Beauty']
preferred_categories = [', '.join(np.random.choice(product_categories, np.random.randint(1, 4), replace=False)) for _ in range(n_customers)]

# Create the DataFrame
df = pd.DataFrame({
    'customer_id': customer_ids,
    'age': ages,
    'annual_income': annual_incomes,
    'spending_score': spending_scores,
    'total_purchases': total_purchases,
    'avg_purchase_value': avg_purchase_values,
    'customer_lifetime_value': customer_lifetime_values,
    'registration_date': registration_dates,
    'last_purchase_date': last_purchase_dates,
    'customer_type': customer_types,
    'preferred_categories': preferred_categories
})

# Save the DataFrame to a CSV file
df.to_csv('large_ecommerce_customer_data.csv', index=False)

print("Large e-commerce customer dataset has been generated and saved as 'large_ecommerce_customer_data.csv'")
