#The following iterative sequence is defined for the set of positive integers
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#Which starting number, under one million, produces the largest chain?

def main() :
    largest_count = 0
    longest_starting_number = 0
    for n in range(2, 1000000):
        print("Testing: " + str(n))
        icount = 0
        starting_number = n
        while n != 1:
            if n%2 == 0:
                n = n/2
                icount += 1
            else:
                n = (n * 3) + 1
                icount += 1
        if icount > largest_count:
            largest_count = icount
            longest_starting_number = starting_number
    print("The largest chain was produced by: " + str(longest_starting_number) + " with " + str(largest_count) + " iterations")

if __name__ == "__main__" :
    main()
#Solved by Alec Kramarczyk, October 27, 2021
