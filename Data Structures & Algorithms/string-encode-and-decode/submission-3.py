class Solution:
    '''
    for encoding, using for loop in given str length of word is added at front with '#' 
so that their will be a delimiter and then word itself add to res empty string
for decoding we will initiate i for checking position of word
then in while loop with condition as i is less than length of word
we will define another pointer j equal to i
inside of while we will define another while loop with condition that str[j] is not equal to '#'
this while loop will give us the length of word by j += 1
now define length as int(str[i:j]) this will give us length of word
now we have to move in string to till length by doing this j+1: j+1+length this will give length of word
now increase i will j+1+length then return the res list
    '''
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res

