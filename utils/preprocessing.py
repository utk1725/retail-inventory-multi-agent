import pandas as pd

def load_demand_data(filepath):
    df = pd.read_csv(filepath)
    
    # ✅ Convert 'Date' to datetime
    df['ds'] = pd.to_datetime(df['Date'])

    # ✅ Rename target variable to 'y' for modeling
    df = df.rename(columns={"Sales Quantity": "y"})

    return df[['Product ID', 'Store ID', 'ds', 'y']]
