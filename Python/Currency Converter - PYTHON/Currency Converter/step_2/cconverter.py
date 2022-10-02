class CoinBank:
    def __init__(self, count: int, coin_type: str):
        self.count = count
        self.coin_type = coin_type


class Converter:
    def __init__(self):
        self.type = 'dollars'

    @staticmethod
    def convert_to_usd(coin: CoinBank) -> int:
        return coin.count * 100


class Interface:
    def __init__(self):
        self.converter = Converter()

    def main(self):
        count = int(input())
        coin = CoinBank(count, 'conicoin')
        self.print_coin_info(coin)

    def print_coin_info(self, coin: CoinBank):
        print(f"I have {coin.count} {coin.coin_type}s.")
        print(f"{coin.count} {coin.coin_type}s cost {self.converter.convert_to_usd(coin)} {self.converter.type}.")
        print("I am rich! Yippee!")


if __name__ == '__main__':
    coin_interface = Interface()
    coin_interface.main()
