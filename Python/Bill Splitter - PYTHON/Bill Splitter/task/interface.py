from billsplitter import BillSplitter


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

            self.bill_splitter.display_friends()
        else:
            print("No one is joining for the party")

    def get_bill(self) -> int:
        """Return the bill if it is a proper value or recursively call method until such a value is given."""
        print("Enter the total bill value: ")
        bill = input()
        return float(bill) if self.validate_numeric_input(bill) else self.get_bill()

    def lucky_friend(self) -> bool:
        """Ask the user if they wish to have a lucky friend selected."""
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
        """Ensure that float values are given via the user's input strings where needed."""
        try:
            float(input_str)
            return True
        except ValueError:
            print("Please provide a numeric value")
            return False
