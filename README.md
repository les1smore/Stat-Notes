# statnotes
Statistical Learning Notes

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
       
