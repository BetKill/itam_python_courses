voc = {}


def Recursion(arr):
    for elem in arr:
        if isinstance(elem, list) == 1:
            Recursion(elem)
        else:
            for char in elem:
                if char not in voc:
                    voc[char] = 1
                else:
                    voc[char] += 1


l = ["wow", ["waow", "1000-7", "wahoo", ["oh"], ["dead", ["inside"]]]]
Recursion(l)
print(voc)