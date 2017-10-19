def fizzbuzz(low, high):
    for x in range(low, high+1):
        if x%3 == 0 and x%5 == 0:
            print("FizzBuzz")
        elif x%3 == 0:
            print("Fizz")
        elif x%5 == 0:
            print("Buzz")
        else:
            print(x)

fizzbuzz(int(input("Low value: ")), int(input("High value: ")))
