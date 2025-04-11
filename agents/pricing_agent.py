# agents/pricing_agent.py

import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

class PricingAgent:
    def __init__(self, pricing_data_path="data/pricing_optimization.csv"):
        self.df = pd.read_csv(pricing_data_path)
        self.model = None

    def preprocess(self):
        df = self.df.copy()
        df.columns = df.columns.str.strip()

        self.features = [
            "Price", "Competitor Prices", "Discounts", "Customer Reviews",
            "Return Rate (%)", "Storage Cost", "Elasticity Index"
        ]
        self.target = "Sales Volume"

        return df[self.features], df[self.target]

    def train(self):
        X, y = self.preprocess()
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, random_state=42, n_jobs=-1)
        self.model.fit(X_train, y_train)

        preds = self.model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, preds))
        print(f"📉 Pricing Model Trained. RMSE on test set: {rmse:.2f}")

    def suggest_optimal_prices(self):
        suggestions = []

        for idx, row in self.df.iterrows():
            if idx % 5 == 0:
                print(f"🔄 Processing {idx + 1}/{len(self.df)} products...")  
            best_price = row['Price']
            best_revenue = row['Price'] * row['Sales Volume']

            for price in np.linspace(0.5 * row['Price'], 1.5 * row['Price'], 10):
                features = pd.DataFrame([{
                    "Price": price,
                    "Competitor Prices": row['Competitor Prices'],
                    "Discounts": row['Discounts'],
                    "Customer Reviews": row['Customer Reviews'],
                    "Return Rate (%)": row['Return Rate (%)'],
                    "Storage Cost": row['Storage Cost'],
                    "Elasticity Index": row['Elasticity Index']
                }])

                predicted_volume = self.model.predict(features)[0]
                revenue = predicted_volume * price

                if revenue > best_revenue:
                    best_price = price
                    best_revenue = revenue

            suggestions.append({
                "Product ID": row['Product ID'],
                "Store ID": row['Store ID'],
                "Current Price": row['Price'],
                "Optimal Price": round(best_price, 2),
                "Expected Revenue": round(best_revenue, 2)
            })

        return pd.DataFrame(suggestions)
