import pandas as pd
import os
import argparse

def preprocess_data(file_path, pval_threshold=0.05):
    """
    Loads, cleans, and preprocesses the raw methylation data for a machine learning model.

    Args:
        file_path (str): The path to the raw data file (e.g., 'data/raw/GSE140686_GPL13534_matrix_processed.txt').
        pval_threshold (float): The p-value threshold for filtering unreliable probes.

    Returns:
        pd.DataFrame: A preprocessed features matrix with samples as rows and probes as columns.
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

    # Separate methylation values and p-values based on column names
    methylation_df = df.filter(regex='^REFERENCE_SAMPLE')
    pvalue_df = df.filter(regex='^Detection Pval')
    
    # Set the 'ID_REF' column as the index for both dataframes
    if 'ID_REF' in df.columns:
        methylation_df.set_index(df['ID_REF'], inplace=True)
        pvalue_df.set_index(df['ID_REF'], inplace=True)
    else:
        print("Error: 'ID_REF' column not found in the input file.")
        return None

    # Filter out unreliable probes where any p-value is above the threshold
    unreliable_probes = (pvalue_df > pval_threshold).any(axis=1)
    filtered_methylation_df = methylation_df.loc[~unreliable_probes]

    # Transpose the dataframe to have samples as rows and probes as columns
    X = filtered_methylation_df.T

    # Impute any remaining missing values using the median of each probe
    X_imputed = X.fillna(X.median())

    print(f"Data preprocessed successfully. Final features matrix shape: {X_imputed.shape}")
    return X_imputed

if __name__ == '__main__':
    # Hardcoded path as requested by the user.
    file_path = "C:/Users/dell/Downloads/Sarcoma_detection/src/sample.csv"

    # Call the preprocessing function with the hardcoded file path.
    features = preprocess_data(file_path)
    if features is not None:
        print("\nPreprocessing script completed.")
        # Optional: Save the preprocessed data for future use.
        # features.to_csv('data/processed/features.csv')

