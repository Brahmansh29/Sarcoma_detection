Sarcoma Classification by DNA Methylation
Overview
This project aims to classify sarcoma subtypes using DNA methylation data from the Gene Expression Omnibus (GEO) dataset GSE140686. Sarcoma, a type of cancer that develops in bone and soft tissue, can be challenging to classify. By leveraging machine learning models on epigenetic data (DNA methylation), this project seeks to develop an effective classification system.

The core of this project involves a data-driven approach:

Data Preprocessing: Cleaning and preparing the raw methylation data.

Model Training: Developing a machine learning model to classify sarcoma subtypes.

Evaluation: Assessing the model's performance.

For a comprehensive and interactive overview of the project's current status, including model performance metrics and a detailed analysis of the results, please view the live report:
View the Interactive Report

Project Structure
The repository is organized to follow a standard data science project workflow, making it easy to navigate and reproduce the results.

/sarcoma-classification
|-- data/
|   |-- processed/      # Preprocessed data files (e.g., features.csv)
|   |-- raw/            # Raw data and labels from the GEO dataset
|-- src/
|   |-- data_preprocessing.py   # Script for data cleaning and preparation
|   |-- train_model.py          # Script for training and evaluating the model
|-- .gitignore                  # Files and directories to ignore in Git
|-- index.html                  # The interactive project report
|-- requirements.txt            # Python dependencies
|-- README.md                   # Project overview and documentation


Model Performance
The initial model was a Random Forest Classifier trained on a dummy dataset to test the workflow. As expected, the accuracy is low, which highlights the importance of using the real labels from the dataset's metadata.

Model Metrics
Model Accuracy: 0.3279

Classification Report
              precision    recall  f1-score   support

      Type_0       0.00      0.00      0.00        41
      Type_1       0.00      0.00      0.00        41
      Type_2       0.33      1.00      0.49        40

    accuracy                           0.33       122
   macro avg       0.11      0.33      0.16       122
weighted avg       0.11      0.33      0.16       122


Analysis of Results
The classification report shows that the model's performance is currently poor, with a macro average F1-score of 0.16. This is because the model was trained on placeholder data where samples were randomly assigned to Type_0, Type_1, and Type_2.

Notice that the model's performance is concentrated on Type_2, which it always predicts. This is a clear indication that it is unable to learn any meaningful patterns from the dummy labels. The next step is to replace these placeholders with the actual sarcoma subtypes from the dataset's clinical metadata.