class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.node = None
        self.length = 0

    def add(self, value, next_node):
        new_node = Node(value, next_node)
        if self.length == 0:
            self.node = new_node
        elif self.length == 1:
            self.node.next_node = new_node
        else:
            current = self.node.next_node
            while current.next_node:
                current = current.next_node
            current.next_node = new_node
        self.length += 1

    def sorted_merge(self, left_list, right_list):
        if left_list == None:
            return right_list
        if right_list == None:
            return left_list

        if left_list.value <= right_list.value:
            sorted_part = left_list
            sorted_part.next_node = self.sorted_merge(left_list.next_node, right_list)
        else:
            sorted_part = right_list
            sorted_part.next_node = self.sorted_merge(left_list, right_list.next_node)
        return sorted_part

    def merge_sort(self, head):

        if head == None or head.next_node == None:
            return head
        middle = self.get_middle(head)
        middle_next = middle.next_node
        middle.next_node = None
        left = self.merge_sort(head)
        right = self.merge_sort(middle_next)
        sorted_list = self.sorted_merge(left, right)
        return sorted_list

    def get_middle(self, head):
        if (head == None):
            return head

        middle = head
        next_mid = head

        while (next_mid.next_node != None and next_mid.next_node.next_node != None):
            middle = middle.next_node
            next_mid = next_mid.next_node.next_node
        return middle

    def print(self):
        current_node = self.node
        while current_node:
            print(current_node.value, end=' ')
            current_node = current_node.next_node


    def counter(self):
        max_cards_length = 0
        card_count = None
        remember = 0
        remember_number=0
        current_node = self.node
        while current_node:
            if int(current_node.value) == card_count:
                max_cards_length += 1
            else:
                max_cards_length = 0

            if max_cards_length != 0 and max_cards_length >= remember:
                remember = max_cards_length
                remember_number = current_node.value
            card_count = current_node.value
            current_node = current_node.next_node
        result=remember+1
        print("number with max sequence: {}".format(remember_number))
        print("max length of sequence: {}".format(result))
        return result


def long_poker():
    cards = LinkedList()

    for card in open('lngpok.in', 'r').readline().split():
        if int(card) > 1000000 or int(card) < 0:
            print("we haven't such card")
        if cards.length > 10000:
            print("write less cards")
        if int(card) == 0:
            print("congratulate! you have a jocker, choose the value:")
            your_joker_value = int(input())
            cards.add(int(your_joker_value), None)
        else:
            cards.add(int(card), None)
    print("LinkedList")
    LinkedList.print(cards)
    print("")

    cards.node = cards.merge_sort(cards.node)
    print("SortedLinkedList")
    LinkedList.print(cards)
    print("")
    result = LinkedList.counter(cards)
    open('lngpok.out', 'w').write(str(result))


if __name__ == '__main__':
    long_poker()
