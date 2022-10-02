class CoinBank:
    def __init__(self, count: int):
        self.count = count


class Converter:
    def __init__(self):
        self.rate = None
        self.type = 'dollars'

    def set_rate(self, rate: float):
        self.rate = rate

    def convert(self, coin: CoinBank) -> int:
        return coin.count * self.rate


class Interface:
    def __init__(self):
        self.converter = Converter()

    def main(self):
        count = int(input("Please, enter the number of conicoins you have: "))
        coin = CoinBank(count)

        rate = float(input("Please, enter the exchange rate: "))
        self.converter.set_rate(rate)

        self.print_coin_info(coin)

    def print_coin_info(self, coin: CoinBank):
        print(f"The total amount of {self.converter.type}s: {self.converter.convert(coin)}")


if __name__ == '__main__':
    coin_interface = Interface()
    coin_interface.main()
