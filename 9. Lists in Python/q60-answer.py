"""
Given two lists, merge them into a single new list without modifying the
originals.
"""

nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]


def merge_lists(nums1, nums2):
    new_list = nums1 + nums2

    # Methord - 2
    # new_list = []
    # for num in nums1:
    #     new_list.append(num)
    # for num in nums2:
    #     new_list.append(num)
    return f"Your merged list is = {new_list}"


answer = merge_lists(nums1, nums2)
print(answer)
