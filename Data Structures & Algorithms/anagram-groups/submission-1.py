class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we will create a placeholder dict
        res = {}
        # We will iterate thorugh given string
        for s in strs: 
        # we will set up an count list which have 
        # the length of 26 for each char for a-z placeholder will be zero
            count = [0] * 26
        # we will again iterate over element of string char wise
            for char in s:
        # we will calculate ord value of char and append it to count
                count[ord(char)-ord("a")] += 1
        # we will create a key as tuple of count to make it immutable
            key = tuple(count)
        # check if key is present in result dict if not then we will create a placeholder list
            if key not in res:
                res[key] = []
        # we will add key and add element to the dict as value
            res[key].append(s)
        # then we will return values of result dictionary
        return res.values()