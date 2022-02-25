# Prepare the data
piedpiper=np.array([4.57, 4.55, 5.47, 4.67, 5.41, 5.55, 5.53, 5.63, 3.86, 3.97, 5.44, 3.93, 5.31, 5.17, 4.39, 4.28, 5.25])
endframe = np.array([4.27, 3.93, 4.01, 4.07, 3.87, 4. , 4. , 3.72, 4.16, 4.1 , 3.9 , 3.97, 4.08, 3.96, 3.96, 3.77, 4.09])

# Assumption check
check_normality(piedpiper)
check_normality(endframe)

# Select the proper test
test, pvalue = stats.wilcoxon(endframe, piedpiper) # alternative defalt two sided
print('p-value:%.6f' % pvalue,'>> one_tailed_pval:%.6f'%(pvalue/2))

test,one_sided_pvalue = stats.wilcoxon(endframe, piedpiper, alternative = 'less')
print('one sided pvalue:%.6f' % (one_sided_pvalue))

if pvalue < 0.05:
    print('Reject null hypothesis')
else:
    print('Fail to reject null hypothesis')
    
