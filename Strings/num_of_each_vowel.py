vowels={'a','e','i','o','u'}
result={'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
string = "anjana is a good girl"
for s in string:
    print(s)
    if s in vowels:
        result[s]=result[s] + 1
print(result)