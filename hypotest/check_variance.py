# Levene's test 
def check_variance_homogeneity(group1, group2):
    test_stat_var, p_value_var = stats.levene(group1, group2)
    print("p value:%.4f" % p_value_var)
    if p_value_var < 0.05:
        print('Reject null hypothesis >> The variance of the samples are different.')
    else:
        print('Fail to reject null hypothesis >> The variance of the samples are same.')
