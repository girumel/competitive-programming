# Problem: Validate Binary Tree Nodes - https://leetcode.com/problems/validate-binary-tree-nodes/

root = [i for i in range(n)]
        
        for i in range(n):
            if leftChild[i] != -1:
                if leftChild[i] in root:
                    root.remove(leftChild[i])
                else:
                    return False
            if rightChild[i] != -1:
                if rightChild[i] in root:
                    root.remove(rightChild[i])
                else:
                    return False
                
        if len(root) != 1:
            return False
        
        def dfs(node):
            if node == -1:
                return 0
            return 1 + dfs(leftChild[node]) + dfs(rightChild[node])
        
        return dfs(root[0]) == n