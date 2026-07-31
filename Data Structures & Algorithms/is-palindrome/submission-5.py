class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(c.casefold() for c in s if c.isalnum())
        print(cleaned)
        i, j = 0, len(cleaned)-1
        while i <= j:
            if cleaned[i] != cleaned[j]:
                return False
            else:
                i += 1
                j -= 1

        return True
        