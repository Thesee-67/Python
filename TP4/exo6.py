x = [5, 2, 4, 8, 1, 3]
print(x)

for i in range(len(x) - 1):
    min = x[i]
    for j in range(i + 1, len(x)):
        if x[j] < min:
            min = x[j]
            index = j
    if min < x[i]:
        temp = x[i]
        x[i] = x[index]
        x[index] = temp
    print(x)