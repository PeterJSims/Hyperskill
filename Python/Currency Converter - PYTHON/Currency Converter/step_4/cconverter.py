class CoinBank:
    def __init__(self, count: float):
        self.count = count


class Converter:
    RATES = {'RUB': 2.98, 'ARS': 0.82, 'HNL': 0.17, 'AUD': 1.9622, 'MAD': 0.208}

    def __init__(self):
        self.rate = None
        self.type = 'dollars'

    def set_rate(self, rate: float):
        self.rate = rate

    def convert(self, coin: CoinBank) -> dict:
        return {k: round(v * coin.count, 2) for k, v in self.RATES.items()}


class Interface:
    def __init__(self):
        self.converter = Converter()

    def main(self):
        count = float(input())
        coin = CoinBank(count)
        self.print_coin_info(coin)

    def print_coin_info(self, coin: CoinBank):
        conversion_dict = self.converter.convert(coin)
        for k, v in conversion_dict.items():
            print(f"I will get {v} {k} from the sale of {coin.count} conicoins.")


if __name__ == '__main__':
    coin_interface = Interface()
    coin_interface.main()
