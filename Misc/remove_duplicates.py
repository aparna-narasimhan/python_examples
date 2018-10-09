from collections import defaultdict


def remove_dup1(l):
    d = defaultdict(bool)
    for i in l:
        if d[i]:
            l.remove(i)
        else:
            d[i] = True
    print(l)

def remove_dup2(l):
    for p1 in l[::]:
        for p2 in l[l.index(p1)+1:len(l)]:
            if p1 == p2:
                l.remove(p2)

def remove_dup_sorted(l):
    flag=False
    for p1 in l[::]:
        for p2 in l[l.index(p1)+1:len(l)]:
            if p1 == p2:
                flag = True
                l.remove(p2)
            else:
                if flag:
                    flag = False
                    break

l = [1,3,4,0,3,5,1,6,2,1]
l1=[1,2,2,2,3,3,4,5,5,5,5,6]
#remove_dup_sorted(l1)
#print(l1)
#print(list(set(l1)))
print([set(l1)])