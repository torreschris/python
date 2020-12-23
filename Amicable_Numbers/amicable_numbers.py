__author__ = 'torreschris'

class Amicables:
    def __init__(self, x):
        self.x = int(x)
        self.amicables = [1]

    def get_amicables(self):
        i = 2
        searchUnder = self.x
        while i < searchUnder:            
            if (self.x % i) == 0:
                self.amicables.append(int(self.x / i))
                self.amicables.append(i)
                searchUnder = self.x / i
            i += 1
        
        return sorted(self.amicables)


def main():
    x = input("Enter a positive integer: ")
    A = Amicables(x)
    amicable_no = A.get_amicables()
    print("The amicable numbers of " + str(A.x) + " is: " + str(amicable_no))    
    print("The sum of all amicable numbers is: " + str(sum(amicable_no)))

if __name__ =='__main__':
    main()    