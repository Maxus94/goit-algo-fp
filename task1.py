class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

         

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):        
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def len_list(self):        
        if self.head:
            len = 1
        else: return 
        current = self.head
        while current.next is not None:
            current = current.next
            len += 1
        return len
    
    def get_middle(self):
        if self.head is None:
            return self.head
        slow = self.head
        fast = self.head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def sort(self):
        if self.head is None or self.head.next is None:
        # if len(self) <= 1:
            return self

        mid = self.get_middle()
        
        cur = self.head
        left_half = LinkedList()
        left_half.head = self.head
        # left_current = left_half.head
        print("Inside sort")
        print(left_half.head.data)
        while cur.next is not None and cur.next.data != mid.data:
            left_half.next = cur.next
            cur = cur.next
            print(left_half.next.data)
        # left_half = arr[:mid]
        # right_half = arr[mid:]
        # return merge(merge_sort(left_half), merge_sort(right_half))
        left_half.next = None
        print()
        print(cur.next.data)

        print()

        right_half = LinkedList()
        right_half.head = cur
        while cur.next is not None:
            right_half.next = cur.next
            cur = cur.next
            print(cur.data)
        
        print()

        print("Lists")
        left_half.print_list()
        print()
        right_half.print_list()

        return right_half
    

    # def sort(self):
    #     i = 1
    #     current = self.head        
    #     while current.next.next:
    #         tmp = current.next
    #         # current = current.next
    #         j = i - 1
    #         current = self.head
    #         while j >= 0:                
    #             prev_node = current
    #             current_node = current.next
    #             if prev_node.value > current_node.value:
    #                 prev_node.value = current_node.value
    #             j -= 1
            


                # tmp.data < current.next.next.data:
            # print(current.next.next.data)
                
            

            
        # for i in range(1, len(lst)):
        #     key = lst[i]
        #     j = i-1
        #     while j >=0 and key < lst[j] :
        #         lst[j+1] = lst[j]
        #         j -= 1
        #     lst[j+1] = key 


        




llist = LinkedList()


# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

llist.reverse()
print()
llist.print_list()
print()
print("Left")

l = llist.sort()
print()
l.print_list()
# llist.sort()

# # Видаляємо вузол
# llist.delete_node(10)

# print("\nЗв'язний список після видалення вузла з даними 10:")
# llist.print_list()

# # Пошук елемента у зв'язному списку
# print("\nШукаємо елемент 15:")
# element = llist.search_element(15)
# if element:
#     print(element.data)
