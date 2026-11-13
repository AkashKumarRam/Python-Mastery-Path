nums = [4, 7, 3, 8, 1, 1, 2, 10, 9, 6, 9, 1, 1, 1]

"""
Difference between sort() and sorted()
sort() = same list er modhe sorting kore dei accending ba decending order e
eke in place sorting o bola hoi

nums.sort() = Accending Order
nums.sort(reverse=True) = Decending Order

sorted() = sorted accesnding ba decensing oder e list ke sort kore kintu
akta new list return kore. Sorted new List
"""
print(f"Nums is = {nums} and ID is = {id(nums)}")

# new_list = sorted(nums)
# print(new_list, id(new_list))

nums.sort()
print(f"Nums is = {nums} and ID is = {id(nums)}")
