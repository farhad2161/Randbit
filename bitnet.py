import requests
import time


class BitNet:
    BASE_URL = "https://blockexplorer.com/api/"
    PROXY = {
        "http": "127.0.0.1:1080",
        "https": "127.0.0.1:1080"
    }

    @staticmethod
    def get_balance(address):
        r = requests.get(
            "https://blockchain.info/q/addressbalance/"+address, proxies=BitNet.PROXY)
        if r.text.isdigit() == False:
            print(r.text)
            time.sleep(1)
            return BitNet.get_balance(address)
        return r.text

    @staticmethod
    def get_balance_btc_com(address):
        r = requests.get("https://chain.api.btc.com/v3/address/"+address)
        return r.json()['data']['balance']

    @staticmethod
    def get_balance_blockcypher_com(address):
        r = requests.get(
            "https://api.blockcypher.com/v1/btc/main/addrs/"+address+"/balance")
        return str(r.json()['balance'])

# a=BitNet.get_balance_btc_com("15urYnyeJe3gwbGJ74wcX89Tz7ZtsFDVew")
# print(a)
