max = int(input("Enter max number: "))

odd_numbers = []

for i in range(1, max):
    if i % 2 == 1:
        odd_numbers.append(i)

print("Odd numbers: ", odd_numbers)



# Sir, can't we simply do the following
'''
x = int(input("Please add max number : "))
odd_num = list(range(1, x+1, 2))
print(odd_num)
'''
