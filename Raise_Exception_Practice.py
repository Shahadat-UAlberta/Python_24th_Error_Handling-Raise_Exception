num = int(input())

if num % 2 != 0:
    raise Exception("Shouldn't be Odd Number.")
else:
    print(num)
