'''numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("Even numbers:", even_numbers)'''


'''text = "University"

reverse_text = ""

for char in text:
    reverse_text = char + reverse_text

print(reverse_text)'''


''''numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 7, 89]

total = 0

for num in numbers:
    total = total + num

average = total / len(numbers)

print("Average:", average)'''





'''numbers = [-1, 3, 34, -8, -9, 1]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest number:", smallest)'''



'''list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [4, 5, 6, 7]

common = []

for num in list1:
    if num in list2 and num in list3:
        common.append(num)

print("Common elements:", common)'''


'''numbers = [3, 10, 12, 54, 75, 89, 25, 23]

for num in numbers:
    if num % 3 != 0:
        print(num)'''
        

'''string = "university"

print("Number of characters:", len(string))'''


'''numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 85]

unique_numbers = list(set(numbers))
unique_numbers.sort()

print("Second smallest element:", unique_numbers[1])'''


'''numbers = [-1, 3, 34, -8, -9, 1]

numbers[0], numbers[-1] = numbers[-1], numbers[0]

print(numbers)'''


'''list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

for num in list1:
    if num in list2:
        print(num)'''
        


'''numbers = [3, 10, 15, 54, 75, 89, 25, 23]

for num in numbers:
    if num % 3 == 0 and num % 5 == 0:
        print(num)'''
        


'''numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

smallest = min(numbers)
largest = max(numbers)

print("Smallest element:", smallest)
print("Largest element:", largest)'''


'''numbers = [-1, 3, 34, -8, -9, 1]

numbers[0], numbers[2] = numbers[2], numbers[0]

print(numbers)'''



'''list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = set(list1) & set(list2)

print("Repeating values:", common)'''


num = int(input("Enter a number: "))

if num % 3 == 0:
    print("Square:", num ** 2)
else:
    print("The number is not divisible by 3.")















