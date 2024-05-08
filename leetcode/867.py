class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        trans_matrix = []

        for i in range(len(matrix[0])):
            trans_row = []
            for row in matrix:
                trans_row.append(row[i])
            trans_matrix.append(trans_row)
        
        return trans_matrix