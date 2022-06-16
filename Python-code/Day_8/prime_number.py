def prime_checker(number):
    is_prime = True
    for i in range(2, number - 1):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Number is prime\n")
    else:
        print("Number is not prime\n")

n = int(input("Enter the number which have to be checked:\n"))
prime_checker(number=n)