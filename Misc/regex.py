#https://www.tutorialspoint.com/python/python_reg_expressions.htm
import re

line = "Cats are smarter than dogs";

searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
   print "searchObj.group() : ", searchObj.group()
   print "searchObj.group(1) : ", searchObj.group(1)
   print "searchObj.group(2) : ", searchObj.group(2)
else:
   print "Nothing found!!"

'''
When the above code is executed, it produces following result −

searchObj.group() :  Cats are smarter than dogs
searchObj.group(1) :  Cats
searchObj.group(2) :  smarter
'''

#!/usr/bin/python
import re

phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print "Phone Num : ", num

# Remove anything other than digits
num = re.sub(r'\D', "", phone)
print "Phone Num : ", num

'''
When the above code is executed, it produces the following result −

Phone Num :  2004-959-559
Phone Num :  2004959559
'''

'''
Sr.No.	Example & Description
1
[Pp]ython

Match "Python" or "python"

2
rub[ye]

Match "ruby" or "rube"

3
[aeiou]

Match any one lowercase vowel

4
[0-9]

Match any digit; same as [0123456789]

5
[a-z]

Match any lowercase ASCII letter

6
[A-Z]

Match any uppercase ASCII letter

7
[a-zA-Z0-9]

Match any of the above

8
[^aeiou]

Match anything other than a lowercase vowel

9
[^0-9]

Match anything other than a digit

Special Character Classes
Sr.No.	Example & Description
1
.

Match any character except newline

2
\d

Match a digit: [0-9]

3
\D

Match a nondigit: [^0-9]

4
\s

Match a whitespace character: [ \t\r\n\f]

5
\S

Match nonwhitespace: [^ \t\r\n\f]

6
\w

Match a single word character: [A-Za-z0-9_]

7
\W

Match a nonword character: [^A-Za-z0-9_]

Repetition Cases
Sr.No.	Example & Description
1
ruby?

Match "rub" or "ruby": the y is optional

2
ruby*

Match "rub" plus 0 or more ys

3
ruby+

Match "rub" plus 1 or more ys

4
\d{3}

Match exactly 3 digits

5
\d{3,}

Match 3 or more digits

6
\d{3,5}

Match 3, 4, or 5 digits
'''