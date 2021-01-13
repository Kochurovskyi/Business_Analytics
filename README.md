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

Detailed visualistion you can find in [Tableau file](https://github.com/Kochurovskyi/Business_Analytics/blob/main/Tableau/Pet_Prj(3)%20%E2%80%93%20Storry_1(pre-model)%20.twb)


## Predictive model

Predictive analytics is the use of data, statistical algorithms and in our case machine learning techniques to identify the likelihood of future outcomes based on historical data. The goal is to go beyond knowing what has happened to providing a best assessment of what will happen in the future.

As a result using one of the most effective XGBoosting algorithm for binary classification I found predicted values of mortgage, savings and pension columns for the file [unknown_behaviors](https://github.com/Kochurovskyi/Business_Analytics/blob/main/Datasets/unknown_behaviors_0.csv) and now I have clear picture who can be interested among the customers to be contacted with offers.

It’s clear that predicted data has the same semantic as the base data, with even more clear frontiers:


•	for savings, there is a clear frontier at $50K revenue.

•	for pension, there is a clear frontier at 55 years old customers.

<img src="https://github.com/Kochurovskyi/Business_Analytics/blob/main/Misc/model1.png " width="1000"/>

Detailed visualistion you can find in [Tableau file](https://public.tableau.com/profile/yukochu#!/vizhome/Pet_Prj4Storry_2modeling/Modeling)

The goal was to contact the customers to sell them only one product, so you cannot select all of them. This increases the complexity of the problem: you need to determine the best contact channel, but also need to select which product will be sold to a given customer.
It might be hard to compute this. In order to check, you will use greedy optimization algorithm

## Proscriptive model

Now I have a prediction of who will buy what in the list of new customers. However, I do not have the budget to contact all of them and I have various contact channels with different costs and effectiveness. Furthermore, if I contact a customer I want to propose only one product per customer.

I used a custom algorithm that ensures 30% of offers are made per channel by choosing the most promising per channel. The algorithm then continues to add offers until the budget is reached.

Base on predicted date I’m going to implement Greedy algorithm, which allows me to distribute marketing channels (Gifts, Newsletter, Seminar) equally and most effective within the budget limit and taking in account that:

Each product gives revenue:

•	Mortgage - 200

•	Pension - 300

•	Savings - 400

Each channel (marketing action) costs with following success factor:

•	gift - 20 / 0.20

•	newslette - 15, / 0.05

•	seminar - 23.0 / 0.30


For a greedy algorithm I will use most effective marketing channels firstly and move forward to less effective in ours case I will all all Seminars with the highest success factor and implement it to Savings product with the highest revenue (400) and finish with gifts implemented to Mortgage. Then I will iterate till the budget’s finished. This is how it works.

And in the end I will have such results for different limits of budget like in the example bellow (for $20000):

•	Budget limit: 20000

•	Total offers:546

•	Number of Mortgage offers:273, Number of Pension offers:273, Number of Savings offers:367

•	Campaign cost: 18031.0


•	Revenue: 63220.0


## Clusterization model

Clusterization is an unsupervised clustering / topic extraction. We have no previous knowledge on the number of topics there are in every corpus of documents.

A conventional approach involves an -optional- initial step of LSA (Latent Semantic Analysis) (TruncatedSVD) for dimensionalty reduction followed by K-Means. The downside to this approach in this scenario is that it requires a predefined number of clusters, which is not available

If a good candidate for k is found K-Means can be re-run using it as input. In addition, several K-Means runs are advised since the algorithm might end up in a local optima.

SVD/LSA TruncatedSVD implements a variant of singular value decomposition (SVD) that only computes the k largest singular values, where k is a user-specified parameter.

When truncated SVD is applied to term-document matrices (as returned by CountVectorizer or TfidfVectorizer), this transformation is known as latent semantic analysis (LSA), because it transforms such matrices to a “semantic” space of low dimensionality.

In particular, LSA is known to combat the effects of synonymy and polysemy (both of which roughly mean there are multiple meanings per word), which cause term-document matrices to be overly sparse and exhibit poor similarity under measures such as cosine similarity.


After a couple of experiments I decided to take 4 clusters as the most optimal.

And now my marketing department can split all offers according to the clusters, here is some distributions of most critical customer characteristics like Age or Income taking to account the clusters.  

<img src="https://github.com/Kochurovskyi/Business_Analytics/blob/main/Misc/model2.png" width="1000"/>

## Conclusions

In general all project goals were reached:


1. I analyzed the data and prepared it for modeling

2. Preliminary some research was carried out to find patterns and relations between the customer’s characteristics 

3. Predicted model provided me a list of customers who could be interested in a new offer and what kind of offer it should be

4.  Prescriptive model gave some direction and advises in which way I should contact assigned customer and which offer should be proposed.  

5. As a result of prescriptive analysis I have a various range of budget limits what will allow to be flexible in decision making.

6. And finally Clusterization. All my customers which likely to be interested in the new offers are separated into 4 clusters what allows to marketing department to work more effective.



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

