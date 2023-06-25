# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root==None):
            return []

        queue=deque()
        queue.append(root)
        result=[]
        while(len(queue)):
            current_level_length=len(queue)
            current_level_elements=[]
            for i in range(current_level_length):
                current_element=queue.popleft()
                current_level_elements.append(current_element.val)
                if current_element.left:
                    queue.append(current_element.left)
                if current_element.right:
                    queue.append(current_element.right)
            result.append(list(current_level_elements))
        return result
                

        