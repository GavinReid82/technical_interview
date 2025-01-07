def solution(buckets):
    def calculate_moves(balls, target_positions):
        # Calculate the total moves to align balls with target positions
        return sum(abs(b - t) for b, t in zip(balls, target_positions))

    # Get the positions of the balls
    balls = [i for i, c in enumerate(buckets) if c == 'B']
    n = len(balls)
    total_buckets = len(buckets)

    # If there are more balls than a valid pattern can handle, return -1
    max_possible_balls = (total_buckets + 1) // 2
    if n > max_possible_balls:
        return -1

    # Generate valid patterns dynamically
    target_even = list(range(0, total_buckets, 2))[:n]  # Balls on even indices
    target_odd = list(range(1, total_buckets, 2))[:n]   # Balls on odd indices

    # Calculate moves for both patterns
    moves_even = calculate_moves(sorted(balls), target_even)
    moves_odd = calculate_moves(sorted(balls), target_odd)

    # Return the minimum moves required
    return min(moves_even, moves_odd)


# Test cases:
print(solution("..B....B.BB"))  # Expected: 2
print(solution("BB.B.BBB..."))  # Expected: 4
print(solution(".BBB.B"))       # Expected: -1
print(solution("......B.B"))    # Expected: 0
print(solution("B..B"))         # Expected: 1
