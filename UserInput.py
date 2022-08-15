value = input("Enter a random number between 1 and 10 (Im going to guess the final number you end up with): ")

print("Multiply your number by 9")
second_value = int(value) * 9
third_value = 0
sum = 0

print("Once you've multiplied it by 9, add the digits together e.g 73 = 7 + 3 = 10")
while (int(second_value) > 0):
    third_value = second_value % 10
    sum = sum + third_value
    second_value = second_value / 10


print("Add 77")
sum = int(sum) + 77
print("Divide your number by 10")
sum /= 10
print("Subtract 8 from your answer")
sum = sum - 8

print("is your answer:")
print(sum)
