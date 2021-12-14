import random


class BillSplitter:
    def __init__(self):
        self.friends = {}
        self.lucky_friend = None

    def add_friends(self, friend_count: int) -> None:
        if friend_count > 0:
            print("Enter the name of every friend (including you), each on a new line:")
            for _ in range(friend_count):
                name = input()
                self.friends[name] = 0
        else:
            print("No friends to add")

    def display_friends(self) -> None:
        print(self.friends)

    def divide_payment(self, bill: int) -> None:
        if self.lucky_friend:
            avg = round(bill / len(self.friends) - 1, 2)
            for friend in self.friends:
                if friend != self.lucky_friend:
                    self.friends[friend] = avg
        else:
            avg = round(bill / len(self.friends), 2)
            for friend in self.friends:
                self.friends[friend] = avg

    def set_lucky_friend(self):
        self.lucky_friend = random.choice(list(self.friends))


class Interface:
    def __init__(self):
        self.bill_splitter = BillSplitter()

    def main(self):
        print("Enter the number of friends joining (including you):")
        friend_count = int(input())
        if friend_count > 0:
            self.bill_splitter.add_friends(friend_count)
            print()
            bill = self.get_bill()
            print()
            self.lucky_friend()
            print()
            self.bill_splitter.divide_payment(bill)
            # print()
            # self.bill_splitter.display_friends()
        else:
            print("No one is joining for the party")

    def get_bill(self) -> int:
        print("Enter the total bill value: ")
        bill = input()
        return float(bill) if self.validate_numeric_input(bill) else self.get_bill()

    def lucky_friend(self) -> bool:
        print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        choice = input().lower()
        print()
        if choice in 'yes':
            self.bill_splitter.set_lucky_friend()
            print(f"{self.bill_splitter.lucky_friend} is the lucky one!")
            return True
        else:
            print("No one is going to be lucky")
            return False

    @staticmethod
    def validate_numeric_input(input_str: str) -> bool:
        try:
            float(input_str)
            return True
        except ValueError:
            print("Please provide a numeric value")
            return False


if __name__ == '__main__':
    interface = Interface()
    interface.main()
