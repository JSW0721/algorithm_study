#문제 : 배달의 민족 서버 개발자로 입사했다.
# 상점에서 현재 가능한 메뉴가 ["떡볶이", "만두", "오뎅", "사이다", "콜라"] 일 때, 유저가 ["오뎅", "콜라", "만두"] 를 주문했다.
# 그렇다면, 현재 주문 가능한 상태인지 여부를 반환하시오.
shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

def is_available_to_order(menus, orders):
    menus_set = set(menus) # O(N)
    for order in orders: # M -> O(M)
        if order not in menus_set: #O(1)
            return False
        return True
# 이 함수의 시잔 복잡도 => O(N) + ( O(M) * O(1)) = O(N+M)

def is_available_to_order_binary(menus, orders):
    menus.sort() #메뉴의 길이가 N => O(NlogN)
    for order in orders: #메누의 길이가 => O(M)
        if not is_exist_target_binary(order, menus): #O(logN)
            return False
    return True
    # 이 함수의 시간 복잡도 => O(NlogN) + (O(M) * O(logN)) = O((M+N)*logN)
def is_exist_target_binary(target,array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max)//2
    find_count = 0

    while current_min <= current_max:
        find_count += 1
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_min + current_max)//2
    return False

result1 = is_available_to_order(shop_menus, shop_orders)
print(result1)
result2 = is_available_to_order_binary(shop_menus, shop_orders)
print(result2)
# O(N+M) < O((M+N)*logN)
# 결론 : 이진 탐색이 항상 모든 상황에서 효율적인 것은 아니다.