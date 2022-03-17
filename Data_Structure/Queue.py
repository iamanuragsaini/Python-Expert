# Python user-defined data structure in python --- Queue
# FIFO -- First In First Out
# LILO -- Last In Last Out

queue = []

def add():
    element = input("Enter the element: ")
    queue.append(element)
    print(queue)

def remove():
    e = queue.pop(0)
    print("Remove element",e)
    print(queue)

def display():
    print(queue)

while True:
    print("Enter the operation 1.Add 2.Remove 3.Display 4.Exit ")
    choice = int(input())
    if choice==1:
        add()
    elif choice==2:
        remove()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Enter the right operation.")