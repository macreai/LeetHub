class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        saved_nodes = set()

        for edge in edges:
            for node in edge:
                if node in saved_nodes:
                    return node
                saved_nodes.add(node)
            
        