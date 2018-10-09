'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #Approach: 1.For each word in the list:
        #               a. store the word
        #               b. sort the word and append the sorted word as key and orig word as val in a dict
        #               c. return all the values in the dict

        anag_dict = defaultdict(list)
        result = []
        for word in strs:
            sorted_word = sorted(word)
            sorted_str = "".join(sorted_word)
            anag_dict[sorted_str].append(word)

        for words in anag_dict.values():
            result.append(words)

        return(result)