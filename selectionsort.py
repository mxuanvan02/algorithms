def selectionSort(arr):
  if len(arr) <= 1:
    return arr

  minE = arr[0]
  for ele in arr:
    if ele < minE:
      minE = ele

  minArr = [minE]
  arr2 = [ele for ele in arr if ele > minE]
  return minArr + selectionSort(arr2)

if __name__ == "__main__":
  arr = []
  count = 0
  while count >= 0:
    print("""
Nhập 0 để thoát chương trình
Nhập 1 để thêm phần tử vào mảng
Nhập 2 sắp xếp lựa chọn mảng
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
      sorted = selectionSort(arr)
      print("Mảng sau khi sắp xếp:", end=" ")
      for i in sorted:
        print(i, end=" ")








