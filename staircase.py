def staircase(n):

    for i in range(n):
        st = ""
        for j in range(n):

            if j < n - i-1:
                st += " "
            else:
                st += "#"

        print(st)
    return


n = 50
print(staircase(n))
