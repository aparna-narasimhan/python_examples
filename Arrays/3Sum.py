class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #Brute force - have 3 pointers and then check if sum of the 3 elements is 0: O(N^3)
        #Option2:
            #Sort the array
            #Get each element one by one, and keep pointers one at the first and then another at end
            #Check if the elements pointed by the 2 pointers equals inverse of the chosen element. If so add it to             #a list if not already there
            #If the sum is greater than inverse, decrement the end pointer
            #Otherwise increment the first pointer
            #n(log(n)) , linear time.

        nums.sort()
        print(nums)
        result = []
        #[-1, 0, 1, 2, -1, -4]
        #sorted: [-4,-1,-1,0,1,2]

        for i,num in enumerate(nums):
            p1 = i+1
            p2 = len(nums)-1
            inv = -(num)
            #print("p1={}, p2={}, inv={}".format(p1,p2,inv))
            while(p1<p2):
                #print("nums[p1]: {}, nums[p2]: {}".format(nums[p1], nums[p2]))
                if(nums[p1] + nums[p2] == inv):
                    if( [num,nums[p1],nums[p2]] not in result ):
                        result.append( [num,nums[p1],nums[p2]] )
                    p2-=1
                elif( nums[p1] + nums[p2] > inv ):
                    p2-=1
                else:
                    p1+=1
        return(result)