def count_down(number):
    print(number)
    count_down(number - 1)
    if number < 0:

count_down(60)