import sys
sys.setrecursionlimit(100000)

chosen_set=set()
def permute(s):
    permute_helper(s,"")

def permute_helper(s, chosen):
    #print("String is", s)
    #print("Chosen is", chosen)
    if s =="":
        if(chosen not in chosen_set):
            chosen_set.add(chosen)
            print(chosen)
    else:
        for ch in s:
            #choose
            idx=s.index(ch)
            s=s.replace(s[idx],'')
            chosen+=ch
            #explore
            permute_helper(s,chosen)
            #unchoose
            s=s.replace('',ch)
            chosen=chosen[:len(chosen)-1]

permute('abc')