class Solution:
    def romanToInt(self, s: str) -> int:
        val = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        s += " " 
        decimal  = 0
        double = False
        
        for i in range(len(s) - 1):
            
            if double:
                double = False
                continue
            elif s[i]+s[i+1] in val.keys():
                decimal += val[s[i]+s[i+1]]
                double = True
            else:
                decimal += val[s[i]]
                
        
        return decimal
            
