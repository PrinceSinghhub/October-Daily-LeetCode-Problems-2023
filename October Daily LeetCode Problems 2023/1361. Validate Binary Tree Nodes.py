from collections import deque


class Solution:
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        isChild = [0] * n
        for x in range(n):
            if leftChild[x] != -1:
                isChild[leftChild[x]] = 1
            if rightChild[x] != -1:
                isChild[rightChild[x]] = 1

        root = -1
        for x in range(n):
            if not isChild[x]:
                root = x
                break

        if root == -1:
            return False

        q = deque()
        q.append(root)
        vis = set()

        while q:
            node = q.popleft()
            if node in vis:
                return False
            vis.add(node)
            if leftChild[node] != -1:
                q.append(leftChild[node])
            if rightChild[node] != -1:
                q.append(rightChild[node])

        return len(vis) == n
