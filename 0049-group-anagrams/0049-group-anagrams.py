class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         copy_strs = strs
#         index_arr = list(range(0, len(strs)))
        
#         copy_strs = ["".join(sorted(str)) for str in copy_strs]
#         copy_strs = [(copy_strs[i], i) for i in index_arr]
#         copy_strs = sorted(copy_strs)
#         print(strs, index_arr, copy_strs)
#         return [strs[j]]
        
        from collections import defaultdict
        anagram_dict = defaultdict(list)
        for word in strs:
            anagram_dict["".join(sorted(word))].append(word)
        return [l for l in (anagram_dict.values())]