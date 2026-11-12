count = 0

def increase():
    global count
    count += 1
    print(f"Inside the function count is = {count}")

increase()
increase()
print(count)