class Node:
    def __init__(self, data):
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
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# 1. Зміна посилань для реверсування списку
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next  # Зберігаємо посилання на наступний вузол
        current.next = prev       # Змінюємо напрямок стрілки назад
        prev = current            # Переміщуємо покажчик prev на поточний
        current = next_node       # Переходимо до наступного вузла
    return prev  # Нова голова списку

# 2. Сортування злиттям
def merge_sort(head):
    if head is None or head.next is None:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next

    # / на дві частини
    middle.next = None

    # Рекурсивно --> ліву та праву
    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    sorted_list = merge_sorted_lists(left, right)
    return sorted_list

def get_middle(head):
    if head is None:
        return head
    slow = head
    fast = head
    # Використання метода швидкого та повільного вказівника
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# 3. б'єднання двох відсортованих списків
def merge_sorted_lists(head1, head2):
    # --> фіктивний вузол
    dummy = Node(0)
    tail = dummy

    while head1 and head2:
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    # Додаємо залишок
    if head1:
        tail.next = head1
    elif head2:
        tail.next = head2

    return dummy.next


if __name__ == "__main__":
    print("=== ТЕСТ 1: Реверсування списку ===")
    llist = LinkedList()
    llist.insert_at_end(10)
    llist.insert_at_end(20)
    llist.insert_at_end(30)
    llist.insert_at_end(40)
    
    print("Початковий список:")
    llist.print_list()
    
    # Реверсуємо
    llist.head = reverse_list(llist.head)
    print("Реверсований список:")
    llist.print_list()

    print("\n=== ТЕСТ 2: Сортування списку (Merge Sort) ===")
    llist_unsorted = LinkedList()
    import random
    for _ in range(6):
        llist_unsorted.insert_at_end(random.randint(1, 50))
        
    print("Невідсортований список:")
    llist_unsorted.print_list()
    
    # Сортуємо
    llist_unsorted.head = merge_sort(llist_unsorted.head)
    print("Відсортований список:")
    llist_unsorted.print_list()

    print("\n=== ТЕСТ 3: Об'єднання двох відсортованих списків ===")
    # --> відсортовані списки
    list1 = LinkedList()
    list1.insert_at_end(5)
    list1.insert_at_end(10)
    list1.insert_at_end(15)
    
    list2 = LinkedList()
    list2.insert_at_end(2)
    list2.insert_at_end(3)
    list2.insert_at_end(20)
    
    print("Список 1:")
    list1.print_list()
    print("Список 2:")
    list2.print_list()
    
    # --> oб'єднуємо
    merged_head = merge_sorted_lists(list1.head, list2.head)
    
    print("Об'єднаний відсортований список:")
    result_list = LinkedList()
    result_list.head = merged_head
    result_list.print_list()