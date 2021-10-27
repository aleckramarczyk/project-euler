#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def main():
    found = False
    num = 2520
    #any number that is divisible by 1 through 20 will be a multiple of 2520, which is given to us in the problem
    #therefore, by checking only multiples of 2520 we save a massive amount of computing power compared to bruteforcing every number
    while found == False:
        print("Testing: " + str(num),end="\r")
        test = [num%n for n in range(11, 21)]
        if sum(test) == 0:
            print("\nThe smallest number that is divisible by 1-20 is: " + str(num))
            found = True
        else:
            num = num + 2520
if __name__ == "__main__":
    main()
