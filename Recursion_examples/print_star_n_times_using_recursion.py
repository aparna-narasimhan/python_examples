def print_star(n):
    if n==0:
        return
    else:
        print('*')
        print_star(n-1)