class Solution:
    def sortSentence(self, s: str) -> str:
        
        
        output = ""


        num = 1
        i = 0
        while i < len(s):
            temp = ""
            if s[i] == str(num):
                i -= 1
                while s[i] != " " and i != -1:
                    temp += s[i]
                    i -= 1
                #print("temp is:",temp)
                for j in range(len(temp)-1, -1, -1):
                    output += temp[j]

                output += " "
                #print (output)



                num += 1
                #print(num)
                if num > len(s):
                    #print("num is greater than length of string")
                    break
                else:
                    #print("reset")
                    i = 0
                    #print("-",i)
            i += 1

        output = output.rstrip(" ")
        #print("final", output)
        return output
