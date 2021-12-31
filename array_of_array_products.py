def array_of_array_products(arr):
    array_products = []
    for i in range(len(arr)):
        left_product = get_product(arr, 0, i)
        right_product = get_product(arr, i + 1, len(arr))
        array_products.append(left_product * right_product)

    return array_products


def get_product(arr, beg, end):
    product = 1
    for i in range(beg, end):
        product *= arr[i]
    return product


print(array_of_array_products([2, 7, 3, 4]))
