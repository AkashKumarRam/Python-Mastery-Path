lst = ["Akash", 54, 45.56, True, "Anjali"]

print(lst, id(lst))

lst.append("Subrata")
lst.append(1900)

"""
Insert need two parameters. First one where to put and Second is what you put
"""
lst.insert(2, "Monu")

"""
Pop() = by default last er index ke remove kore dei. Pop() jetake remove kore
setake return kore. Chaile ami pop hoa value ke print korate pari. Pop(1) e
index number diyeu specific index ke pop korate pari

lst.pop(3)
value = lst.pop()
print(value)

"""
lst.pop()

"""
remove(54) = remove by value remove kore. Jodi ami chai 54 value take list
theke remove korte tahole ami korte parbo. Jodi same list e same value
multiple time thake tahole sobar first er value take se remove korbe
"""
lst.remove(54)

print(lst, id(lst))
