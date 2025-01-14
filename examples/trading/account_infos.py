import json
import logging

from degiro_connector.trading.api import API as TradingAPI
from degiro_connector.trading.models.credentials import Credentials

logging.basicConfig(level=logging.DEBUG)

with open("config/config.json") as config_file:
    config_dict = json.load(config_file)

credentials = Credentials.model_validate(obj=config_dict)

# SETUP TRADING API
trading_api = TradingAPI(credentials=credentials)

# CONNECT
trading_api.connect()

# FETCH DATA
account_info_table = trading_api.get_account_info()

# DISPLAY DATA
account_info_pretty = json.dumps(account_info_table, sort_keys=True, indent=4)
print(account_info_pretty)
