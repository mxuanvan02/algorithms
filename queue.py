class Node:
  def __init__(self, data):
    self.next = None
    self.data = data

class LinkedList:
  def __init__(self):
    self.head = None


def enqueue(queue, data):
  new_node = Node(data)
  if queue.head == None:
    queue.head == new_node
    return

  last = queue.head
  while last.next:
    last = last.next
    if last.next == None:
      last.next = new_node
      break

def dequeue(queue):
  temp = queue.head
  if temp != None:
    queue.head = temp.next
    temp = None
    return
    

def peek(queue):
  if queue.head == None:
    return
  return queue.head.data

if __name__ == "__main__":
  queue = LinkedList()
  queue.head = Node(1)
  queue.head.next = Node(30)
  queue.head.next.next = Node(3)
  queue.head.next.next.next = Node(24)
  queue.head.next.next.next.next = Node(12)
  queue.head.next.next.next.next.next = Node(12)

  print("Queue: ")  
  temp = queue.head
  while temp:
    print(temp.data, end=" ")
    temp = temp.next
  print()
  count = 0
  while count >= 0:
    print("""
Nhập 0 để thoát chương trình
Nhập 1 để thêm phần tử vào queue
Nhập 2 để lấy phần tử từ queue
Nhập 3 để xoá phần tử từ queue
""")
    count = int(input())
    if count == 0:
      break
    elif count == 1:
      x = int(input("Nhập số bạn muốn thêm vào queue: "))
      enqueue(queue, x)

      print("Queue sau khi thêm: ")
      temp = queue.head
      while temp:
        print(temp.data, end=" ")
        temp = temp.next
    elif count == 2:
      print("Phần tử được lấy ra: ", peek(queue))

    elif count == 3:
      dequeue(queue)
      print("Queue sau khi xoá 1 phần tử: ")
      temp = queue.head
      while temp:
        print(temp.data, end=" ")
        temp = temp.next






