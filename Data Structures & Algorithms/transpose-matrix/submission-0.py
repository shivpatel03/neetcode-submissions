class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # temp = [0] * len(matrix)
        # result = [temp] * len(matrix[0])
        result = []
        for i in range(len(matrix[0])):
            result.append([0] * len(matrix))


        # print(result)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                result[j][i] = matrix[i][j]
                print(result)

        return result