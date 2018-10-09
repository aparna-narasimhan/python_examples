class Stack:
    def __init__(self, stack=[]):
	    self.stack = stack

    def push(self,data):
	    self.stack.append(data)

    def pop(self):
	    return(self.stack.pop())

    def is_empty(self):
	    if self.size() == 0:
		    return True

    def size(self):
	    return(len(self.stack))

def check_paranthesis(s,str):
    for ch in str:
	    if ch == '(':
	        s.push(ch)
	    if ch == ')' and s.pop() != '(':
		    return False
    if(s.is_empty()):
	    return True
    else:
	    return False

def main():
    s = Stack()
    str='(()'
    balanced = check_paranthesis(s, str)
    print(balanced)
main()

