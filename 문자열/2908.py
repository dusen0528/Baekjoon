num = input().split()
num1 = num[0]
num2 = num[1]
if (int(num1[::-1])>int(num2[::-1])):
    print(num1[::-1])
else:
    print(num2[::-1])