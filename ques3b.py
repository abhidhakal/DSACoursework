# Imagine you are managing a bus service with passengers boarding at various stops along the route. Your task is to
# optimize the boarding process by rearranging the order of passengers at intervals of k stops, where k is a positive
# integer. If the total number of passengers is not a multiple of k, then the remaining passengers at the end of the route
# should maintain their original order.

def optimize_boarding_in_place(head, k):
    n = len(head)

    for i in range(0, n, k):
        left = i
        right = min(i + k - 1, n - 1)
        while left < right:
            head[left], head[right] = head[right], head[left]
            left += 1
            right -= 1

    return head

h1 = [1, 2, 3, 4, 5]
k1 = 2
print(optimize_boarding_in_place(h1, k1))  # Output: [2, 1, 4, 3, 5]
