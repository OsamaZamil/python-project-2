#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

class DataPreprocessor:
    def __init__(self, data=None):
        self.data = data
    
    def load_data(self):
        file_path = input("Enter the path to the data file: ")
        file_format = file_path.split(".")[-1]  # Extract file format from the file path

        if file_format == 'csv':
            self.data = pd.read_csv(file_path)
        elif file_format == 'xlsx':
            self.data = pd.read_excel(file_path)
        elif file_format == 'json':
            self.data = pd.read_json(file_path)
        else:
            raise ValueError("Unsupported file format. Please provide a CSV, Excel, or JSON file.")

    def summary_statistics(self):
        return self.data.describe()
    
    def data_type_distribution(self):
        return self.data.dtypes.value_counts()
    
    def unique_value_counts(self):
        return {col: self.data[col].nunique() for col in self.data.columns}
    
    def handle_missing_values(self, method='imputation'):
        if method == 'imputation':
            return self.data.fillna(self.data.mean())  # Example: Impute with mean
        elif method == 'removal':
            return self.data.dropna()
        elif method == 'flagging':
            return self.data.fillna('missing', inplace=True)
        else:
            raise ValueError("Unsupported missing value handling method. Please choose from 'imputation', 'removal', or 'flagging'.")
    
    def encode_categorical_variables(self, method='one-hot'):
        if method == 'one-hot':
            return pd.get_dummies(self.data, columns=self.data.select_dtypes(include='object').columns)
        elif method == 'label':
            # Implement label encoding
            pass
        elif method == 'target':
            # Implement target encoding
            pass
        else:
            raise ValueError("Unsupported categorical variable encoding method. Please choose from 'one-hot', 'label', or 'target'.")
    
    def save_processed_data(self, file_path):
        self.data.to_csv(file_path, index=False)

# Create an instance of DataPreprocessor
preprocessor = DataPreprocessor()

# Load the dataset
preprocessor.load_data()

# Display summary statistics
summary_stats = preprocessor.summary_statistics()
print("Summary Statistics:")
print(summary_stats)
print()

# Display data type distribution
data_type_dist = preprocessor.data_type_distribution()
print("Data Type Distribution:")
print(data_type_dist)
print()

# Display unique value counts
unique_counts = preprocessor.unique_value_counts()
print("Unique Value Counts:")
for col, count in unique_counts.items():
    print(f"{col}: {count}")
print()

# Handle missing values by imputation
clean_data = preprocessor.handle_missing_values(method='imputation')
print("Cleaned Data after Imputation:")
print(clean_data.head())
print()

# Encode categorical variables using one-hot encoding
encoded_data = preprocessor.encode_categorical_variables(method='one-hot')
print("Encoded Data after One-Hot Encoding:")
print(encoded_data.head())
print()

# Save the processed data
processed_file_path = input("Enter the path to save the processed data (include file name with extension): ")
preprocessor.save_processed_data(processed_file_path)
print("Processed data saved successfully.")


# In[ ]:





# In[ ]:




