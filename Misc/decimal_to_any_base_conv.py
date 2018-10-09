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

def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

print(baseConverter(25,2))
print(baseConverter(25,16))