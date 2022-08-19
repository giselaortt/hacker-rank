#https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem?isFullScreen=true


def mergeLists(head1, head2):
    node_pointer = head1
    second_node =head2
    answer = SinglyLinkedList()

    while( node_pointer is not None or second_node is not None ):
        if( (second_node is None) or ( node_pointer is not None and  node_pointer.data < second_node.data ) ):
            answer.insert_node( node_pointer.data )
            node_pointer = node_pointer.next
        else:
            answer.insert_node( second_node.data )
            second_node = second_node.next

    return answer.head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()

