from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_dict=defaultdict(int)

        for num in nums:
            nums_dict[num]+=1

        values=nums_dict.values()
        #print(values)
        neg_values = [val*-1 for val in values]
        #print(neg_values)
        heapq.heapify(neg_values)
        #print(neg_values)

        result = []
        for i in range(k):
            result.append( -( heapq.heappop(neg_values) ) )
        #print(result)

        result_keys = set()
        count = 0
        for res in result:
            for key, val in nums_dict.items():
                if val == res and count < k:
                    if key not in result_keys:
                        count += 1
                        result_keys.add( key )

        return( list(result_keys) )
