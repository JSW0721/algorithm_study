#하나씩 찾기
finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_sequential(target, array):
    find_count = 0
    for number in array:
        find_count += 1
        if target == number:
            print(find_count)
            return True

    return False

def is_existing_target_number_binary(target,array):
    current_min = 0
    current_max = len(array)-1
    current_guess = (current_min+current_max)//2
    find_count = 0

    while current_min <= current_max:
        find_count += 1
        if array[current_guess] == target:
            print(find_count)
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_min + current_max)//2

result1 = is_existing_target_number_sequential(finding_target, finding_numbers)
result2 = is_existing_target_number_binary(finding_target, finding_numbers)

print("result1 = ",result1)  # True
print("result2 = ",result2)  # True