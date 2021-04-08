word = ""

for x in range(101):
    if x % 3 == 0 and not x % 5 == 0:
        word = "Fizz"

    elif x % 5 == 0 and not x % 3 == 0:
        word = "Buzz"

    elif x % 3 == 0 and x % 5 == 0:
        word = "FizzBuzz"

    else:
        word = x

    print(word)
