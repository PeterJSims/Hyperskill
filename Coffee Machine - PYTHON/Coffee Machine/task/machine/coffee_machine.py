import interface


class CoffeeMachine:
    DRINK_TYPES = {"espresso": {'water': 250, 'milk': 0, 'beans': 16, 'cups': 1, 'cost': 4},
                   "latte": {'water': 350, 'milk': 75, 'beans': 20, 'cups': 1, 'cost': 7},
                   "cappuccino": {'water': 200, 'milk': 100, 'beans': 12, 'cups': 1, 'cost': 6}
                   }

    def __init__(self):
        """Initialize a coffee machine with the standard starting ingredient counts"""
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def display_state(self):
        """Show every ingredient in the machine's current state"""
        print()
        print("The coffee machine has: ")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")
        print()

    def determine_enough_ingredients(self, drink_type: str) -> bool:
        """Iterating through the drink type's necessary ingredients against the machine's current ingredient state.
        Return False if any of the ingredients are below the threshold for the given drink type."""
        return all([self.water >= self.DRINK_TYPES[drink_type]['water'],
                    self.milk >= self.DRINK_TYPES[drink_type]['milk'],
                    self.beans >= self.DRINK_TYPES[drink_type]['beans'],
                    self.cups >= self.DRINK_TYPES[drink_type]['cups']])

    def get_missing_ingredients(self, drink_type: str) -> list:
        """Return a list of the necessary drink ingredients that are larger than the machine's ingredient state."""
        missing_ingredients = []
        if self.water < self.DRINK_TYPES[drink_type]['water']:
            missing_ingredients.append('water')
        elif self.water < self.DRINK_TYPES[drink_type]['milk']:
            missing_ingredients.append('milk')
        elif self.beans < self.DRINK_TYPES[drink_type]['beans']:
            missing_ingredients.append('beans')
        elif self.cups < self.DRINK_TYPES[drink_type]['cups']:
            missing_ingredients.append('cups')
        return missing_ingredients

    def buy(self, drink_type: str) -> None:
        """Remove the ingredients and add the money to the current state for the corresponding drink"""
        self.water -= self.DRINK_TYPES[drink_type]['water']
        self.milk -= self.DRINK_TYPES[drink_type]['milk']
        self.beans -= self.DRINK_TYPES[drink_type]['beans']
        self.money += self.DRINK_TYPES[drink_type]['cost']
        self.cups -= 1

    def fill(self, water: int, milk: int, beans: int, cups: int) -> None:
        """Add ingredients for any ingredients above 0"""
        if water > 0:
            self.water += water
        if milk > 0:
            self.milk += milk
        if beans > 0:
            self.beans += beans
        if cups > 0:
            self.cups += cups

    def take(self) -> int:
        """Return the amount of money in the machine and set its state to 0"""
        temp_money = self.money
        self.money = 0
        return temp_money


if __name__ == '__main__':
    interface = interface.UserInterface()
    interface.main()
