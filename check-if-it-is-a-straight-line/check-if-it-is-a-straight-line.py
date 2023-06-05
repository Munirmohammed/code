class Solution:
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        x0,y0=c[0][0],c[0][1]
        x1,y1=c[1][0],c[1][1]
        for i in range(2, len(c)):
            x,y=c[i][0],c[i][1]
            if(x-x0)*(y1-y0)!=(y-y0)*(x1-x0):return False
        return True