import requests


class Converter:

    def get_rates(self, currency_type: str) -> tuple:
        r = requests.get(f"http://www.floatrates.com/daily/{currency_type}.json").json()
        return r


class Interface:
    def __init__(self):
        self.converter = Converter()
        self.rate_json = None
        self.currency_cache = {}

    def main(self):
        currency_type = input().lower()
        self.rate_json = self.converter.get_rates(currency_type)
        if currency_type != 'usd':
            self.currency_cache['usd'] = float(self.rate_json['usd']['rate'])
        if currency_type != 'eur':
            self.currency_cache['eur'] = float(self.rate_json['eur']['rate'])

        self.currency_loop()

    def currency_loop(self):
        received_code = input().lower()
        if received_code == '':
            return False
        else:
            amount = int(input())
            print('Checking the cache...')
            received_rate = float(self.rate_json[received_code]['rate'])
            if received_code in self.currency_cache.keys():
                print('Oh! It is in the cache!')
            else:
                print('Sorry, but it is not in the cache!')
                self.currency_cache[received_code] = received_rate
            result = round(amount * received_rate, 2)
            print(f'You received {result} {received_code.upper()}.')
            self.currency_loop()


if __name__ == '__main__':
    coin_interface = Interface()
    coin_interface.main()
