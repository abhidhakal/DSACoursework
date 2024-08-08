# Question: Imagine you're a scheduling officer at a university with n classrooms numbered 0 to n-1. Several different courses
# require classrooms throughout the day, represented by an array of classes classes[i] = [starti, endi], where starti is
# the start time of the class and endi is the end time (both in whole hours). Your goal is to assign each course to a
# classroom while minimizing disruption and maximizing classroom utilization. Here are the rules:
# • Priority Scheduling: Classes with earlier start times have priority when assigning classrooms. If multiple
# classes start at the same time, prioritize the larger class (more students).
# • Dynamic Allocation: If no classroom is available at a class's start time, delay the class until a room
# becomes free. The delayed class retains its original duration.
# • Room Release: When a class finishes in a room, that room becomes available for the next class with the
# highest priority (considering start time and size).
# Your task is to determine which classroom held the most classes throughout the day. If multiple classrooms are
# tied, return the one with the lowest number.

def find_most_used_classroom(n, classes):
    # Sorting all classes by its starting time and no. of students if they have same starting time
    classes.sort(key=lambda x: (x[0], -x[2]))
    
    # Initializing the list to track if room is available
    room_class_endtime = [0] * n  # When each room will be free
    room_count = [0] * n     # No. of classes each room handles
    
    for start, end, students in classes:
    
        earliest_room = 0
        for i in range(1, n):
            if room_class_endtime[i] < room_class_endtime[earliest_room]:
                earliest_room = i
        
        # If the room is free by the start time, assign the class to that room
        if room_class_endtime[earliest_room] <= start:
            room_class_endtime[earliest_room] = end
        else:

            room_class_endtime[earliest_room] += (end - start)

        room_count[earliest_room] += 1
    
    # Finding the most utilized room
    max_classes = max(room_count)
    for i in range(n):
        if room_count[i] == max_classes:
            return i

# Example Usage
n1 = 2
classes1 = [[0, 10, 30], [1, 5, 25], [2, 7, 20], [3, 4, 10]]
print(find_most_used_classroom(n1, classes1))  # Output: 0

n2 = 3
classes2 = [[1, 20, 30], [2, 10, 25], [3, 5, 20], [4, 9, 15], [6, 8, 10]]
print(find_most_used_classroom(n2, classes2))  # Output: 1


