from collections import deque
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue=deque()
        queue.append(root)
        level=-1
        while queue:
            l=len(queue)
            level+=1
            li=[]
            for _ in range(l):
                pop=queue.popleft()
                if level%2==0:
                    if pop.val%2==0:
                        return False
                    else:
                        if len(li)>0 and li[-1]>=pop.val:
                            return False
                        else:
                            li.append(pop.val)
                else:
                    if pop.val%2!=0:
                        return False
                    else:
                        if len(li)>0 and li[-1]<=pop.val:
                            return False
                        else:
                            li.append(pop.val)
                if pop.left:
                    queue.append(pop.left)
                if pop.right:
                    queue.append(pop.right)
        return True
            
                    

        