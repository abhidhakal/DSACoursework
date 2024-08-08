# Imagine you're on a challenging hiking trail represented by an array nums, where each element represents the
# altitude at a specific point on the trail. You want to find the longest consecutive stretch of the trail you can hike
# while staying within a certain elevation gain limit (at most k).
# Constraints:
# You can only go uphill (increasing altitude).
# The maximum allowed elevation gain between two consecutive points is k.
# Goal: Find the longest continuous hike you can take while respecting the elevation gain limit.
# Examples:
# Input:
# Trail: [4, 2, 1, 4, 3, 4, 5, 8, and 15], Elevation gain limit (K): 3
# Output: 5
# Explanation
# Longest hike: [1, 3, 4, 5, 8] (length 5) - You can climb from 1 to 3 (gain 2), then to 4 (gain 1), and so on, all within the limit.
# Invalid hike: [1, 3, 4, 5, 8, 15] - The gain from 8 to 15 (7) exceeds the limit.

def longest_hike(nums, k):
    if not nums:
        return 0
    
    left = right = 0
    max_length = 1
    current_gain = 0
    
    while right < len(nums) - 1:
        right += 1
        
        # Calculate gain
        if nums[right] > nums[right-1]:
            current_gain += nums[right] - nums[right-1]
        
        # Adjust left pointer if gain exceeds k
        while current_gain > k and left < right:
            if nums[left+1] > nums[left]:
                current_gain -= nums[left+1] - nums[left]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

trail = [4, 2, 1, 4, 3, 4, 5, 8, 15]
k = 3
result = longest_hike(trail, k)
print(f"Longest hike: {result}")





