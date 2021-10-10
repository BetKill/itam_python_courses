def product(a, b):
    if a < 0:
        a *= -1
    elif b < 0:
        b *= -1
    result = a * b
    print("Product of", a, "and", b, "equals", result)
    return result


def pre_product(a, b):
    sign = (str(a)[0] + str(b)[0]).count("-") % 2
    return product(abs(int(a)), abs(int(b))) * ((-1)**sign)


print(pre_product(-2, 3))


# def product(a, b):
#     if a < 0:
#         a *= -1
#     elif b < 0:
#         b *= -1
#     result = a * b
#     return result
#
#
# def pre_product(a, b):
#     sign = (str(a)[0] + str(b)[0]).count("-") % 2
#     print("Product of", a, "and", b, "equals", product(abs(int(a)), abs(int(b))) * ((-1)**sign))
#
#
# pre_product(-2, 3)