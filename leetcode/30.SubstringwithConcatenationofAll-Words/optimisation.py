from collections import Counter
class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        wordBag = Counter(words)   # Compter les occurences des mots dans words
        wordLen, numWords = len(words[0]), len(words)
        totalLen, res = wordLen*numWords, []
        for i in range(len(s) - totalLen + 1):   # Parcourir s
            # Capture la sous-chaîne et la divise en liste de mots
            seen = [s[i+j*wordLen:i+j*wordLen+wordLen] for j in range(numWords)]
            if Counter(seen) == wordBag:   # Comparer les occurences
                res.append(i)   # Ajouter le début de la sous-chaîne à la liste des résultats
        return res

def main():
    s = Solution()
    print(s.findSubstring("barfoothefoobarman", ["foo", "bar"]))  # Attendu: [0, 9]
    print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))  # Attendu: []
    print(s.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))  # Attendu: [6,9,12]
    print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))  # Attendu: [8]
    print(s.findSubstring("ababaab", ["ab","ba","ba"]))  # Attendu: [1]

if __name__ == "__main__":
    main()
