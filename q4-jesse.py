def largest_number(numbers):
    return max(numbers)

input_list = []
for i in range(5):
    number = int(input(f"enter number {i+1}: "))
    input_list.append(number)

output = largest_number(input_list)
print(f"largest number: {output}")