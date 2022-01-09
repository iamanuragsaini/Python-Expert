# *args and **kwargs

def funargs(normal, *args, **kwargs):
    print(type(args))
    print(type(kwargs))
    print(normal)
    for i in args:
        print(f"{i}")
    print("\n")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")


nrm = "Nice to meet you!!"
lst1 = ["Anurag","Ankur","Ankit","chiku"]
lst2 = {
    "Anurag":"good",
    "Ankur":"excellent",
    "Ankit":"Brilliant",
    "chiku":"cool"
}

funargs(nrm,*lst1,**lst2)
