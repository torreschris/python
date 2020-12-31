__author__ = 'torreschris'

class Amicables:
    def __init__(self, x):
        self.x = int(x)
        self.factors = self.get_factors(self.x)
        self.factors2 = self.get_factors(sum(self.factors))
        self.type = ''
        self.set_type()

    def get_factors(self, x):
        i = 2
        searchUnder = x
        factors = [1]
        while i < searchUnder:            
            if (x % i) == 0:
                factors.append(int(x / i))
                factors.append(i)
                searchUnder = x / i
            i += 1
        
        return sorted(factors)

    def set_type(self):
        if sum(self.factors) == self.x:
            self.type = 'Perfect'
        elif sum(self.factors2) == self.x:
            self.type = 'Amicable'
        else:
            self.type = 'Neither perfect or amicable'

def main():
    x = input("Enter a positive integer: ")
    A = Amicables(x)
    print("The factored numbers of " + str(A.x) + " is: " + str(A.factors))
    print("The sum of all factored numbers is: " + str(sum(A.factors)))
    print("The type is: " + A.type)
    if A.type == 'Amicable':
        print("It's amicable pair is: " + str(sum(A.factors)))
        print("It's factored numbers are: " + str(A.factors2))

if __name__ =='__main__':
    main()    