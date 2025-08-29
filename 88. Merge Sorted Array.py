class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            nums1.sort()
            nums1.append(0)
            nums1.sort()

        if len(nums1) == m and len(nums2) == n:

         for i in range(0,len(nums2)):
            nums1.append(nums2[i])
        
         nums1.sort()

         if 0 in nums1:
             while 0 in nums1:
                 nums1.remove(0)
        
        elif len(nums1) != m and len(nums2) == n:

            for i in range(len(nums1)-m):
                nums1.remove(0)
            
            for i in range(0,len(nums2)):
              nums1.append(nums2[i])
        
            nums1.sort() 
        
        elif len(nums1) == m and len(nums2) != n:

            for i in range(len(nums2)-n):
                nums1.remove(0)
            
            for i in range(0,len(nums2)):
              nums1.append(nums2[i])
        
            nums1.sort() 


# Time Complexity: O((m+n)²) worst case
# Space Complexity: O(1) average, O(m+n) worst case
