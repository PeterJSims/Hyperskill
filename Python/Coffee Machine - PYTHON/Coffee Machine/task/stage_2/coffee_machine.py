class CoffeeMachine:
    INGREDIENTS_PER_CUP = {'water': 200, 'milk': 50, 'beans': 15}

    @staticmethod
    def calculate_cups(cups: int) -> tuple:
        water = CoffeeMachine.INGREDIENTS_PER_CUP['water'] * cups
        milk = CoffeeMachine.INGREDIENTS_PER_CUP['milk'] * cups
        beans = CoffeeMachine.INGREDIENTS_PER_CUP['beans'] * cups
        return water, milk, beans


class UserInterface:

    def main(self) -> None:
        print("Write how many cups of coffee you will need:")
        cups_needed = self._validate_input(input())

        if cups_needed:
            self._display_amounts(cups_needed)
        else:
            self.main()

    @staticmethod
    def _display_amounts(cups_needed: list) -> None:
        water, milk, beans = CoffeeMachine.calculate_cups(cups_needed)
        print(f"For {cups_needed} cups of coffee you will need:")
        print(f"{water} ml of water")
        print(f"{milk} ml of milk")
        print(f"{beans} g of coffee beans")

    @staticmethod
    def _validate_input(user_input: str) -> int:
        try:
            num_input = int(user_input)
            return num_input
        except ValueError:
            print("Please provide an integer")
            return None


if __name__ == '__main__':
    interface = UserInterface()
    interface.main()
