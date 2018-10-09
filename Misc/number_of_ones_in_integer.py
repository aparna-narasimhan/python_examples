num=8
count=0
while(num):
  print(num)
  if(num & 1 == 1):
   count+=1
  num=num >> 1
print(count)