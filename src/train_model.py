import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import os
from data_preprocessing import preprocess_data

def train_and_evaluate_model(features_path, labels_path):
    """
    Trains and evaluates a machine learning model using preprocessed features and labels.

    Args:
        features_path (str): The path to the preprocessed features file (e.g., 'data/processed/features.csv').
        labels_path (str): The path to the file containing sample labels (e.g., 'data/raw/labels.csv').
    """
    # Load features from the preprocessed data file
    try:
        X = pd.read_csv(features_path, index_col=0)
    except FileNotFoundError:
        print(f"Error: The features file '{features_path}' was not found.")
        print("Please run `data_preprocessing.py` first to generate this file.")
        return

    # Load labels from the raw data file
    try:
        labels_df = pd.read_csv(labels_path)
    except FileNotFoundError:
        print(f"Error: The labels file '{labels_path}' was not found.")
        print("Please place the real labels file in the 'data/raw' directory.")
        return
    
    # Set the 'SampleID' column as the index for the labels dataframe
    if 'SampleID' in labels_df.columns:
        labels_df.set_index('SampleID', inplace=True)
    else:
        print("Error: 'SampleID' column not found in the labels file.")
        return
    
    # Align the features and labels
    # This is a crucial step to ensure each sample's features are matched with its label
    y = labels_df.loc[X.index, 'SarcomaType']
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
    
    print(f"Training set size: {len(X_train)} samples")
    print(f"Testing set size: {len(X_test)} samples")
    print("-" * 40)
    
    # Initialize and train the Random Forest Classifier
    print("Training Random Forest Classifier...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Make predictions and evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print("Model training complete.")
    print(f"Model Accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

if __name__ == '__main__':
    # Conceptual usage:
    # 1. First, you would run data_preprocessing.py to generate features.csv.
    #    features = preprocess_data('data/raw/GSE140686_GPL13534_matrix_processed.txt.gz')
    #    features.to_csv('data/processed/features.csv')
    
    # 2. Then, you would run this script.
    
    # Here, we'll simulate the features file being present and use a dummy labels file
    # for the demonstration, since the real labels file is not yet available.
    
    # Dummy data for demonstration purposes only.
    if not os.path.exists('data/processed/features.csv'):
        # This part simulates running the preprocessing script first.
        # In a real scenario, you'd run `data_preprocessing.py` and save the output.
        print("Creating dummy features and labels for demonstration...")
        dummy_data = pd.DataFrame({f'probe_{i}': [0.5] * 485 for i in range(1000)})
        dummy_data.index = [f'REFERENCE_SAMPLE_{i}' for i in range(485)]
        dummy_data.to_csv('data/processed/features.csv')
        
        dummy_labels = pd.DataFrame({'SampleID': dummy_data.index, 'SarcomaType': [f'Type_{i % 3}' for i in range(485)]})
        dummy_labels.to_csv('data/raw/labels.csv', index=False)
        print("Dummy features and labels created.")

    train_and_evaluate_model('data/processed/features.csv', 'data/raw/labels.csv')

