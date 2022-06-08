class Solution:
    def reverseBits(self, n: int) -> int:
        formatted_binary='{0:032b}'.format(n)
        reverse = formatted_binary[::-1]
        return int(reverse , 2)
