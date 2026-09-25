import pandas as pd
import numpy as np

def clean_raw_dataset(file_path):
    # Load dataset
    df = pd.read_csv(file_path)
    print(f"Original shape: {df.shape}")
    
    # 1. Remove duplicate rows
    df = df.drop_duplicates()
    
    # 2. Handle missing values (e.g., fill numerical nulls with median, categorical with 'Unknown')
    for col in df.select_dtypes(include=[np.number]).columns:
        df[col] = df[col].fillna(df[col].median())
        
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].fillna('Unknown')
        
    # 3. Standardize text data (strip whitespace and convert to title case)
    string_cols = df.select_dtypes(include=['object']).columns
    for col in string_cols:
        df[col] = df[col].str.strip().str.title()
        
    print(f"Cleaned shape: {df.shape}")
    return df

if __name__ == "__main__":
    # Example execution placeholder
    print("Data cleaning pipeline module initialized successfully.")
  
