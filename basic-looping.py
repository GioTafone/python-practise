#Program that uses a for loop to print the numbers from 1 to 10
for number in range(1, 11):
    print(number)
#Program that uses a while loop to print the numbers from 1 to 10.
i = 1
while i < 11:
    print(i)
    i += 1
#Program that uses a for loop to print the even numbers from 2 to 20.
for number in range(1, 21):
    if (number % 2) == 0:
        print(number)
#Program that uses a while loop to print the odd numbers from 1 to 15.
i = 1
while i < 16:
    if (i % 2) != 0:
        print(i)
    i += 1
#Program that uses a for loop to calculate the sum of all numbers from 1 to 100.
sum = 0
for number in range(1, 101):
    sum += number
print(sum)