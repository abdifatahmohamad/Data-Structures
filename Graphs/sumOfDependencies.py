# User function Template for python3
from collections import defaultdict
# Sum of dependencies in a graph : https://practice.geeksforgeeks.org/problems/sum-of-dependencies-in-a-graph5311/1?page=1&category[]=Graph&sortBy=difficulty


class Solution:
    def sumOfDependencies(self, adj, V):
        # Solution 1
        # array size of v
        indirect = [0 for _ in range(V)]
        for edge in adj:
            indirect[edge[0]] += 1
        print(indirect)
        res = 0

        for n in indirect:
            res += n
        return res

        '''
            # Solution 2
            adjacency = defaultdict(list)
            for src, des in adj:
                adjacency[src].append(des)
            res = 0
            for k in adjacency:
                res += len(adjacency.get(k))
            return res
        '''


adj = [[0, 2], [0, 3], [1, 3], [2, 3]]
'''
indirect = [2,1,1,1]
edge = [3,1]
edge[0] = 4
indirect[3] += 1
'''
res = Solution().sumOfDependencies(adj, 4)
print(res)
