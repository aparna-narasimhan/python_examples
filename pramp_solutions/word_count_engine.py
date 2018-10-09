'''
Word Count Engine
Implement a document scanning function wordCountEngine, which receives a string document and returns a list of all unique words in it and their number of occurrences, sorted by the number of occurrences in a descending order. If two or more words have the same count, they should be sorted according to their order in the original sentence. Assume that all letters are in english alphabet. You function should be case-insensitive, so for instance, the words “Perfect” and “perfect” should be considered the same word.

The engine should strip out punctuation (even in the middle of a word) and use whitespaces to separate words.

Analyze the time and space complexities of your solution. Try to optimize for time while keeping a polynomial space complexity.

Examples:

input:  document = "Practice makes perfect. you'll only
                    get Perfect by practice. just practice!"

output: [ ["practice", "3"], ["perfect", "2"],
          ["makes", "1"], ["youll", "1"], ["only", "1"],
          ["get", "1"], ["by", "1"], ["just", "1"] ]
'''
#Note: Use OrderedDict so that the order of the words(keys) are maintained.
from collections import OrderedDict
def word_count_engine(document):
  freq_dict = OrderedDict()
  document = document.lower()
  for ch in document:
      if not ( ord(ch) >= ord('A') and ord(ch) <= ord('Z') ) and not (ord(ch) >= ord('a') and ord(ch) <= ord('z')) and not ch == " ":
          document = document.replace(ch, "")
  #print(line)
  count = 0
  for words in document.split():
    if freq_dict.get(words):
      freq_dict[words] += 1
    else:
      freq_dict[words] = 1
    count += 1
  #print(freq_dict)
  words_arr = [None] * (count + 1)
  #print(words_arr)
  for key in freq_dict.keys():
      val = freq_dict[key]
      if words_arr[val] == None:
        words_arr[val] = []
      words_arr[val].append(key)
  #print(words_arr)
  result = []
  for i in range(len(words_arr)-1,0,-1):
    #print(i)
    if words_arr[i] is not None:
      for word in words_arr[i]:
        result.append([word,str(i)])
  return(result)

