def plusMinus(arr):
    pos = neg = zer = 0
    for i in range(n):
        if arr[i] > 0:
            pos += 1
        elif arr[i] < 0:
            neg += 1
        else:
            zer += 1
    positive = "%.6f" % (pos/n)

    negative = "%.6f" % (neg/n)

    zero = "%.6f" % (zer/n)

    return "{}\n{}\n{}".format(positive, negative, zero)


n = 8
arr = [1, 2, 3, -1, -2, -3, 0, 0]
print(plusMinus(arr))
