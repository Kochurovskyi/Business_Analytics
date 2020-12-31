import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics


# df.ExpirationMonth = df.ExpirationMonth.replace('-','999')
# df.ExpirationMonth = df.ExpirationMonth.astype(np.float16)
# df = df[(df.Reward!=0.0) & (df.NumStores!=0) & (df.ExpirationMonth!=999)]
# lst = ['Salerank',
#        'X2013USSales',
#        'X2013WorldSales',
#        #'NumStores',
#        'RewardSize',
#        'ProfitMargin']
# for i in lst:
#     X = np.array(df[['NumStores', i]]).astype(np.float16)
#     #X = np.log(np.array(df[i]).astype(np.float16))
#     y = np.array(df.ExpirationMonth).astype(np.float16)
#     #y = np.log(np.array(df.ExpirationMonth).astype(np.float16))
#     #slope, intercept, r_value, p_value, std_err = stats.linregress(X, y)
#     #print(i, round(r_value**2,4))
#     X1 = sm.add_constant(X)
#     result = sm.OLS(y, X1).fit()
#     # print dir(result)
#     print(i, result.rsquared)
#
#     #plt.scatter(X, y, edgecolors='red')
#     #plt.plot(X, intercept + slope * X, )
#     #plt.show()
#     #print(stats.linregress(X, y))


# df = pd.read_csv('appointments.csv')
# X = np.array(df.Lag)
# y = np.where(df.Status=='Arrived', 0, 1)

df = pd.read_csv('crp.csv')
y = df.Reward
print(y.shape)
X = np.array(pd.get_dummies(df.IndustryType)[['Discount', 'Grocery']])
# X_train = X
# y_train = y

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                      test_size=0.40,
                                                      random_state=12345)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
THRESHOLD = 0.5
y_pred = np.where(logreg.predict_proba(X_train)[:,1] > THRESHOLD, 1, 0)
# y_pred = logreg.predict(X_train)
print('Accuracy: {:.2f}'.format(logreg.score(X_train, y_train)))
print(confusion_matrix(y_train, y_pred))
tn, fp, fn, tp = confusion_matrix(y_train, y_pred).ravel()
print('tn, fp, fn, tp', tn, fp, fn, tp)
print('inercept:', logreg.intercept_)
print('coef:', logreg.coef_)