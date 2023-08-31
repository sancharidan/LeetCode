class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        sorted_strs = sorted(strs)
        if len(sorted_strs)==1:
            return sorted_strs[0]
        if sorted_strs[0]=="":
            return ""
        for i in range(len(sorted_strs[0])):
            if sorted_strs[0][i]==sorted_strs[-1][i]:
                prefix = prefix + sorted_strs[0][i]
            else:
                return prefix
        return prefix