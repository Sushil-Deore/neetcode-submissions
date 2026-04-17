# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quicksorthelper(pairs, 0, len(pairs)-1)
        return pairs

    def quicksorthelper(self, pairs, s, e):    
        
        # base case
        if e - s + 1 <= 1: return

        # Pivot assignment
        pivot = pairs[e]

        # Pointer assignment
        left = s

        # Partition: Elements smaller than pivot on left side
        for i in range(s, e):
            if pairs[i].key < pivot.key:
                temp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = temp
                left += 1

        # Move pivot in-between left and right sides
        pairs[e] = pairs[left]
        pairs[left] = pivot

        # quick sort left side
        self.quicksorthelper(pairs, s, left -1)

        # Quick sort right side
        self.quicksorthelper(pairs, left+1, e)

        return pairs

