# Merge k sorted Lists - Leetcode - 23


# approach 1
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def mergeLists(lists):
    current = mergeTwoLists(lists[0], lists[1])
    for i in range(2, len(lists)):
        current = mergeTwoLists(current, lists[i])

    print(current)
    return arrayToLinkedList(current)


def arrayToLinkedList(arr):
    if not arr:
        return None

    head = Node(arr[0])
    current = head

    for i in range(1, len(arr)):
        new_node = Node(arr[i])
        current.next = new_node
        current = new_node
    return head.val


def mergeTwoLists(list1, list2):
    i, j = 0, 0
    ans = []
    print(list1, list2)
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            ans.append(list1[i])
            i += 1
        else:
            ans.append(list2[j])
            j += 1

    while i < len(list1):
        ans.append(list1[i])
        i += 1

    while j < len(list2):
        ans.append(list2[j])
        j += 1

    return ans


print(mergeLists([[1, 2, 4, 5], [2, 3, 4, 5, 6], [2, 9]]))


# approach 2
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        current = self.mergeTwoLists(lists[0], lists[1])
        for i in range(2, len(lists)):
            current = self.mergeTwoLists(current, lists[i])
        return current

    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        while list1:
            current.next = list1
            list1 = list1.next
            current = current.next

        while list2:
            current.next = list2
            list2 = list2.next
            current = current.next

        return dummy.next
