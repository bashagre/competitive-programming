class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        
        interval = sorted(intervals)
        #print(interval)
        output = []

        output.append(interval[0])

        i = 1
        while i<len(interval):
            x = output[-1]
            
            if output[-1][1] >= interval[i][0]:
                if output[-1][1] >= interval[i][1]:
                    output.append(output[-1])
                    output.pop(-2)

                    i+=1
                else:

                    output.append( [ output[-1][0] , interval[i][1] ] )
                    output.pop(-2)
                    #print(output)
                    i+=1
            else:
                output.append(interval[i])
                #print(output)
                i+=1
        return output
