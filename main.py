a = [["a", 5, ""], ["b", 2, ""], ["c", 1, ""], ["d", 1, ""]]


def ShannonFano(probability):
    summ = 0
    for i in probability:
        summ = summ + i[1]

    group = summ / 2
    index = 0
    group1 = []
    group2 = []

    for i in probability:
        if index < group:
            i[2] += '1'
            group1.append(i)
            index += i[1]
        else:
            i[2] += '0'
            group2.append(i)
    if len(group1) != 1:
        ShannonFano(group1)
    if len(group2) != 1:
        ShannonFano(group2)

    return probability
if __name__ == "__main__":
    print(ShannonFano(a))