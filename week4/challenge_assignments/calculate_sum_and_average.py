from typing import Union

def eval_sum_and_average(nums: list) -> Union[float, float]:
    total = 0
    for x in nums: 
        total += x

    avg = total/len(nums)
    return total, avg
