class Solution(object):
    def shuffle(self, nums, n):
        ans = []  # Create an empty list to store the final result

        # Loop runs from 0 to n-1
        for i in range(n):
            ans.append(nums[i])     # Add xᵢ from the first half
            ans.append(nums[i + n]) # Add yᵢ from the second half

        return ans  # Return the shuffled result
