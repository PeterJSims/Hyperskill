# write your code here

class BillSplitter:
    def __init__(self):
        self.friends = {}

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


class Interface:
    def __init__(self):
        self.bill_splitter = BillSplitter()

    def main(self):
        print("Enter the number of friends joining (including you):")
        friend_count = int(input())
        if friend_count > 0:
            self.bill_splitter.add_friends(friend_count)
            self.bill_splitter.display_friends()
        else:
            print("No one is joining for the party")


if __name__ == '__main__':
    interface = Interface()
    interface.main()
