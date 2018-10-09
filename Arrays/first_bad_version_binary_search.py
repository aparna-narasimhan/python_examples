class Solution(object):
	def firstBadVersion(self,n):
		first = 0
		last = n-1
		middle = (first+last)/2
		while(first <= last):
			if isBadVersion(middle) == False and isBadVersion(middle+1) == True:
				return middle+1
			elif isBadVersion(middle) == True:
				last=middle-1
			else:
			    first=middle+1
			middle = (first+last)/2

		if first>last:
		    return -1