from collections import defaultdict
def subarray_sum_equals_k(nums, k):
    count = 0
    current_sum = 0
    sum_map = defaultdict(int)
    sum_map[0] = 1
    for num in nums:
        current_sum += num
        # if (current_sum - k) in sum_map:
        #     count += sum_map[current_sum - k]
        # sum_map[current_sum] += 1
        count += sum_map[current_sum-k]
        sum_map[current_sum] += 1
    return count

#Example usage:
if __name__ == "__main__":
    nums = [5,1,4,6,5,9,2,7]
    k = 10
    print(subarray_sum_equals_k(nums, k))  # Output: 2

    nums = [1, 2, 3]
    k = 3
    print(subarray_sum_equals_k(nums, k))  # Output: 2

    nums = [5,5,1,4,5,1,9,1,2,7,4,6]
    k=10
    print(subarray_sum_equals_k(nums, k))