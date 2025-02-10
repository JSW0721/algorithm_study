input = "011110"

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    turn_to_all_zero = 0
    turn_to_all_one = 1

    if string[0] == '0':
        turn_to_all_zero +=1
    elif string[0]=='1':
        turn_to_all_one +=1

    return 1

result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)