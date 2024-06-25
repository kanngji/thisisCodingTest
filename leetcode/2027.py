class Solution:
    def minimumMoves(self, s: str) -> int:
        n = len(s)
        i = 0
        moves = 0
        
        while i < n:
            if s[i] == 'X':
                moves += 1
                i += 3
            else:
                i += 1
        
        return moves
    
# ...?