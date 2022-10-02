import requests


class Converter:

    def get_rates(self, currency_type: str) -> tuple:
        r = requests.get(f"http://www.floatrates.com/daily/{currency_type}.json").json()
        return r['usd'], r['eur']


class Interface:
    def __init__(self):
        self.converter = Converter()

    def main(self):
        currency_type = input()
        self.print_currency_info(currency_type)

    def print_currency_info(self, currency_type: str) -> None:
        info = self.converter.get_rates(currency_type)
        for item in info:
            print(item)


if __name__ == '__main__':
    coin_interface = Interface()
    coin_interface.main()
