# agents/store_agent.py

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_squared_error
import joblib

class StoreAgent:
    def __init__(self):
        self.model = None
        self.encoder = None
        self.columns_to_encode = ['Store ID', 'Product ID', 'Promotions', 'Seasonality Factors', 'External Factors', 'Customer Segments', 'Demand Trend']


    def preprocess(self, df):
        df = df.copy()
        df.columns = df.columns.str.strip()  # ✅ Fix: Strip whitespace from column names

        df['Date'] = pd.to_datetime(df['Date'])
        df['day'] = df['Date'].dt.day
        df['month'] = df['Date'].dt.month
        df['weekday'] = df['Date'].dt.weekday

        # Fill missing values
        df.fillna('Unknown', inplace=True)

        # One-hot encode categorical columns
        self.encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
        encoded = self.encoder.fit_transform(df[self.columns_to_encode])
        encoded_df = pd.DataFrame(encoded, columns=self.encoder.get_feature_names_out(self.columns_to_encode))

        df = pd.concat([df, encoded_df], axis=1)
        df.drop(columns=self.columns_to_encode + ['Date'], inplace=True)

        return df

    def train(self, df):
        print("🧪 Training global demand prediction model...")

        df = self.preprocess(df)
        X = df.drop(columns=['Sales Quantity'])
        y = df['Sales Quantity']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.model = RandomForestRegressor(n_estimators=10, max_depth=10, random_state=42, n_jobs=-1)
        self.model.fit(X_train, y_train)

        predictions = self.model.predict(X_test)
        rmse = mean_squared_error(y_test, predictions, squared=False)
        print(f"📉 Model trained. RMSE on test set: {rmse:.2f}")

        joblib.dump(self.model, 'models/global_model.pkl')
        joblib.dump(self.encoder, 'models/encoder.pkl')

    def predict(self, df):
        if self.model is None or self.encoder is None:
            self.model = joblib.load('models/global_model.pkl')
            self.encoder = joblib.load('models/encoder.pkl')

        df = df.copy()
        if 'Sales Quantity' in df.columns:
            df = df.drop(columns=['Sales Quantity'])

        df = self.preprocess(df)
        return self.model.predict(df)

