# Business Analytics
 Analytics and Visualization Practice
 
 <img src="https://github.com/Kochurovskyi/Business_Analytics/blob/main/Misc/businessman-and-virtual-business-intelligence-icons.jpg" alt="drawing" width="1000"/>


## Introduction
Business Analytics and Business Intelligent are one of the fastest growing sectors in Data Science and this project is my result to dive deeply into the practical problems from the real world using my ML and Visualization skills for a business purposes.   
 
The project contains some [graphics materials]( https://github.com/Kochurovskyi/Business_Analytics/tree/main/Tableau) of data exploratory, descriptive and prescriptive analysis. For an easy access this folder also contains another readme-file with all links to a relevant files of my [Tableau Public Profile]( https://public.tableau.com/profile/yukochu#!/).

Another important part  of the project is [Jupiter (Python) Notebook]( https://github.com/Kochurovskyi/Business_Analytics/blob/main/MarketingCampaign_model.ipynb) with all predictive, prescriptive and clusterization models developed in python with all notes and explanations. 
  
  All conclusions and addition information you will find here in this readme-file.
  Besides the project itself this folder contains all practical exercises made by me taking the Coursera Courses: Data Visualization with Tableau and Advanced Business Analytics Specialization I have successfully finished before start this project. All details related to Coursera Specializations you can find in the end of the file.


## Marketing campaign strategy. Promoting financial products to bank customers

<img src="https://github.com/Kochurovskyi/Business_Analytics/blob/main/Misc/image-asset.jpeg" alt="drawing" width="1000"/>

In previous 4 years, a retail bank sold several products (mortgage account, savings account, and pension account) to its customers. It kept records of all historical data, and this data is available for analysis and reuse. Following a merger in 2021, the bank has new customers and wants to launch some marketing campaigns.

The budget for the campaigns is limited. The bank wants to contact a customer and propose only one product.

The marketing department needs to decide:

Who should be contacted?

Which product should be proposed? (Proposing too many products is counter productive, so only one product per customer contact will be proposed).

How will a customer be contacted? There are different ways, with different costs and efficiency.

How can they optimally use their limited budget?

Will such campaigns be profitable?

## Content
1.	[Data overview](#Data-overview)
2.	[Exploratory Analysis](#Exploratory-Analysis)
3.	[Predictive model](#Predictive-model)
4.	[Proscriptive model](#Proscriptive-model)
5.	[Clusterization model](#Clusterization-model)
6.	[Conclusions](#Conclusions)
6. 	[Coursera details and certificates](#Coursera-details-and-certificates)

## Data overview
All data is stored in the [Datasets folder]( https://github.com/Kochurovskyi/Business_Analytics/tree/main/Datasets) including input datasets and resulting tables
There is two main files for my research and marketing campaign planning:

•	known_behaviors

•	unknown_behaviors



<img src="https://github.com/Kochurovskyi/Business_Analytics/blob/main/Misc/Known.png" alt="drawing" width="1000"/>

The difference is that [known_behaviors]( https://github.com/Kochurovskyi/Business_Analytics/blob/main/Datasets/known_behaviors_1.xlsx) has columns “Mortgage, Pension, Savings”, but [unknown_behaviors]( https://github.com/Kochurovskyi/Business_Analytics/blob/main/Datasets/unknown_behaviors_0.csv) doesn’t have it – we need to predict it.

These file contain data related to each customer of the bunk. It has some personal information like Age, Income, working or non-working information and others and historical data of customer relation with bank like Months contract, Debt to Equity Ratio, Loan Accounts, Number of Purchased Products. It has everything to analyze and predict the customer’s behaviors in the future.

In order to find any data problems preliminary data analysis was carried out. All data was checked for missing cells, gaps in time series, outliers, data format correctness and a couple [Tableau visualizations]( https://github.com/Kochurovskyi/Business_Analytics/blob/main/Tableau/Pet_Prj(1)%20%E2%80%93%20PreExploratory(Hist)%20.twb) were implemented to each data column. 
<img src="https://github.com/Kochurovskyi/Business_Analytics/blob/main/Misc/Pre_view.png" alt="drawing" width="1000"/>

In fact, no critical problems were detected and all data was OK.


## Exploratory Analysis
Exploratory Data Analysis refers to the critical process of performing  investigations on data so as to discover patterns, to test hypothesis and to check assumptions with the help of summary statistics and graphical representations.

The main purpose of this analysis was to find most important patterns which make customers to buy one of the products. I prepared a range of visualizations and in the [Tableau Story]( https://public.tableau.com/profile/yukochu#!/vizhome/Pet_Prj3Story_1pre-model/Exploratorystory) I represented the most important findings.    

<img src="https://github.com/Kochurovskyi/Business_Analytics/blob/main/Misc/exp1.png" alt="drawing" width="1000"/>

You can see that:

•	The greater a customer's income, the more likely it is he or she will buy a savings account.

•	The older a customer is, the more likely it is he or she will buy a pension account.

•	There is a correlation between the number of people in a customer's household, the number of loan accounts held by the customer, and the likelihood a customer buys a mortgage account. To see the correlation, look at the upper right and lower left corners of the mortgage chart.


<img src="https://github.com/Kochurovskyi/Business_Analytics/blob/main/Misc/exp2.png" alt="drawing" width="1000"/>

In conclusion I can say that Age, Income Rate and amount of Loan Accounts are the most important factors for decision making. For example if customer’s Age is more than 55 it’s more likely he will not buy the Savings product, but will consider to buy a pension. And if customer has a lot Loan Accounts he will think about Mortgage product.

## Predictive model

Predictive analytics is the use of data, statistical algorithms and in our case machine learning techniques to identify the likelihood of future outcomes based on historical data. The goal is to go beyond knowing what has happened to providing a best assessment of what will happen in the future.

As a result using one of the most effective XGBoosting algorithm for binary classification I found predicted values of mortgage, savings and pension columns for the file [unknown_behaviors](https://github.com/Kochurovskyi/Business_Analytics/blob/main/Datasets/unknown_behaviors_0.csv) and now I have clear picture who can be interested among the customers to be contacted with offers.

It’s clear that predicted data has the same semantic as the base data, with even more clear frontiers:


•	for savings, there is a clear frontier at $50K revenue.

•	for pension, there is a clear frontier at 55 years old customers.

<img src="https://github.com/Kochurovskyi/Business_Analytics/blob/main/Misc/model1.png " width="1000"/>

The goal was to contact the customers to sell them only one product, so you cannot select all of them. This increases the complexity of the problem: you need to determine the best contact channel, but also need to select which product will be sold to a given customer.
It might be hard to compute this. In order to check, you will use greedy optimization algorithm

## Proscriptive model

## Clusterization model

## Conclusions



## Coursera details and certificates

### Data Visualization with Tableau Specialization

**Course 1. - Fundamentals of Visualization with Tableau**

**Course 2. - Essential Design Principles for Tableau**

**Course 3. - Visual Analytics with Tableau**

**Course 4. - Creating Dashboards and Storytelling with Tableau**

**Course 5. - Data Visualization with Tableau Project**



### Advanced Business Analytics Specialization

**Course 1. - Introduction to Data Analytics for Business**

**Course 2. - Predictive Modeling and Analytics**

**Course 3. - Business Analytics for Decision Making**

**Course 4. - Communicating Business Analytics Results**


<img src="https://github.com/Kochurovskyi/Business_Analytics/blob/main/Coursera/TB_cert.png" alt="drawing" width="1000"/>

