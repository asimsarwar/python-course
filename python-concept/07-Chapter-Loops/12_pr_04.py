num = int(input("Enter the number: "))
prime = True

for i in range(2, num):
    print(i)
    if(num%i == 0):
        prime = False
        break
if prime:
    print("This number is Prime")
else:
    print("This number is not Prime")