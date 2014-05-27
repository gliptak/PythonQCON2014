from data_access import get_file
from transform import make_ccy_matrix

__author__ = 'maku-8qlabs'

market = get_file('market1')
model = get_file('model')

ccy_matrix=make_ccy_matrix(market, model)
