'''
Bracket Match
A string of brackets is considered correctly matched if every opening bracket in the string can be paired up with a later closing bracket, and vice versa. For instance, “(())()” is correctly matched, whereas “)(“ and “((” aren’t. For instance, “((” could become correctly matched by adding two closing brackets at the end, so you’d return 2.

Given a string that consists of brackets, write a function bracketMatch that takes a bracket string as an input and returns the minimum number of brackets you’d need to add to the input in order to make it correctly matched.

Explain the correctness of your code, and analyze its time and space complexities.

Examples:

input:  text = “(()”
output: 1

input:  text = “(())”
output: 0

input:  text = “())(”
output: 2
'''
#Note: Since its only 1 type of bracket, you don't even need stack, just use an ordinary counter variable.
def bracket_match(text):
  #Set count=0
  #Push open brackets to a stack
  #when it is a closed bracket:
      #if stack is empty - count+=1
      #else pop() and check
           #if its a '(' else count += 1
  #repeat till end of the string
  #if stack is not empty, count +=1
  #return count

  count = 0
  insert_count = 0
  for i in text:
    if i == '(':
      insert_count += 1
    else:
      if insert_count > 0:
        insert_count -= 1
      else:
        count += 1

  count += insert_count
  return(count)