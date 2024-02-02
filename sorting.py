dupnums = [1,5,2,9,4,3,100,6,56,89,12,5000]

def sortnum(arg):
    for i in range(len(arg) - 1, 0, -1):
        for j in range(i + 1, len(arg)):
            if arg[i] < arg[j]:
                temp = arg[i]
                arg[i] = arg[j]
                arg[j] = temp
    return arg

print(sortnum(dupnums))
