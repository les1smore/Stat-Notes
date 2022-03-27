import numpy as np
import scipy.stats as stats
from matplotlib import pyplot as plt

fig, (ax_gamma, ax_beta) = plt.subplots(ncols=1, nrows=2, figsize=(20,16))

x_gamma = np.linspace(0, 10, 1000)
y_gamma = stats.gamma.pdf(x_gamma, a = bgf.params_['alpha'], scale = bgf.params_['r'])
ax_gamma.plot(x_gamma, y_gamma,'-')
ax_gamma.set_title(f'Gamma distribution (alpha = {bgf.params_["alpha"]:.2f}, scale (r)  = {bgf.params_["r"]:.2f})')
ax_gamma.set_xlabel(r'$\lambda$')
ax_gamma.set_ylabel(r'$P(\lambda)$')

x_beta = np.linspace(0, 1, 100)
y_beta = stats.beta.pdf(x_beta, a=bgf.params_["a"], b=bgf.params_["b"])
ax_beta.plot(x_beta, y_beta, "-")
ax_beta.set_title(f'Beta distribution (a = {bgf.params_["a"]:.2f}, b  = {bgf.params_["b"]:.2f})')
ax_beta.set_xlabel('p')
ax_beta.set_ylabel('P(p)')
plt.show()

# Frequency/Recency/Future Purchases Matrix
from lifetimes.plotting import plot_frequency_recency_matrix

_ = plot_frequency_recency_matrix(bgf)

# Frequency/Recency/Probability Alive Matrix
from lifetimes.plotting import plot_probability_alive_matrix

_ = plot_probability_alive_matrix(bgf)

# CLV estimation using BG-NBD
# The predicted number of transactions in the next 10 weeks
rfm_cal_holdout['n_transactions_10_pred'] = bgf.predict(t=10,
                                                        frequency=rfm_cal_holdout['frequency_holdout'],
                                                        recency=rfm_cal_holdout['recency_cal'],
                                                        T=rfm_cal_holdout['T_cal'])

# The probability of being alive
rfm_cal_holdout['alive_prob'] = bgf.conditional_probability_alive(frequency = rfm_cal_holdout['frequency_cal'],
                                                                  recency = rfm_cal_holdout['recency_cal'],
                                                                  T = rfm_cal_holdout['T_cal'])

# Multiply the alive probability and number of purchases and average past purchase
rfm_cal_holdout['value_10_pred'] = rfm_cal_holdout['alive_prob'] * \
                                  rfm_cal_holdout['n_transactions_10_pred'] *\
                                rfm_cal_holdout['monetary_value_cal']

rfm_cal_holdout[["value_10_pred", "alive_prob", "n_transactions_10_pred", "monetary_value_cal"]].head()

rfm_cal_holdout['value_10_pred'].describe()

# Plot a histogram
import seaborn as sns

fig, ax = plt.subplots(figsize=(12, 7))
ax = sns.histplot(rfm_cal_holdout['value_10_pred'],
                  kde=False,
                  binwidth=2)
ax.set_title(f'Customer value histogram')
ax.set_xlabel(r'Customer value estimate for 10 periods ($)')
ax.set_ylabel(r'Number of customers in each bin')
ax.set_xlim(-2,20)

plt.show()

# Proactive intervention
VALUE_10_PRED_THRESHOLD = 10

# Filter for high-value customers
rfm_cal_holdout.loc[rfm_cal_holdout['value_10_pred'] > VALUE_10_PRED_THRESHOLD, ['value_10_pred']]

