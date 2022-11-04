class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output =[]
        
        for i in range(len(nums1)):

            j = nums2.index(nums1[i])
            #print(j)

            if j == len(nums2)-1:
                output.append(-1)

            elif j < len(nums2)-1:

                if nums2[j+1] > nums1[i]:
                    output.append(nums2[j+1])

                while nums2[j+1] <= nums1[i]:
                    j+=1
                    if j == len(nums2)-1:
                        output.append(-1)
                        break

                    if nums2[j+1] > nums1[i]:
                        output.append(nums2[j+1])

        return output
                    
