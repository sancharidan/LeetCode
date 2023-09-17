class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # smaller_str = str1 if len(str1)<len(str2) else str2
        # bigger_str = str1 if str1!=smaller_str else str2
        # for i in range(len(smaller_str)+1,1,-1):
        #     prefix = smaller_str[:i]
        #     print (prefix)
        #     if bigger_str == "".join([prefix]*int(len(bigger_str)/len(prefix))):
        #         return prefix
        # return ""
        import math
        if str1+str2==str2+str1:
            return str1[:math.gcd(len(str1), len(str2))]
        else:
            return ""