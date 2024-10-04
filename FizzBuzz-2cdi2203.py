x = 0
y = int(input("整数を入力してください。"))

for x in range(y):
    x += 1

    if (x % 3 == 0) and (x % 5 == 0):
        print("Fizz Buzz")
        continue
        
    elif x % 5 == 0:
        print("Buzz")
        continue

    elif x % 3 == 0:
        print("Fizz ")
        continue

    else:
        print(x)  

#test