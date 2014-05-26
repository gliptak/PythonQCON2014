__author__ = 'andriod'

import pandas as pd

def make_ccy_matrix(market, model):
    """

    :param market: - a market data collection
    :param model: - a model data collection
    :return: a Dataframe with rows of dates and columns of fx rates per ccy
    """
    return pd.DataFrame({ccy:curve.Rate for ccy,curve in [(ccy,market.fx[ccy+'_usd']) for ccy in model.ccyConfig]})