from lifetimes.utils import calibration_and_holdout_data

rfm_cal_holdout = calibration_and_holdout_data(transactions = transactions,
                                               customer_id_col = 'customer_id',
                                               datetime_col = 'date',
                                               monetary_value_col = 'amount',
                                               freq = 'W',
                                               calibration_period_end = '1998-01-01',
                                               observation_period_end = '1998-06-30')
rfm_cal_holdout.head(3)
