def bubbleSort(arr):
  for i in range(len(arr) - 1):
    # push the largest element to float
    for j in range(len(arr) - 1 - i):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]




if __name__ == "__main__":
  arr = []
  count = 0
  while count >= 0:
    print("""
Nhập 0 để thoát chương trình
Nhập 1 để thêm phần tử vào mảng
Nhập 2 sắp xếp nổi bọt mảng
""")
    count = int(input())
    if count == 0:
      break
    elif count == 1:
      x = str(input("Nhập phần tử muốn thêm vào mảng: "))
      arr.append(x)
      for i in arr:
        print(i, end=" ")
    elif count == 2:
      bubbleSort(arr)
      print("Mảng sau khi sắp xếp:", end=" ")
      for i in arr:
        print(i, end=" ")


