#n! means n × (n − 1) × ... × 3 × 2 × 1
#
#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
#Find the sum of the digits in the number 100!

def main():
    def factorial(number):
        product = 1
        while number > 1:
            product = product * number
            number -= 1
        return product
    num = factorial(100)
    faclist = []
    for digit in str(num):
        faclist.append(int(digit))
    print(sum(faclist))
if __name__ == "__main__":
    main()
#Solved by Alec Kramarczyk, October 28, 2021
