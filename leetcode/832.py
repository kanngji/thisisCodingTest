class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        m = len(image[0]) if n > 0 else 0

        for i in range(n):
            image[i] = image[i][::-1]
            for j in range(m):
                image[i][j] = 1 - image[i][j]

        return image
    
# 2차원 배열 연습하기
    