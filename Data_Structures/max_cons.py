class Solution:
  def findMaxConsecutiveOnes(self, nums):
    # space complexity: O(1)
    max_ones = 0 
    ones = 0 

    # time complexity: O(n)
    for i in range(len(nums)):
      if nums[i] == 1:
        ones += 1
      else:
        if ones >= max_ones:
          max_ones = ones
        ones = 0
    if ones >= max_ones:
      return ones
    else:
      return max_ones


def main():
 sol = Solution()

 nums1 = [1, 1, 0, 1, 1, 1]
 output1 = sol.findMaxConsecutiveOnes(nums1)
 print(f"The maximum number of consecutive 1s in {nums1} is: {output1}") # Expected output: 3

 nums2 = [0, 0, 0, 0]
 output2 = sol.findMaxConsecutiveOnes(nums2)
 print(f"The maximum number of consecutive 1s in {nums2} is: {output2}") # Expected output: 0

 nums3 = [1, 1, 1, 1, 1]
 output3 = sol.findMaxConsecutiveOnes(nums3)
 print(f"The maximum number of consecutive 1s in {nums3} is: {output3}") # Expected output: 5

 nums4 = [1, 0, 1, 0, 1]
 output4 = sol.findMaxConsecutiveOnes(nums4)
 print(f"The maximum number of consecutive 1s in {nums4} is: {output4}") # Expected output: 1

 nums5 = [1, 1, 0, 1, 1, 1, 0, 1]
 output5 = sol.findMaxConsecutiveOnes(nums5)
 print(f"The maximum number of consecutive 1s in {nums5} is: {output5}") # Expected output: 3

main()