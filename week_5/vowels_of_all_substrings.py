"""
https://leetcode.com/problems/vowels-of-all-substrings/
"""

class Solution:
    def countVowels(self, word: str) -> int:
        vowels = {"a", "e", "i", "o", "u"}        
        
        # 1 for vowel 0 for consonant
        word = [int(i in vowels) for i in word]
        
        sum_ = 0
        for i in range(len(word) // 2 if len(word) % 2 == 0 else (len(word) + 1) // 2):
            sum_ += word[i] * (i * (i + 1) + (len(word) - i * 2) * (i + 1) )
        
        for i in range(len(word) // 2):
            sum_ += word[len(word) - i - 1] * (i * (i + 1) + (len(word) - i * 2) * (i + 1))
            
        return sum_

    # TLE
    def _countVowels(self, word: str) -> int:
        vowels = {"a", "e", "i", "o", "u"}        
        
        sum_ = 0
        for i in range(1, len(word) + 1):
            vowels_in_substring = 0
            left = right = 0
            while right < len(word):                                    
                if word[right] in vowels:
                    vowels_in_substring += 1
                
                if right - left + 1 == i:
                    sum_ += vowels_in_substring
                    
                    if word[left] in vowels:
                        vowels_in_substring -= 1
                    left += 1                    
                    
                right += 1
        
        return sum_