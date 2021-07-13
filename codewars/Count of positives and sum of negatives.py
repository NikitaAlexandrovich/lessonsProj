def count_positives_sum_negatives(arr):
    count = []
    min = 0
    pos = 0
    if len(arr) == 0:
        return count
    else:
        for i in range(len(arr)):
            if arr[i] < 0:
                min = min + arr[i]
            elif arr[i] > 0:
                pos += 1

        count.append(pos)
        count.append(min)
        return count

print(count_positives_sum_negatives([-1]))