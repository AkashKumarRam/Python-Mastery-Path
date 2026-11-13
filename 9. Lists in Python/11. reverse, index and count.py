nums = [4, 7, 3, 8, 1, 1, 2, 10, 9, 6, 9, 1, 1, 1]

print(f"Nums is = {nums} and ID is = {id(nums)}")

"""
Reverse list ke just ulta kore dei. Accending ba decending order e sort korena
nums.reverse()
"""

"""
index() = new list baniye dei. Ete amra jodi value pass kore, e setake bole
dei koto number index e ache.

new_list = nums.index(8)
print(f"Nums is = {new_list} and ID is = {id(new_list)}")
"""

"""
Etau new list banai, ekhane kono value dile se bole dei oi value list e 
kotobar ache
"""
new_list = nums.count(1)
print(f"Nums is = {new_list} and ID is = {id(new_list)}")
