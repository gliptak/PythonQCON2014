__author__ = 'andriod'

import pandas as pd

def make_ccy_matrix(market, model):
    """

    :param market: - a market data collection
    :param model: - a model data collection
    :return: a Dataframe with rows of dates and columns of fx rates per ccy
    """
    return pd.DataFrame([curve.Rate for curve in [market.fx[ccy+'_usd'] for ccy in model.ccyConfig]]).T