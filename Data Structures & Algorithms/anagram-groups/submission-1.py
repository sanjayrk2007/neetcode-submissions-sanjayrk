class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            sor="".join(sorted(s))
            res[sor].append(s)
        return list(res.values())