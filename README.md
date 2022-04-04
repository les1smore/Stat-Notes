# statnotes
Statistical Learning Notes

## Variance
Variance is the spread of values in a dataset around its mean value. It tells you how far each number in the dataset is from its mean. The formula for variance (s²) is defined as follows:

![image](https://user-images.githubusercontent.com/60702562/161456643-a7c6e7b8-a18d-40cd-86ad-be737d2cecf5.png)

**Note**: For sample variance, the denominator is n-1. For population variance, the denominator is n.

A large variance indicates that the numbers in the dataset are far from the mean and far from each other. A small variance, on the other hand, indicates that the numbers are close to the mean and to each other. A variance of 0 indicates that all the numbers in the dataset are the identical. Finally, the valid value of variance is always a positive number (0 or more).

![image](https://user-images.githubusercontent.com/60702562/161456837-52a4af96-fe23-48e6-af40-7e89cb68d11b.png)

As you can see, the values in column a are much more dispersed compared to the rest of the columns, and likewise the values in column b are more dispersed than b and c, and so on. The values in d are the most closely grouped compared to the rest of the columns. As such, you would expect the variance for a would be the largest and the variance for d would be the lowest.


## Covariance
While variance measures the spread of data within its mean value, covariance measures the relationalship between two random variables.

![image](https://user-images.githubusercontent.com/60702562/161573475-57ef443b-b89d-40ed-acc0-537d956f43a4.png)

When two random variables are independent, the covariance will be zero. **However, the reverse is not necessarily true** — a covariance of zero does not mean that 2 random variables are independent (a non-linear relationship can still exist between 2 random variables that has zero covariance). In the above example, you can see that there exists some sort of non-linear v-shape relationship.

While the covariance measures the directional relationship between 2 random variables, it does not show the strength of the relationship between the 2 random variables. Its value is not constrained, and can be from -infinity to +infinity.

## Correlation
A much better way to measure the strength of two random variables is correlation.

The correlation between two random variables measures both the strength and direction of a linear relationship that exists between them. There are two ways to measure correlation:
- **Pearson Correlation Coefficient** — captures the strength and direction of the linear association between two continuous variables
![image](https://user-images.githubusercontent.com/60702562/161575149-3d80c169-33ab-4989-9ced-d4588e62a463.png)

The Pearson Correlation Coefficient is defined to be the covariance of x and y divided by the product of each random variable’s standard deviation.

Like covariance, the sign of the pearson correlation coefficient indicates the direction of the relationship. However, the values of the Pearson correlation coefficient is contrained to be between -1 and 1. Based on the value, you can deduce the following degrees of correlation:
1. Perfect — values near to ±1
2. High degree — values between ±0.5 and ±1
3. Moderate degree — values between ±0.3 and ±0.49
4. Low degree — values below ±0.29
5. No correlation — values close to 0

Understanding the correlations between the various columns in your dataset is an important part of the process of preparing your data for machine learning. You want to train your model using the columns that has the highest correlation with the label of your dataset.
```
df[['math', 'science']].corr(method = 'pearson')
```
- **Spearman’s Rank Correlation Coefficient** — determines the strength and direction of the monotonic relationship which exists between two ordinal (categorical) or continuous variables.

If your data is not linearly distributed, you should use Spearman’s Rank Correlation Coefficient.

In algebra, a montonic function is a function whose gradient never changes sign. In other words, it is a function which is either always increasing or decreasing. The following first two figures are *_monotonic_*, while the third is not (since the gradient changes sign a few times going from left to right).
![image](https://user-images.githubusercontent.com/60702562/161578552-16500a64-aa85-428f-9d2f-afc139fd33b4.png)

The formula for Spearman’s Rank Correlation Coefficient is:
![image](https://user-images.githubusercontent.com/60702562/161579136-67bd4232-480c-4c26-9c8d-a31eac357980.png)

```
df[['math', 'science']].corr(method = 'spearman')
```

***Which method should you use? Pearson or Spearman’s*** 
- Pearson correlation describes linear relationships and spearman correlation describes monotonic relationships
- A scatter plot would be helpful to visualize the data — if the distribution is linear, use Pearson correlation. If it is monotonic, use Spearman correlation.
- You can also apply both the methods and check which is performing well. For instance if results show spearman rank correlation coefficient is greater than Pearson coefficient, it means your data has monotonic relationships and not linear.


## Hypothesis Test
1. **t-test independent:** parametric version of 2 groups paired data


2. **ANOVA:** parametric version of more than 2 groups and unpaired data - To find which group or groups cause the difference, we need to perform a *posthoc test/pairwise comparison* e.g.`Bonferroni adjustment`


3. **Mann Whitney U:** nonparametric version of 2 group comparison for unpaired data


4. **Kruskal-Wallis:** the nonparametric version of ANOVA for unpaired data (the data is collected from different sources)


5. **t-test dependent:** The data is paired since data is collected from the same individuals and assumptions are satisfied


6. **Wilcoxon signed-rank test:** The normality assumption is not satisfied; therefore, we need to use the nonparametric version for 2 groups of paired data


7. **Friedman Chi-Square:** nonparametric version of ANOVA for more than 2 groups paired data

- T-Test: 
    - Compare the Means between two groups
    - Small sample size
- Z-Test:
    - Compare the Means between two groups
    - Large sampl size
- ANOVA:
    - Compare the means between two+ groups
- Chi-Square:
    - Compares proportions between two groups


Reference: https://towardsdatascience.com/hypothesis-testing-with-python-step-by-step-hands-on-tutorial-with-practical-examples-e805975ea96e

*** 

## When to use each measure of Central Tendency
1. *Mean* is the most frequently used measure of central tendency and generally considered the **best** meature of it. However, there are some situations where either median of mode are preferred.
2. *Median* is the preferred measure of central tendency when:
    - There are a few **extreme** scores in the distribution of the data (Remember that a single outlier can have a great effect on the mean).
    - There are some **missing** or **undetermined** values in your data.
    - There is an open ended distribution (e.g.if you have a data field which measures number of children and your options are 0,1,2,3,4,5 or "6 or more", then the "6 or more" is open ended and makes calculating the mean impossible, since we do not know exact values for this field.
    - You have data measured on an **ordinal** scale.
3. *Mode* is preferred measure when data are measured in a **nominal** (and even sometimes ordinal) scale.

Reference: https://courses.lumenlearning.com/introstats1/chapter/when-to-use-each-measure-of-central-tendency/

***

## BG-NBD model
1. CLV (Customer Lifetime Value): the total worth of a customer to a company over the lengh of his relationship. In practice, this "worth" can be defined as revenue, profit, or other metrics of an analyst's chooosing.
    Two reasons for CLV as an important metric:
    - The totality of a company's CLV over its entire customer base gives a rough idea of its market value. Thus, a company with a high total CLV will appear attractive to investors.
    - A CLV analysis can guide the formulation of *customer acquisition* and *retention* strategies. For example, special attention could be given to high-value customers to ensure that they stay loyal to the company.

2. Limitations of CLV: 
   
   - *Only applicable to non-contractual, continuous purchases*
   Depending on the relationship between the sellers and the buyers, a business can either be a contractual business or a non-contractual business.
        - A contractual business: the buyer-seller relationship is governed by contracts. When either party no loger wants to continue this relationship, the contract is terminated. There is no ambiguity as to whether someone is a customer of the business at a given point.
        - A non-contractual business: purchases are made on a per-need basis without any contract
        - In a continuous setting, purchases can occur at any given moment.
        - In a discrete setting, purchases usually occur periodically with some degree of regularity. 
        ![image](https://user-images.githubusercontent.com/60702562/160159329-4f6d35a4-1e77-4533-ba16-3b664ab15adc.png)

   - *Only tackles one component of CLV calculation, which is the prediction of the number of purchases*
     A customer's CLV for a given period can be calculated by multiplying two numbers:
        1. The customer's predicted number of transactions within this period
        2. The predicted value of each purchase
        ![image](https://user-images.githubusercontent.com/60702562/160160527-60caa26b-7851-430b-accb-8805c5a20d4f.png)

Reference: 
1. https://towardsdatascience.com/customer-lifetime-value-estimation-via-probabilistic-modeling-d5111cb52dd
2. https://towardsdatascience.com/modeling-customer-lifetime-value-with-lifetimes-71171a35f654#2b5f-e66d9b5b6df0
       
