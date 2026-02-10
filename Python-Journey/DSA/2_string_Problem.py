# class Solution:
#     def biggest_string (self, strs: str ):

#         current_string = ""
#         prev_string = ""
#         updated_string = ""

#         for char in strs:
#             current_string = strs[char]

#             if len(current_string) > len(prev_string):
#                 updated_string = strs[char]
#         return updated_string

# sol = Solution()
# print(sol.biggest_string(["flower","flow","flight"]))


# class Solution:
#    def longestCommonPrefix (self, strs: list ) -> str:
#       if not strs:
#          return ""
    
#       for i in range(len(strs)):
#          char = strs[i]

#          for len(string) in strs[1:]:
#             if i >= len(string) or string[i] != char:
#                return strs[:i]
#       return strs    

# sol = Solution()
# print(sol.longestCommonPrefix(["flower", "flow", "flight"]))

class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        if not strs:
            return ""
        
        answer = ""
        # Compare characters at each position
        for i in range(len(strs)):  # Loop through positions in FIRST string
            char = strs[i]  # Get character at position i from first string
            
            # Check if this character matches in all OTHER strings
            for string in strs[1:]:

                if i >= len(string) or string[i] != char:
                    return strs[0][:i]  # Return prefix up to position i
        
        return strs[:i]  # All characters matched, return entire first string

sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"