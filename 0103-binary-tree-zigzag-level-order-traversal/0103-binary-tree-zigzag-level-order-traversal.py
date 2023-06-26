# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root==None:
            return []
        queue=deque()
        level=0
        queue.append(root)
        result=[]
        
        while (len(queue)):
            current_level_len=len(queue)
            current_level_ele=deque()
            for _ in range(current_level_len):
                current_element=queue.popleft()
                if(level%2==0):
                    current_level_ele.append(current_element.val)
                else:
                    current_level_ele.appendleft(current_element.val)
                
                if current_element.left:
                    queue.append(current_element.left)
                if current_element.right:
                    queue.append(current_element.right)
                    
            result.append(list(current_level_ele))
            level+=1
        return result
            
                
        
                
                
                
        
        