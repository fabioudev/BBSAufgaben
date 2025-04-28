L = [0, 1, 2, 3, 4, 5]

def kopiere_und_erhoehe(list):
    returnList = []
    for i in list:
        i += 1
        returnList.append(i)
    return returnList

print(kopiere_und_erhoehe(L))