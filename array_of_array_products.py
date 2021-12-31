def array_of_array_products(arr):
    left_products = []
    right_products = []
    array_products = []
    for i in range(len(arr)):
        if i == 0:
            left_products.append(1)
        else:
            left_products.append(left_products[i - 1] * arr[i - 1])

    for i in range(len(arr) - 1, -1, -1):
        if i == len(arr) - 1:
            right_products.append(1)
        else:
            right_products.insert(0, right_products[0] * arr[i + 1])

    for i in range(len(arr)):
        array_products.append(left_products[i] * right_products[i])

    return array_products


print(array_of_array_products([2, 7, 3, 4]))
print(array_of_array_products([8, 10, 2]))
