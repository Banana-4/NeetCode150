class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        turns = lambda i: (target - position[i]) / speed[i]
        sorted_positions = sorted(range(len(position)), key=lambda i: position[i], reverse=True)
        groups = [sorted_positions[0]]
        for i in sorted_positions[1:]:
            if turns(i) > turns(groups[-1]):
                groups.append(i)
        return len(groups)
