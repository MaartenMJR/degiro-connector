import json
import logging

from degiro_connector.trading.api import API as TradingAPI
from degiro_connector.trading.models.credentials import Credentials

logging.basicConfig(level=logging.DEBUG)

with open("config/config.json") as config_file:
    config_dict = json.load(config_file)

credentials = Credentials.model_validate(obj=config_dict)
trading_api = TradingAPI(credentials=credentials)
trading_api.connect()

# FETCH DATA
product_isin = "FR0000131906"
financial_statements = trading_api.get_financial_statements(
    product_isin=product_isin,
    raw=False,
)

# DISPLAY DATA
print(financial_statements)
