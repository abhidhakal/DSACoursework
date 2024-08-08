# Imagine you have a secret decoder ring with rotating discs labeled with the lowercase alphabet. You're given a
# message s written in lowercase letters and a set of instructions shifts encoded as tuples (start_disc, end_disc,
# direction). Each instruction represents rotating the discs between positions start_disc and end_disc (inclusive)
# either clockwise (direction = 1) or counter-clockwise (direction = 0). Rotating a disc shifts the message by one
# letter for each position moved on the alphabet (wrapping around from ‘z’ to ‘a’ and vice versa).
# Your task is to decipher the message s by applying the rotations specified in shifts in the correct order.

def rotate(c, direction):
    # Rotate the character clockwise
    if direction == 1:
        return chr((ord(c) - ord('a') + 1) % 26 + ord('a'))
    # Rotate the character counter-clockwise
    elif direction == 0:
        return chr((ord(c) - ord('a') - 1) % 26 + ord('a'))

def apply_shifts(s, shifts):
    # String to List
    s = list(s)
    
    # Applying each shift
    for start, end, direction in shifts:
        for i in range(start, end + 1):
            s[i] = rotate(s[i], direction)
    
    # List to String
    return ''.join(s)

s = "hello"
shifts = [[0, 1, 1], [2, 3, 0], [0, 2, 1]]
result = apply_shifts(s, shifts)
print(result)  # Output: "jglko"
