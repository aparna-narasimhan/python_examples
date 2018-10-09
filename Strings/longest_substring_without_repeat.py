#Return length of longest substring without repeating characters
#Eg: "pwwkew" => 4(pkew)
from collections import defaultdict
def lenngthOfLongestSubstring(s):
    #Approach:
    # Step1: Use two pointers - i goes through each char in the string, j goes from i + 1 upto any char that repeats.
    # Step2: when a char repeats, i is incremented to point to the next char and j is again i+1
    # Step3: Keep track of the length of non-repetitive chars and update max len accordingly
    # Return max_len

    char_occur = defaultdict(boolean)
    i = 0
    length = 0
    max_length = length
    #j = i + 1
    while i < len(s):
        if s[i] in char_occur:
            if length > max_length:
                max_len = length
            length = 1
            #i += 1
            #j = i + 1
        else:
            length += 1
            char_occur[s[j]] = True
        i += 1
        if length > max_length:
            max_length = length
        return(max_length)

