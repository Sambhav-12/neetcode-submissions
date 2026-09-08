class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for string in strs:
            s = str(len(string))
            encoded = s + "#" + string
            encode += encoded
        return encode

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            delimiter = s.find("#", i)
            l = s[i:delimiter]
            integer = int(l)
            st = s[(delimiter + 1) : (delimiter + 1 + integer)]
            result.append(st)
            i = (delimiter + 1 + integer)
        return result



