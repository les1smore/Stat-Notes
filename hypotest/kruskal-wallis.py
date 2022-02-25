# Prepare the data
youtube = np.array([1913, 1879, 1939, 2146, 2040, 2127, 2122, 2156, 2036, 1974, 1956, 2146, 2151, 1943, 2125])
instagram = np.array([2305., 2355., 2203., 2231., 2185., 2420., 2386., 2410., 2340., 2349., 2241., 2396., 2244., 2267., 2281.])
facebook = np.array([2133., 2522., 2124., 2551., 2293., 2367., 2460., 2311., 2178., 2113., 2048., 2443., 2265., 2095., 2528.])

# Assumption check
check_normality(youtube)
check_normality(instagram)
check_normality(facebook)

stat, pvalue_levene = stats.levene(youtube, instagram, facebook)

print("p value:%.4f" % pvalue_levene)
if pvalue_levene < 0.05:
    print('Reject null hypothesis >> The variance of the samples are different.')
else:
    print('Fail to reject null hypothesis >> The variance of the samples are same.')
    
# Select the proper test
F, p_value = stats.kruskal(youtube, instagram, facebook)
print("p value:%.6f" % p_value)
if p_value < 0.05:
    print('Reject null hypothesis')
else:
    print('Fail to reject null hypothesis')
