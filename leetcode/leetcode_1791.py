# 1791. Find Center of Star Graph
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        candidate_node = edges[0][0]
        if edges[1][0] == candidate_node or edges[1][1] == candidate_node:
            return candidate_node
        else:
            return edges[0][1]
