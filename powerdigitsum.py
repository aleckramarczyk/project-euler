#215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
#What is the sum of the digits of the number 21000?

def main():
    digit_list = []
    number = 2 ** 1000
    for digit in str(number):
        digit_list.append(int(digit))
    print(sum(digit_list))
if __name__ == "__main__":
    main()
#Solved by Alec Kramarczyk, October 28, 2021
