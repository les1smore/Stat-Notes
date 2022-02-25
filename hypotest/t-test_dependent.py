# Prepare the data
test_results_before_diet=np.array([224, 235, 223, 253, 253, 224, 244, 225, 259, 220, 242, 240, 239, 229, 276, 254, 237, 227])
test_results_after_diet = np.array([198, 195, 213, 190, 246, 206, 225, 199, 214, 210, 188, 205, 200, 220, 190, 199, 191, 218])

# Assumption check
check_normality(test_results_before_diet)
check_normality(test_results_after_diet)

# Select the proper test
test_stat, p_value_paired = stats.ttest_rel(test_results_before_diet, test_results_after_diet)
print("p value:%.6f" % p_value_paired, "one tailed p value:%.6f" %(p_value_paired/2))

if p_value_paired < 0.05:
    print('Reject null hypothesis')
else:
    print('Fall to reject null hypothesis')

