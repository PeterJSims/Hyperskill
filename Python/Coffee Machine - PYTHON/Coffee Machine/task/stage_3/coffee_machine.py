class CoffeeMachine:
    INGREDIENTS_PER_CUP = {'water': 200, 'milk': 50, 'beans': 15}

    def __init__(self, water: int, milk: int, beans: int):
        self.water = water
        self.milk = milk
        self.beans = beans

    @staticmethod
    def calculate_cups(cups: int) -> tuple:
        water = CoffeeMachine.INGREDIENTS_PER_CUP['water'] * cups
        milk = CoffeeMachine.INGREDIENTS_PER_CUP['milk'] * cups
        beans = CoffeeMachine.INGREDIENTS_PER_CUP['beans'] * cups
        return water, milk, beans

    def calculate_cup_availability(self) -> int:
        possible_amount = min([self.water // self.INGREDIENTS_PER_CUP['water'], \
                               self.milk // self.INGREDIENTS_PER_CUP['milk'], \
                               self.beans // self.INGREDIENTS_PER_CUP['beans']])
        return possible_amount


class UserInterface:

    def __init__(self):
        self.machine = None

    def main(self) -> None:
        water, milk, beans = self._get_amounts()

        self.machine = CoffeeMachine(water, milk, beans)

        print("Write how many cups of coffee you will need:")
        cups_needed = self._validate_input(input())
        self._display_cups_possible(cups_needed)

    def _get_amounts(self) -> tuple:
        print("Write how many ml of water the coffee machine has:")
        water = self._validate_input(input())
        print("Write how many ml of milk the coffee machine has:")
        milk = self._validate_input(input())
        print("Write how many grams of coffee beans the coffee machine has:")
        beans = self._validate_input(input())
        if None in [water, milk, beans]:
            self._get_amounts()
        else:
            return water, milk, beans

    def _display_cups_possible(self, cups_needed: int) -> None:
        possible_cups = self.machine.calculate_cup_availability()
        if possible_cups == cups_needed:
            print("Yes, I can make that amount of coffee")
        elif possible_cups > cups_needed:
            print(f"Yes, I can make that amount of coffee (and even {possible_cups - cups_needed} more than that)")
        else:
            print(f"No, I can make only {possible_cups} cups of coffee")

    # @staticmethod
    # def _display_amounts(cups_needed: list) -> None:
    #     water, milk, beans = CoffeeMachine.calculate_cups(cups_needed)
    #     print(f"For {cups_needed} cups of coffee you will need:")
    #     print(f"{water} ml of water")
    #     print(f"{milk} ml of milk")
    #     print(f"{beans} g of coffee beans")

    @staticmethod
    def _validate_input(user_input: str) -> int:
        try:
            num_input = int(user_input)
            return num_input
        except ValueError:
            print("Please only provide integers")
            return None


if __name__ == '__main__':
    interface = UserInterface()
    interface.main()
