# Scopping

## Problems

Credit Card Fraud Detection
https://www.kaggle.com/mlg-ulb/creditcardfraud:
problem: recognize fraudulent credit card transactions
 * classification

New York City Taxi Fare Prediction
https://www.kaggle.com/c/new-york-city-taxi-fare-prediction/:
problem: predicting the fare amount (inclusive of tolls) for a taxi ride in New York City given the pickup and dropoff locations.
 * time series regression

Santander Customer Transaction Prediction
https://www.kaggle.com/c/santander-customer-transaction-prediction:
problem: customers will make a specific transaction in the future
 * classification binary

I chose the **Santander Customer Transaction Prediction** challenge, because is a binary classification problem, I found the data a little different from what I usually work with, and as the main objective of this test is not related to model modeling, I will use this challenge to learn project structuring.

## Database

The problem´s question is: "Can you identify who will make a transaction?". The contextualization of the problem informs that the objective is to identify which customers will make a transaction.
This is a sentiment analysis problem. The provided data has a label, identified by the target column, which has a binary value (0 or 1) and must be the column used for inference.

Input data:
 * 200 raw features without description

Output data:
 * binary target column, 0 or 1.

## Solution

Having a model will analyze customer sentiments and tell you which customers will transact in the future.

## How?

Since we are dealing with a binary classification, I will implement a decision tree with the LightGBM library, as an initial model to analyze the data.

The end result will be a survey if a customer will make transactions in the future

# Metrics 

Metric: How many customers got the test data right.

## Milestone

* EDA
* Modelo
* Análise dos resultos
* Mlflow
* Docker
* TC
* CI/CD
* Workflow
