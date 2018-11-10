import requests
import time


class BitNet:
    BASE_URL = "https://blockexplorer.com/api/"
    proxy = dict()

    def __init__(self, http_proxu_url, http_proxy_port):
        if http_proxu_url:
            self.proxy = dict(http=http_proxu_url+":"+http_proxy_port,
                              https=http_proxu_url+":"+http_proxy_port)

    def get_balance_blockchain_info(self, address):
        try:
            r = requests.get(
                "https://blockchain.info/q/addressbalance/"+address, proxies=self.proxy)
            if r.text.isdigit() == False:
                print(r.text)
                time.sleep(1)
                return self.get_balance_blockchain_info(address)
            return r.text
        except:
            time.sleep(60)
            return self.get_balance_blockchain_info(address)

    def get_balance_bitaps_com(self, address):
        r = requests.get("https://bitaps.com/api/address/" +
                         address, proxies=self.proxy)
        return str(r.json()['balance'])

    def get_balance_blockexplorer_com(self, address):
        r = requests.get(
            "https://blockexplorer.com/api/addr/{}/balance".format(address), proxies=self.proxy)
        if r.text.isdigit() == False:
            print(r.text)
            time.sleep(1)
            return self.get_balance_blockexplorer_com(address)
        return r.text

    def get_balance_btc_com(self, address):
        r = requests.get(
            "https://chain.api.btc.com/v3/address/"+address, proxies=self.proxy)
        return r.json()['data']['balance']

    def get_balance_blockcypher_com(self, address):
        r = requests.get(
            "https://api.blockcypher.com/v1/btc/main/addrs/"+address+"/balance", proxies=self.proxy)
        return str(r.json()['balance'])
