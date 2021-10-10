

def debug_control(*arg):
    answer = 0
    for i in arg:
        answer += 1
    return answer


print(debug_control("Hello!", 1000, 7))