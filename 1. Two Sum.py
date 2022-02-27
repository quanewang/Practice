def two_sum(nums, target):
    index_dict = {}
    for i in range(len(nums)):
        num = nums[i]
        vals = index_dict.get(num)
        if vals is None:
            index_dict.update({num: [i]})
        else:
            vals.append(i)
            index_dict.update({num: vals})

    for i in range(len(nums)):
        num = target - nums[i]
        vals = index_dict.get(num)
        if vals:
            for index in vals:
                if index != i:
                    return [i, index]
