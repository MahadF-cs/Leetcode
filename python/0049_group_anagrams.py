class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for word in strs:
            curr = "".join(sorted(word))
            if curr in anagrams:
                anagrams[curr].append(word)
            else:
                anagrams[curr] = []
                anagrams[curr].append(word)
        ans = []
        for group in anagrams:
            ans.append(anagrams[group])
        return ans
            
        
