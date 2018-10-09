#Given two strings, determine if they share a common substring. A substring may be as small as one character.
#For example, the words "a", "and", "art" share the common substring . The words "be" and "cat" do not share a substring.

#Option1: Convert strings to set and see if they intersect
    #Option2: Store each char in 1st string in a dictionary, iterate each char in 2nd string and verify if its already in the dict.
    #Option3: Does String contain only ASCII chars? If so can use an array of 128 or 256 chars to store ord(char) in first string. Then check char in 2nd string exist in dict.

#Option1:
def twoStrings(s1, s2):
    if(set(s1) & set(s2)):
        return "YES"
    else:
        return "NO"

#Option3
def twoStrings(s1, s2):

    #Solution: Choose Option 3
    str_list = [False] * 128
    for ch in s1:
        if(not str_list[ord(ch)]):
            str_list[ord(ch)] = True
    for chars in s2:
        if(str_list[ord(chars)]):
            return "YES"
    return "NO"



