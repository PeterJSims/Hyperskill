import math


class Loan:
    def __init__(self, principal: int):
        self.principal = principal


class LoanCalculator:

    @staticmethod
    def calculate_monthly_payments(principal: int, months: int) -> (int, int):
        payment = math.ceil(principal / months)
        last_payment = principal - (months - 1) * payment
        return payment, last_payment

    @staticmethod
    def calculate_number_of_payments(principal: int, payment_amount: int) -> int:
        return math.ceil(principal / payment_amount)


class LoanInterface:

    def main(self):
        loan = Loan(self.get_loan_info())

        print("What do you want to calculate?")
        print('type "m" - for number of monthly payments,')
        print('type "p" - for the monthly payment:')
        choice = input()
        while choice not in ['m', 'p']:
            print('Please choose from "m" or "p"')
            choice = input()

        self.generate_results(loan, choice)

    def get_loan_info(self) -> int:
        print("Enter the loan principal: ")
        principal = input()
        while not self.validate_numeric_input(principal):
            principal = input()
        return int(principal)

    def generate_results(self, loan: Loan, choice: str):
        if choice == 'm':
            print("Enter the monthly payment:")
            payment = input()

            while not self.validate_numeric_input(payment):
                payment = input()

            payment_count = LoanCalculator.calculate_number_of_payments(loan.principal, int(payment))
            print(
                f"It will take {payment_count} {'month' if payment_count == 1 else 'months'} to repay the loan")
        else:
            print("Enter the number of months:")
            months = input()

            while not self.validate_numeric_input(months):
                months = input()

            avg_payment, last_payment = LoanCalculator.calculate_monthly_payments(loan.principal, int(months))
            last_payment_str = f'and the last payment = {last_payment}'
            print(f'Your monthly payment = {avg_payment} {last_payment_str if avg_payment != last_payment else ""}')

    def validate_numeric_input(self, user_input: str) -> int:
        try:
            return int(user_input)
        except ValueError:
            print("Please enter valid numbers.")
            return False


if __name__ == '__main__':
    interface = LoanInterface()
    interface.main()
