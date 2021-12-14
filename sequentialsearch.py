def sequentialSearch(arr, val):
  for local in range(len(arr)):
    if val == arr[local]:
      return local
  return -1


if __name__ == "__main__":
  arr = []
  count = 0
  while count >= 0:
    print("""
Nhập 0 để thoát chương trình
Nhập 1 để thêm phần tử vào mảng
Nhập 2 để tìm kiếm tuần tự
Nhập 3 để in mảng
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
      y = str(input("Nhập phần tử muốn tìm kiếm: ")) 
      a = sequentialSearch(arr, y) 
      if a == -1:
        print(f"Không có {y} trong mảng")
      else:
        print(f"Vị trí của phần tử trong dãy: {a}")
    elif count == 3:
      print("Mảng:", end=" ")
      for i in arr:
        print(i, end=" ")



