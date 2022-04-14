import pandas as pd 
from sklearn.linear_model import LinearRegression

def calculate_vif(df, features):
    vif, tolerance = {} , {}
    # all the features that you want to examine
    for feature in features:
        # extract all the other features you will regress against
        X = [f for f in features if f!= feature]
        X, y = df[X], df[feature]

        # extract r-squared from the fit
        r2 = LinearRegression().fit(X, y).score(X, y)

        # calculate the tolerence
        tolerance[feature] = 1 - r2

        # calculate the VIF
        vif[feature] = 1/(tolerance[feature])

    # return VIF dataframe
    return pd.DataFrame({'VIF':vif, 'Tolerance': tolerance}) 
