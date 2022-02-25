def check_normality(data):
    test_stat_normality, p_value_normality = stats.shapiro(data)
    print("p value:%.4f" % p_value_normality)
    if p_value_normality < 0.05:
        print("Reject null hypothesis >> The data is not normally distributed")
    else:
        print('Fail to reject null hypothesis >> The data is normally distributed')
