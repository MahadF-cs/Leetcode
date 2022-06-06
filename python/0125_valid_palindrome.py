class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(ch for ch in s if ch.isalnum()).lower()
        i = 0
        j = len(cleaned) - 1
        
        while i < j:
            if cleaned[i] != cleaned[j]:
                return False
            i += 1
            j -= 1
        return True
