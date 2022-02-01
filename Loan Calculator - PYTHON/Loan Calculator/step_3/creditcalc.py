import math


class LoanCalculator:

    @staticmethod
    def calculate_monthly_payments(principal: int, periods: int, interest: float) -> int:
        i = LoanCalculator.calculate_nominal_interest_rate(interest)
        numerator = i * (1 + i) ** periods
        denominator = (1 + i) ** periods - 1
        return math.ceil(principal * (numerator / denominator))

    @staticmethod
    def calculate_number_of_payments(principal: int, payment_amount: int, interest: float) -> int:
        i = LoanCalculator.calculate_nominal_interest_rate(interest)
        n = math.log((payment_amount / (payment_amount - i * principal)), 1 + i)
        return math.ceil(n)

    @staticmethod
    def calculate_principal(annuity: float, periods: int, interest: float):
        i = LoanCalculator.calculate_nominal_interest_rate(interest)
        numerator = i * (1 + i) ** periods
        denominator = (1 + i) ** periods - 1
        p = annuity / (numerator / denominator)
        return math.floor(p)

    @staticmethod
    def calculate_nominal_interest_rate(interest: float):
        return interest / (12 * 100)


class LoanInterface:

    def main(self):
        print("What do you want to calculate?")
        print('type "n" for number of monthly payments,')
        print('type "a" for annuity monthly payment amount,')
        print('type "p" for loan principal:')

        choice = input().lower()
        while choice not in ['n', 'a', 'p']:
            print('Please choose from "n", "a", or "p"')
            choice = input()

        if choice == 'n':
            self.generate_monthly_payment_count()
        elif choice == 'a':
            self.generate_monthly_payment_amount()
        else:
            self.generate_principal()

    def generate_monthly_payment_count(self):
        try:
            print("Enter the loan principal: ")
            principal = float(input())
            print("Enter the monthly payment:")
            monthly_payment = float(input())
            print("Enter the loan interest:")
            interest = float(input())
            result = LoanCalculator.calculate_number_of_payments(principal, monthly_payment, interest)
            years, months = divmod(result, 12)
            print(f"It will take {years} years and {months} months to repay this loan!")
        except ValueError:
            print("Please enter valid values.")
            self.generate_monthly_payment_amount()

    def generate_monthly_payment_amount(self):
        try:
            print("Enter the loan principal: ")
            principal = float(input())
            print("Enter the number of periods:")
            periods = float(input())
            print("Enter the loan interest:")
            interest = float(input())
            result = LoanCalculator.calculate_monthly_payments(principal, periods, interest)
            print(f"Your monthly payment = {result}!")
        except ValueError:
            print("Please enter valid values.")
            self.generate_monthly_payment_amount()

    def generate_principal(self):
        try:
            print("Enter the annuity payment: ")
            annuity = float(input())
            print("Enter the number of periods:")
            periods = int(input())
            print("Enter the loan interest:")
            interest = float(input())
            result = LoanCalculator.calculate_principal(annuity, periods, interest)
            print(f"Your loan principal = {result}")
        except ValueError:
            print("Please enter valid values.")
            self.generate_principal()


if __name__ == '__main__':
    interface = LoanInterface()
    interface.main()
