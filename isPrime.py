def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    
    return True

def main():
    while True:
        number = int(input("Enter a number: "))
        if number == 0:
            break
        if is_prime(number):
            print(number, "is prime")
        else:
            print(number, "is not prime")

main()
