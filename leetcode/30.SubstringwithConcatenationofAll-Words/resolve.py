class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        def occurence(chaine):
            o = {}
            for c in chaine:
                if c in o:
                    o[c] += 1
                else:
                    o[c] = 1     
            return o
        
        occ_words = occurence(words)
        len_window = len(words) * len(words[0])
        start = 0
        end = len_window
        souschaine = []

        while end <= len(s):
            ch = s[start:end]
            ch = [ch[i:i+len(words[0])] for i in range(0, len(ch), len(words[0]))]
            if occ_words == occurence(ch):
                souschaine.append(start)
            end += 1
            start += 1

        return souschaine

def main():
    s = Solution()
    print(s.findSubstring("barfoothefoobarman", ["foo", "bar"]))  # Attendu: [0, 9]
    print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))  # Attendu: []
    print(s.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))  # Attendu: [6,9,12]
    print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))  # Attendu: [8]
    print(s.findSubstring("ababaab", ["ab","ba","ba"]))  # Attendu: [1]

if __name__ == "__main__":
    main()


