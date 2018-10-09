sum=0
def sum_of_nums(num_list):
    if len(num_list) == 1:
        return(num_list[0])
    else:
        return(num_list[0]+sum_of_nums(num_list[1:]))

sum=sum_of_nums([1,2,3,4,5])
print(sum)