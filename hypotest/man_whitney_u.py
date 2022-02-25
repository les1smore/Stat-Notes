test_team = np.array([6.2, 7.1, 1.5, 2,3 , 2, 1.5, 6.1, 2.4, 2.3, 12.4, 1.8, 5.3, 3.1, 9.4, 2.3, 4.1])
developer_team = ([2.3, 2.1, 1.4, 2.0, 8.7, 2.2, 3.1, 4.2, 3.6, 2.5, 3.1, 6.2, 12.1, 3.9, 2.2, 1.2 ,3.4])

check_normality(test_team)
check_normality(developer_team)
check_variance_homogeneity(test_team, developer_team)

ttest, pvalue = stats.mannwhitneyu(test_team, developer_team, alternative = 'two-sided')
print('p-value:%.4f' % pvalue)
if pvalue < 0.05:
    print('Reject null hypothesis')
else:
    print('Fail to reject null hypothesis')
    
