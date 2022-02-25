# Prepare the data
only_breast = np.array([794.1, 716.9, 993. , 724.7, 760.9, 908.2, 659.3 , 690.8, 768.7, 717.3 , 630.7, 729.5, 714.1, 810.3, 583.5, 679.9, 865.1])

only_formula = np.array([ 898.8, 881.2, 940.2, 966.2, 957.5, 1061.7, 1046.2, 980.4, 895.6, 919.7, 1074.1, 952.5, 796.3, 859.6, 871.1 , 1047.5, 919.1 , 1160.5, 996.9])

both = np.array([976.4, 656.4, 861.2, 706.8, 718.5, 717.1, 759.8, 894.6, 867.6, 805.6, 765.4, 800.3, 789.9, 875.3, 740. , 799.4, 790.3, 795.2 , 823.6, 818.7, 926.8, 791.7, 948.3])

# Assumption check
check_normality(only_breast)
check_normality(only_formula)
check_normality(both)

stat, pvalue_levene = stats.levene(only_breast, only_formula, both)
print(" p value:%.4f" % pvalue_levene)
if pvalue_levene < 0.05:
    print('Reject null hypothesis >> The variance of the samples are different.')
else:
    print('Fail to reject null hypothesis >> The variance of the samples are same.')

# Select the proper test
F, p_value = stats.f_oneway(only_breast, only_formula, both)
print("p value:%.6f" % p_value)
if p_value < 0.05:
    print('Reject null hypothesis')
else:
    print('Fail to reject null hypothesis')

# To find which group or groups cause the difference
# pip install scikit-posthocs
# Pairwise T test for multiple comparisons of independent groups. 
# It may be used after a parametric ANOVA to do pairwise comparisons.
import scikit_posthocs as sp
posthoc_df = sp.posthoc_ttest([only_breast, only_formula, both], equal_var = True, p_adjust = 'bonferroni')

group_names = ['only breast', 'only formula','both']
posthoc_df.columns = group_names
posthoc_df.index = group_names
posthoc_df.style.applymap(lambda x: 'background-color:violet' if x<0.05 else 'background-color:white')
