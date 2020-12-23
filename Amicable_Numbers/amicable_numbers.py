__author__ = 'torreschris'

class Amicables:
    def __init__(self, x):
        self.x = x
        self.amicables = [1, int(self.x)]

    def get_amicables(self):
        i = 2
        n = max(self.amicables)
        while i < n:            
            if (max(self.amicables) % i) == 0:
                self.amicables.append(int(max(self.amicables) / i))
                self.amicables.append(int(i))
                n = n / i
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