class Amicables:
    def __init__(self, x):
        self.x = x
        self.amicables = [1, int(self.x)]

    def get_amicables(self):
        print("Max: " + str(max(self.amicables)))
        print("Min: " + str(min(self.amicables)))



def main():
    x = input("Enter a positive integer: ")
    A = Amicables(x)
    A.get_amicables()


if __name__ =='__main__':
    main()
    