'''
Given an array of integers, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution.
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=0, index2=1
'''

'''
Idea: loop over the list nums, start with an empty dictionary D, if (target - value) is NOT in D, then update the D by {value: index}, 
if yes, then it must be that we find the answer so return([index2, index1])
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {};
        for index1, value in enumerate(nums):   # now relook at the list nums again
            complement = target - value
            if complement not in hash_map:
                hash_map.update({value:index1})
            else:
                index2 = hash_map[complement]   # if it is true, then get the index of "target-value"
                return [index2,index1]
