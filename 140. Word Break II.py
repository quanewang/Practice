class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_list = []
        if s == "":
            return [""]

        for i in range(len(s)):
            word = s[0:i + 1]

            if word in wordDict:
                valid_phrases = self.wordBreak(s[i + 1: len(s)], wordDict)

                if valid_phrases is not None:
                    for v_p in valid_phrases:
                        phrase = word
                        if v_p != "":
                            phrase = phrase + " " + v_p
                        word_list.append(phrase)

        return word_list
