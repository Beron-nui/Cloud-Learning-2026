class Solution:
    def Roman_to_integer(self, symbol:str):
        dict_symbol = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000

        }
        
        total = 0
        prev_value = 0

        for char in reversed(symbol):
            current_value = dict_symbol[char]

            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            
            prev_value = current_value

        return total  
                
                
sol = Solution()
print(sol.Roman_to_integer("MCD"))           

