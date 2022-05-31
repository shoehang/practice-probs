class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
	head = ListNode()
	curretNode = head
	carry = 0

	while l1 is not None or l2 is not None:
		subsum = 0
		if l1:
			subsum += l1.val
		if l2:
			subsum += l2.val
		subsum += carry
		carry = subsum // 10
		curretNode.next = ListNode(subsum % 10)
		curretNode = curretNode.next
		if l1:
			l1 = l1.next
		if l2:
			l2 = l2.next
	if carry > 0:
		curretNode.next = ListNode(carry)
	return printLL(head.next)

def printLL(x):
	y = []
	copy = x
	while copy is not None:
		y.append(copy.val)
		copy = copy.next
	return y


x3 = ListNode(3)
x2 = ListNode(4, x3)
x1 = ListNode(2, x2)

y3 = ListNode(4)
y2 = ListNode(6, y3)
y1 = ListNode(5, y2)

print(addTwoNumbers(x1, y1))