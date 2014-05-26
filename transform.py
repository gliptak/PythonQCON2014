__author__ = 'andriod'

import pandas as pd

def make_ccy_matrix(market, model):
    return pd.DataFrame([curve.Rate for curve in [market.fx[ccy+'_usd'] for ccy in model.ccyConfig]]).T