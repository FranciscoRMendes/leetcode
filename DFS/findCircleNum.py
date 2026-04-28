class Solution:
    def dfs(self, node, isConnected, visit):
        visit[node] = True
        for i in range(len(isConnected)):
            if isConnected[node][i] and not visit[i]:
                self.dfs(i, isConnected, visit)

    def findCircleNum(self, isConnected):
        size = len(isConnected)
        numberOfComponents = 0
        visit = [False] * size

        for i in range(size):
            if not visit[i]:
                numberOfComponents += 1
                self.dfs(i, isConnected, visit)

        return numberOfComponents


if __name__ == '__main__':
    sol = Solution()
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(sol.findCircleNum(isConnected))
