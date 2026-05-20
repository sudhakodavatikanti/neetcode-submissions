class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        my_dict_1 = {}
        my_dict_2 = {}

        for item in s:
            my_dict_1[item] = my_dict_1.get(item, 0) + 1

        for item in t:
            my_dict_2[item] = my_dict_2.get(item, 0) + 1

        for item in my_dict_1:
            if item not in my_dict_2 or my_dict_1.get(item) != my_dict_2.get(item):
                return False 
            
        return True

        