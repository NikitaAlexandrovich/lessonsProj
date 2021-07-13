def list_rev(arr):
    len_arr = len(arr) - 1
    i = len_arr
    while i != -1:
        if arr[i] % 2:
            del arr[i]
        else:
            arr[i] = arr[i] // 2

        i -= 1


lst = [1, 2, 3, 4, 5, 6]
list_rev(lst)

lst = [20, 5, 8, 7]
list_rev(lst)
print(lst)