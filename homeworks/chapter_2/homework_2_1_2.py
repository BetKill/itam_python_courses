sp = [int(s) for s in input("input array: \n").split()]


def summation(sp):
    answer = 0
    for i in range(len(sp)):
        if sp[i] < 0:
            sp[i] *= -2
    float_ = max(sp)
    for i in range(n):
        answer += sp[i] / float_
    return answer


print(summation(sp))
