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


Reference: https://towardsdatascience.com/hypothesis-testing-with-python-step-by-step-hands-on-tutorial-with-practical-examples-e805975ea96e
