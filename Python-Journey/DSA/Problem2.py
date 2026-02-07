class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        text_x = str(x)
        reversed_x = "".join(reversed(text_x))
        print(f"reverse of x: {reversed_x}")

        if text_x == reversed_x:
            return True
        else:
            return False
        
sol = Solution()
print(sol.isPalindrome(-212))
