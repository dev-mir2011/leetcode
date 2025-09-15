class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        cto = {")":"(", "]":"[", "}":"{"}


        for c in s:
            if c in cto:
                if st and st[-1] == cto[c]:
                 st.pop()

                
                else:
                    return False

            else:
                st.append(c)

        
        return True if not st else False



# Time Complexity: O(n)
# pace Complexity: O(n)
