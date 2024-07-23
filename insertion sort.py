def insertion(l):
    for i in range(len(l)-1):
        small_index = i
        for j in range(i+1, len(l)):
            if l[j] < l[j-1]:
                small_index = j
        temp = l[i]
        l[i] = l[small_index]
        l[j] = temp

        