class Node:
  def __init__(self, data):
    self.next = None
    self.data = data

class LinkedList:
  def __init__(self):
    self.head = None

def push(stack, data):
  new_node = Node(data)
  new_node.next = stack.head
  stack.head = new_node

def peek(stack):
  data = stack.head
  if data == None:
    return
  return data.data

def pop(stack):
  data = stack.head
  if data != None:
    stack.head = data.next
    return data













if __name__ == "__main__":
  stack = LinkedList()
  stack.head = Node(1)
  stack.head.next = Node(30)
  stack.head.next.next = Node(3)
  stack.head.next.next.next = Node(24)
  stack.head.next.next.next.next = Node(12)
  stack.head.next.next.next.next.next = Node(12)

  print("Stack: ")  
  temp = stack.head
  while temp:
    print(temp.data, end=" ")
    temp = temp.next
  print()
  count = 0
  while count >= 0:
    print("""
Nhập 0 để thoát chương trình
Nhập 1 để thêm phần tử vào stack
Nhập 2 để lấy phần tử từ stack
Nhập 3 để xoá phần tử từ stack
""")
    count = int(input())
    if count == 0:
      break
    elif count == 1:
      x = int(input("Nhập số bạn muốn thêm vào stack: "))
      push(stack, x)

      print("Stack sau khi thêm: ")
      temp = stack.head
      while temp:
        print(temp.data, end=" ")
        temp = temp.next
    elif count == 2:
      print("Phần tử được lấy ra: ", peek(stack))

    elif count == 3:
      a = pop(stack)
      print("Phần tử vừa xoá: ", a.data)
      print("Stack sau khi xoá 1 phần tử: ")
      temp = stack.head
      while temp:
        print(temp.data, end=" ")
        temp = temp.next






