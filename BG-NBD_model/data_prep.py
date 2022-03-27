pip install lifetimes

import pandas as pd
from lifetimes.datasets import load_dataset

transactions = load_dataset(
    filename = 'CDNOW_sample.txt',
    header = None,
    delim_whitespace = True,
    names = ['customer_id', 'customer_index','date','quantity','amount'],
    converters = {'date':lambda x: pd.to_datetime(x, format='%Y%m%d')}
)

transactions.head(3)

# lifetimes provides a utility function that facilitates the conversion from the 'transactions' format to the RFM format
from lifetimes.utils import summary_data_from_transaction_data

rfm = summary_data_from_transaction_data(transactions=transactions,
                                         customer_id_col = 'customer_id',
                                         datetime_col = 'date',
                                         monetary_value_col = 'amount',
                                         observation_period_end = pd.to_datetime('1998-06-30'),
                                         freq = 'W')
rfm.head(3)
