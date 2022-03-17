# Python user-defined data structure in python --- Stack
# FILO ---- First In Last Out

stack = []

def push():
    if len(stack) == n:
        print("Stack full!!")
    else:
        element = input("Enter the element: ")
        stack.append(element)
        print(stack)

def pop():
    if not stack:
        print("Add element in stack")
    else:
        e = stack.pop()
        print("Remove element ",e)
        print(stack)


n = int(input("Enter the stack size: "))

while True:
    print("Enter the operation 1.Push 2.Pop 3.Exit ")
    choice = int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("Enter the right operation.")