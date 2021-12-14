import random
import interface


class BillSplitter:
    def __init__(self):
        """Start with an empty friend list and no name set as the (optional) lucky friend"""
        self.friends = {}
        self.lucky_friend = None

    def add_friends(self, friend_count: int) -> None:
        """Iterate through a count of the number of friends, taking input for each count"""
        if friend_count > 0:
            print("Enter the name of every friend (including you), each on a new line:")
            for _ in range(friend_count):
                name = input()
                self.friends[name] = 0
        else:
            print("No friends to add")

    def display_friends(self) -> None:
        """Print friends dict"""
        print(self.friends)

    def divide_payment(self, bill: int) -> None:
        """Divide the payment equally amongst the number of friends, minus the optional lucky friend.
        Assign that amount to every friend, minus the optional lucky friend."""
        if self.lucky_friend:
            avg = round(bill / (len(self.friends) - 1), 2)
            for friend in self.friends:
                if friend != self.lucky_friend:
                    self.friends[friend] = avg
        else:
            avg = round(bill / len(self.friends), 2)
            for friend in self.friends:
                self.friends[friend] = avg

    def set_lucky_friend(self):
        """Randomly choose a friend's name from a list of friend keys."""
        self.lucky_friend = random.choice(list(self.friends))



if __name__ == '__main__':
    interface = interface.Interface()
    interface.main()
