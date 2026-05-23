class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = "".join(char.lower() for char in s if char.isalnum())
        print(cleaned_text)

        i, j = 0, len(cleaned_text)-1
        while i < j:
            if cleaned_text[i] != cleaned_text[j]:
                return False
            
            i += 1
            j -= 1


            
        return True
        