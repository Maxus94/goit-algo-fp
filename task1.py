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

    @staticmethod
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
    
    @staticmethod
    def merge_sort(self):
        if self.head is None or self.head.next is None:        
            return self

        mid = self.get_middle()        
        cur = self.head        
        left_half = LinkedList()        
        left_half.insert_at_end(cur.data)

        while cur.next is not None and not cur.data == mid.data:            
            cur = cur.next            
            left_half.insert_at_end(cur.data)                                
            
        left_half.next = None
        cur = cur.next
        right_half = LinkedList()
        if cur is not None:
            right_half.insert_at_end(cur.data)
        
            while cur.next is not None:
                right_half.next = cur.next
                right_half.insert_at_end(cur.next.data)
                cur = cur.next            
        
        print("Left list")        
        left_half.print_list()
        print("Right list")
        right_half.print_list()

        # sorted_list = self.merge_sorted(left_half.merge_sort(), right_half.merge_sort())
        # sorted_list = self.merge_sorted(LinkedList.merge_sort(left_half), LinkedList.merge_sort(right_half))
        sorted_list = LinkedList.merge_sorted(LinkedList.merge_sort(left_half), LinkedList.merge_sort(right_half))
        return sorted_list
    
    @staticmethod
    def merge_sorted(left, right):
        if left is None:
            return right
        
        if right is None:
            return left
        
        merged = LinkedList()
        left_index = 0
        right_index = 0
        left_cur = left.head
        right_cur = right.head

        # Спочатку об'єднайте менші елементи
        # while left_index < left.len_list and right_index < right.len_list:
        while left_index < LinkedList.len_list(left) and right_index < LinkedList.len_list(right):
            print(left_cur.data, right_cur.data)
            if int(left_cur.data) <= int(right_cur.data):
                merged.insert_at_end(left_cur)
                left_cur = left_cur.next
                left_index += 1
            else:
                merged.insert_at_end(right_cur)
                right_cur = right_cur.next
                right_index += 1

        # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
        # while left_index < len(left):
        while left_index < LinkedList.len_list(left):
            merged.insert_at_end(left_cur)            
            left_cur = left_cur.next
            left_index += 1

        # while right_index < len(right):
        while right_index < LinkedList.len_list(right):
            merged.insert_at_end(right_cur)
            right_cur = right_cur.next
            right_index += 1

        return merged

llist = LinkedList()
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)
llist.insert_at_end(20)
llist.insert_at_end(25)

print("Зв'язний список:")
llist.print_list()

print()
# l = llist.merge_sort()
l = LinkedList.merge_sort(llist)
print("Left list")
l.print_list()