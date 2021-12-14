def insertionSort(arr):
  for eleN in range(1, len(arr)):
    key = arr[eleN]
    temp = eleN - 1

    while key < arr[temp] and temp >= 0:
      arr[temp + 1] = arr[temp]
      temp -= 1

    arr[temp + 1] = key






if __name__ == "__main__":
  arr = []
  count = 0
  while count >= 0:
    print("""
Nhập 0 để thoát chương trình
Nhập 1 để thêm phần tử vào mảng
Nhập 2 sắp xếp chèn mảng
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
      insertionSort(arr)
      print("Mảng sau khi sắp xếp:", end=" ")
      for i in arr:
        print(i, end=" ")



