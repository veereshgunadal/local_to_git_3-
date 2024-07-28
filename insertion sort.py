def insertion(l):
    for i in range(len(l)-1):
        small_index = i
        for j in range(i+1, len(l)):
            if l[j] < l[j-1]:
                small_index = j
        temp = l[i]
        l[i] = l[small_index]
        l[small_index] = temp
                
    return l

l = [1,3,2,4,9,7,8]
print(insertion(l))
print('1')


def selection(l):
    for i in range(len(l)-1):
        for j in range(i+1, 0 , -1):
            if l[j] < l[j-1]:
                temp1 = l[j]
                l[j] = l[j-1]
                l[j-1] = temp1
    return l
l = [1,3,2,4,9]
print(selection(l))