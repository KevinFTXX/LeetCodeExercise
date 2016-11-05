'''
Given an array of integers, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution.
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=0, index2=1
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}   # create a dictionary, each entry in the dictionary is  key: value
        for index, value in enumerate(nums): # iterate the index and value of all the entry in the list nums, a tuple (index, value) is generated
            hash_map[value] = index   # the value in nums become the key and it stores the index of that value in nums
        # the 1st loop go through all the entris in nums and create a dict
        
        for index1, value in enumerate(nums):   # now relook at the list nums again
            if target - value in hash_map: # check if the "target-value" in the key of hash_map
                index2 = hash_map[target - value]   # if it is true, then get the index of "target-value"
                if index1 != index2:                # check whether these 2 indexs are different, e.g., target = 10, value = 5, index1 = 1, in this case index2 = 1 too, so index1 can equal to index2
                    return [index1 + 1, index2 + 1] # 
