topMax=5

def crtstk():
    stack=[]
    return stack
def roma(stack,item):
    if not isFull(stack):
        stack.append(item)
        return stack
    else:
        print("Ваш стек заповнений")
        
def isFull(steck):
    return len(stack)==(topMax-1)
def isEmpty (stack):
    return len(stack)==0
def remove (stack):
    if not isEmpty(stack):
        stack.pop()
        return stack
    else:
        print("Ваш стек порожній")
stack=crtstk()
for i in range(topMax):
    item=int(input("Введіть число"))
    roma(stack,item)
    print(f"Стек= ",stack,end="  ")
    