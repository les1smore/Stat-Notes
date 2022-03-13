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
