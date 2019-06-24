numbers = input("Enter a list element separated by space: ")
list_  = numbers.split()
n1 = int(input('Enter a number: '))
n = n1 % len(list_)

if n1 < 0 and abs(n1) > len(list_):
    print("wrong number!")
elif n1 > 0:
    print(list_[n:]+(list_[:n]))
else:
    print(list_[abs(n):] + list_[:abs(n)])