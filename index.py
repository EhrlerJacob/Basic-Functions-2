
def count(num):
    newOutput = []
    for i in range(num,-1,-1):
        newOutput.append(i)
    return newOutput
print(count(5))

def box(list):
    print(list[0])
    return list[1]
print(box([1,2]))

def sum(list):
    return list[0] + len(list)

print(sum([1,2,3,4,5]))

def greater_than(list):
    if len(list) < 2:
        return False
    newOutput = []
    for i in range(0,len(list)):
        if list[i] > list[1]:
            newOutput.append(list[i])
    print(len(newOutput))
    return newOutput 
print(greater_than([5,2,3,2,1,4]))
print(greater_than([3]))

def lengthVal(size,value):
    output = []
    for i in range(0, size):
        output.append(value)
    return output 
print(lengthVal(4,7))
print(lengthVal(6,2))
