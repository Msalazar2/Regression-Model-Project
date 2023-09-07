# Regression-Model-Project

This project uses the zillow dataset on MySql through Codeup's servers and produces a regression model to predict tax value.

## Goal

* The purpose of this model is to predict tax values of single family properties using features of the zillow dataset from 2017.
* My goal is to find specific features that are correlated with the tax value and build a model with lowest RMSE to predict property tax values on new data.

## Initial hypotheses

* Null Hypothesis: 
* Alternative Hypothesis: 

## Data dictionary

| Feature     | Description     |
| ----------- | ----------------|
| bedrooms    | total bedrooms  |
| bathrooms   | total bathrooms |
| square_ft   | square footage  |
| tax_value   | tax value       |
| year        | year built      |
| county      | location        |


## Planning:
Questions to ask about the data set based off of what I want my model to predict: 
- Do any features have a correlation with tax value?. 
- What features significantly affect tax value?

- Final report should be in .ipynb, Modules should be in .py, Predictions should be in .csv.
- Audience will be lead data scientist.
- Determine correlation between features and tax value.
- Develop my null hypothsisis and alternative hypothesis.
- Explore data using visuals and statistical tests.
- Determine what model to create.
  
## Acquisition:
- Using a function with my credentials stored in a env.py file, I connected to codeup's MySQL server.
- I created a query pertinent to the project.
- Using a function I bult containing the query and pandas.read_sql, I called the function to acquire and read zillow data from MySQL.

## Preparation:
- Perform tasks such as handling null values, renaming columns, normalizing text, binning of data, changing data types, mapping column values.
- Open wrangle.py file and look under clean_zillow() function for more details.

## Exploration & pre-processing:
- Made visuals and used stats to understand which features had a significant correalation, relationship
- I dropped features that had no significance
- Open explore.py and preprocess.py file for more details.

## Modeling:
- I choose a classification random forest model
- I used my train data set to train my model
- I made predictions with my model
- I made multple models and choose the best one

## Delivery:
- Deployed my model and a reproducable report
- Made recommendations

## Key findings, recommendations, and takeaways
- Monthly contracts amd charges are key features driving customer churn
- I recommend incentivizing yearly contracts by offering promotion deals and a loyalty program

## Instructions or an explanation of how someone else can reproduce project and findings

Enviroment setup: 
- Install Conda, Python, MySql, VS Code or Jupyter Notebook
- Clone this repo to your local 
