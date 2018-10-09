def find_first_two_sum_indices(l,sum):
    dict={}
    for i in range(len(l)):
        if l[i] in dict.keys():
            return(dict[l[i]], i )
        else:
            diff = sum - l[i]
            dict[diff] = i

idx1,idx2=find_first_two_sum_indices([5,-1,5,9,2,3,0],8)
print("The indices are {} and {}".format(idx1,idx2))

def find_all_two_sum_indices(l,sum):
    dict={}
    list=[]
    for i in range(len(l)):
        if l[i] in dict.keys():
            list.append([dict[l[i]], i] )
        else:
            diff = sum - l[i]
            dict[diff] = i
    return(list)


result=find_all_two_sum_indices([5,-1,5,9,2,3,0],8)
print(result)