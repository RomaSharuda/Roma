topMax = 5

def crtstk():
    stack = []
    return stack

def roma(stack, item):
    if not isFull(stack):
        stack.append(item)
        return stack
    else:
        print("Ваш стек заповнений")

def isFull(stack):
    return len(stack) == topMax  

def isEmpty(stack):
    return len(stack) == 0

def remove(stack):
    if not isEmpty(stack):
        stack.pop()
        return stack
    else:
        print("Ваш стек порожній")

def split_even_odd(stack):
    even = []
    odd = []
    for num in stack:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd

stack = crtstk()

for i in range(topMax):
    item = int(input("Введіть число: "))
    roma(stack, item)
    print(f"Стек= ", stack, end="  ")

even_nums, odd_nums = split_even_odd(stack)
print("\nПарні числа: ", even_nums)
print("Непарні числа:", odd_nums)
