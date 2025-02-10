def find_max_num(array):
# 1. 각 숫자들을 뒷 순서 숫자들과 비교해 보기 => array 길이가 길수록 비효율적
#    for number in array:
#        is_max_num = True
#        for compare_number in array:
#            if number < compare_number:
#                is_max_num = False
#        if is_max_num:
#            return number
#
# 2. 첫 숫자를 변수에 넣고, 큰 숫자가 나올때마다 변수를 바꿔주기
    max_num = array[0]
    for number in array:
        if number > max_num:
            max_num = number
    return max_num

print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))