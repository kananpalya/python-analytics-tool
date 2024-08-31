import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from datetime import datetime

class AnalyticsTool:
    def __init__(self, data_file):
        self.data_file = data_file
        self.df = pd.read_csv(data_file)

    def clean_data(self):
        # Drop rows with missing values
        self.df.dropna(inplace=True)

        # Convert date columns to datetime objects if they exist
        if 'registration_date' in self.df.columns:
            self.df['registration_date'] = pd.to_datetime(self.df['registration_date'])
        if 'last_purchase_date' in self.df.columns:
            self.df['last_purchase_date'] = pd.to_datetime(self.df['last_purchase_date'])

        # Ensure numerical columns are correct data types
        numeric_columns = self.df.select_dtypes(include=[np.number]).columns
        self.df[numeric_columns] = self.df[numeric_columns].apply(pd.to_numeric, errors='coerce')

    def visualize_data(self):
        # Plot pairplot only for numeric columns
        numeric_df = self.df.select_dtypes(include=[np.number])
        pairplot = sns.pairplot(numeric_df)
        pairplot.savefig("pairplot.png")  # Save pairplot to a file
        plt.show()

        # Plot heatmap only for numeric columns
        plt.figure(figsize=(10, 8))
        heatmap = sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
        plt.savefig("heatmap.png")  # Save heatmap to a file
        plt.show()

    def predictive_modeling(self, target_column):
        # Prepare the data
        X = self.df.drop(columns=[target_column])

        # Convert datetime columns to numerical format (e.g., days since today)
        if 'registration_date' in X.columns:
            X['registration_date'] = (datetime.now() - X['registration_date']).dt.days
        if 'last_purchase_date' in X.columns:
            X['last_purchase_date'] = (datetime.now() - X['last_purchase_date']).dt.days

        # Remove any remaining non-numeric columns
        X = X.select_dtypes(include=[np.number])

        y = self.df[target_column]

        # Encoding categorical features if any (already handled by get_dummies)
        X = pd.get_dummies(X, drop_first=True)

        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train a linear regression model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Make predictions
        y_pred = model.predict(X_test)

        # Evaluate the model
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        return mse, r2
