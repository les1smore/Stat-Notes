# Prepare the data
# Import pandas library
import pandas as pd

# Initialize list of lists
data = [['E1',89.8,90.0,91.5],['E2',89.9,90.1,90.7],['E3',88.6,88.8,90.3],
        ['E4',88.7,88.9,90.4],['E5',89.6,89.9,90.2],['E6',89.7,90.0,90.3],
        ['E7',89.2,89.0,90.2],['E8',89.3,89.2,90.3]]

# Create the pandas DataFrame
df = pd.DataFrame(data, columns = ['Experiment','A','B','C'])

# Convert the columns from df to np array
method_A = df[['A']].to_numpy()
method_B = df[['B']].to_numpy()
method_C = df[['C']].to_numpy()

# Assumption check
check_normality(method_A)
check_normality(method_B)
check_normality(method_C)

print("p value:%.4f" % pvalue_levene)
if pvalue_levene < 0.05:
    print('Reject null hypothesis >> The variance of the samples are different.')
else:
    print('Fail to reject null hypothesis >> The variance of the samples are same.')
    
# Select the proper test
test_stat, p_value = stats.friedmanchisquare(method_A, method_B, method_C)
print('p value: %.4f' % p_value)
if p_value < 0.05:
    print('Reject null hypothesis')
else:
    print('Fail to reject null hypothesis')

print(np.round(np.mean(method_A),2), np.round(np.mean(method_B),2), np.round(np.mean(method_C),2))



