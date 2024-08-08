# Imagine you're at a movie theater with assigned seating. You have a seating chart represented by an array nums
# where nums[i] represents the seat number at row i. You're looking for two friends to sit together, considering their
# seat preferences and your limitations:
# Seating Distance: Your friends prefer to sit close together, with a maximum allowed seat difference of indexDiff.
# Imagine indexDiff = 2, meaning they'd be comfortable within 2 seats of each other (e.g., seats 3 and 5).
# Movie Preference: They also want similar movie tastes, requiring a difference in their seat numbers (abs(nums[i] -
# nums[j])) to be within valueDiff. Think of valueDiff = 1 as preferring movies with similar ratings (e.g., seats 4 and
# 5 for movies rated 4.5 and 5 stars).
# Your task is to determine if there are two friends (represented by two indices i and j) who can sit together while
# satisfying both the seating distance and movie preference limitations.

from sortedcontainers import SortedList

def canBeSeated(nums, indexDiff, valueDiff):
    sorted_list = SortedList()
    
    for i, num in enumerate(nums):
        # Removing elements that are not in the sliding window
        while sorted_list and i - sorted_list[0][1] > indexDiff:
            sorted_list.pop(0)
        
        # Checking valid pairs in the sorted list
        position = sorted_list.bisect_left((num - valueDiff, -1))
        if position < len(sorted_list) and abs(sorted_list[position][0] - num) <= valueDiff:
            return True
        
        # Inserting current seat into the sorted list
        sorted_list.add((num, i))
    
    return False

nums = [2, 3, 5, 4, 9]
indexDiff = 2
valueDiff = 1

print(canBeSeated(nums, indexDiff, valueDiff))  # Output = True
