class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)
    def get_kth_node_from_last(self, k):
        length = 1
        cur = self.head
        while cur.next is not None :
            cur = cur.next
            length += 1
        print("length is" ,length)
        end_length = length - k
        cur  = self.head
        for i in range(end_length):
            cur =  cur.next
        return cur
    def get_kth_node_from_last2(self,k):
        slow = self.head
        fast = self.head
        for i in range(k):
            fast =  fast.next
        while fast is not None :
            slow = slow.next
            fast = fast.next
        return slow
#1. 우선 모든 노드의 개수를 구한다.
#2. linkedlist의 길이에서 k만킁 배고, 그만큼 이동 시킨다.
#3. 해당값을 반환 한다.
#이걸 개선해 볼 수 있을까?


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)
print("끝까지 갔다가 k만큼 돌아가기")
print(linked_list.get_kth_node_from_last2(2).data)
print("k만큼 차이가 나는 node 2개를 이용해서 뒤의 노드 반환하기")# 7이 나와야 합니다!