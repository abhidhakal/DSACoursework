# Imagine a small community with n houses, numbered 0 to n-1. Some houses have restriction against becoming
# friends, represented by pairs in the restriction list. For example, if [0, 1] is in the list, houses 0 and 1 cannot be
# directly or indirectly friends (through common friends).
# Residents send friend requests to each other, represented by pairs in the requests list. Your task is to determine if
# each friend request can be accepted based on the current friendship network and the existing restriction.

from collections import deque

def can_be_friends(graph, restrictions, houseA, houseB):
    # Check if there is a path from houseA to any restricted pair involving houseB
    for restrictedHouseA, restrictedHouseB in restrictions:
        if (houseA == restrictedHouseA and houseB == restrictedHouseB) or (houseA == restrictedHouseB and houseB == restrictedHouseA):
            return False
        
        # BFS from restrictedHouseA to see if we can reach restrictedHouseB through houseA-houseB connection
        queue = deque([restrictedHouseA])
        visited = set()
        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            if node == restrictedHouseB:
                return False
            for neighbor in graph[node]:
                queue.append(neighbor)
    return True

def friend_requests_bfs(num_houses, restrictions, requests):
    graph = {i: [] for i in range(num_houses)}
    result = []

    for houseA, houseB in requests:
        if can_be_friends(graph, restrictions, houseA, houseB):
            graph[houseA].append(houseB)
            graph[houseB].append(houseA)
            result.append("approved")
        else:
            result.append("denied")
    
    return result

num_houses1 = 3
restrictions1 = [[0, 1]]
requests1 = [[0, 2], [2, 1]]
print(friend_requests_bfs(num_houses1, restrictions1, requests1))  # Output: ["approved", "denied"]

num_houses2 = 5
restrictions2 = [[0, 1], [1, 2], [2, 3]]
requests2 = [[0, 4], [1, 2], [3, 1], [3, 4]]
print(friend_requests_bfs(num_houses2, restrictions2, requests2))  # Output: ["approved", "denied", "approved", "denied"]
