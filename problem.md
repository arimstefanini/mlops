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

 Eu escolhi o desafio Santander Customer Transaction Prediction. Alem de ser uma problema simples de classificação binaria, achei os dados um poucos diferente do que eu geralemnte trabalho, e como o objetivo principal deste teste não está relacionado com a modelagem do modelo, vou usar esse desafio para aprender. 

## Database

o objetivo é classificar os clientes

Variáveis de Input:
 * 200 raw features without description

Variáveis de Output:
 * binary target column, 0 or 1.

## Solução

Ter um modelo de dirá quais clientes que iram transacionar no futuro.

## Como?

Já que tratamos de uma classificação binaria, vou implementar uma árvore de decisão com a biblioteca XGBoost.
Realizar uma análise exploratória dos dados para verificar se há alguma anomalia nos dados.
E construir algumas features aplicando alguma tecnica que faz sentido para o modelo.

O resultado final será pesquisa se sobre um cliente falando se ele será um cliente que fará transaçoes no futuro

# Metrica 

Métrica primaria: Quantos clientes acertou nos dados de teste.

## Milestone

* EDA
* Modelo
* Análise dos resultos
* Mlflow
* Docker
* TC
* CI/CD
* Workflow
