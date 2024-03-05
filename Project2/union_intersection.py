class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current_head = self.head
        out_string = ""
        while current_head:
            out_string += str(current_head.value) + "-->"
            current_head = current_head.next
        return out_string

    def append(self, value):
        if self.head == None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node  = node.next
        return size

def union(ll1, ll2):
    union_linked_list = LinkedList()
    node1 = ll1.head
    node2 = ll2.head
    if node1 is None and node2 is None:
        return union_linked_list
    if node1 is None:
        node1 = node2
    elif node2 is None:
        node2 = node1

    u_list = [] #list of values of the union.

    while node1: #O(n)
        if node1.value not in u_list:#O(n)
            u_list.append(node1.value)
        while node2:#O(n)
            if node1.value != node2.value and node2.value not in u_list: #O(n)
                u_list.append(node2.value)
            node2 = node2.next
        node1 = node1.next
    for i in u_list:#O(n)
        union_linked_list.append(i)
    return union_linked_list

def intersection(ll1,ll2):
    intersection_linked_list = LinkedList()
    node1 = ll1.head
    node2 = ll2.head
    i_list = []

    while node1:#O(n)
        while node2:#O(n^2)
            if node1.value == node2.value and node2.value not in i_list:
                i_list.append(node2.value)
            node2 = node2.next
        node1 = node1.next
        node2 = ll2.head
    for i in i_list:#O(n)
        intersection_linked_list.append(i)
    return intersection_linked_list

# Test case1
print("Test case 1")
ll1 = LinkedList()
ll2 = LinkedList()
ele1 = [3,2,4,35,6,65,6,4,3,21]
ele2 = [6,32,4,9,6,1,11,21,1]
for i in ele1:
    ll1.append(i)
for i in ele2:
    ll2.append(i)
print(union(ll1, ll2))
print(intersection(ll1, ll2))
# Output:
# Test case 1
# 3-->6-->32-->4-->9-->1-->11-->21-->2-->35-->65-->
# 4-->6-->21-->
## Test case 2
print("Test case 2")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()
element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]
for i in element_1:
    linked_list_3.append(i)
for i in element_2:
    linked_list_4.append(i)
print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
# Output:
# Test case 2
# 3-->1-->7-->8-->9-->11-->21-->2-->4-->35-->6-->65-->23-->
# no intersection output
## Test case 3
print("Test case 3")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()
element_1 = []
element_2 = [1,7,8,9,11,21,1]
for i in element_1:
    linked_list_3.append(i)
for i in element_2:
    linked_list_4.append(i)
print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
# Output:
# Test case 3
# 1-->7-->8-->9-->11-->21-->
# no intersection output
## Test case 4
print("Test case 4")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()
element_1 = []
element_2 = []
for i in element_1:
    linked_list_3.append(i)
for i in element_2:
    linked_list_4.append(i)
print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
# Output:
# Test case 4
# no union or intersection outputs

## Test case 5
print("Test case 5")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()
element_1 = [1,1,1,1]
element_2 = [1,1,1,1]
for i in element_1:
    linked_list_3.append(i)
for i in element_2:
    linked_list_4.append(i)
print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
# Output:
# Test case 5
# 1-->
# 1-->
