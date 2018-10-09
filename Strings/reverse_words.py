#Without using additional list
def reverse_words(arr):
  output = ''

  i,j = len(arr)-1, len(arr)
  while i > -1:
    c = arr[i].strip()
    if not c:
      output += ''.join( arr[i+1:j] )
      #output += ''.join(arr[i+1:j]
      output += ''.join( arr[i] )
      j = i
    i -= 1
  output += ''.join( arr[:j] )
  #output.append( arr[:j])
  return [x for x in output]

def reverse_words(arr):
    words = [[]]
    word = []
    output = []
    idx = 0
    for ch in arr:
        if ch != '  ':
            word.append(ch)
            #print(word)
        else:
            words.append(word)
            print(words)
            word = []
    words.append(word)
    print(words)

    for i in range(len(words)-1,-1,-1):
        for ch in words[i]:
            output.append(ch)
        output.append(" ")

    return(output)

arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
        'm', 'a', 'k', 'e', 's', '  ',
        'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
print(reverse_words(arr))