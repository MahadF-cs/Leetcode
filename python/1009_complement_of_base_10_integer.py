class Solution:
    def bitwiseComplement(self, n: int) -> int:
        comp = ''
        
        for char in str(bin(n))[2:]:
            if char == '0':
                comp += '1'
            else:
                comp += '0'
        
        return int(comp, 2)