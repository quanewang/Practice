class Solution:
    def wordBreak(self, s: str, word_dict):
        word_list = []
        if s == "":
            return [""]

        for i in range(len(s)):
            word = s[0:i + 1]

            if word in word_dict:
                valid_phrases = self.wordBreak(s[i + 1: len(s)], word_dict)

                if valid_phrases is not None:
                    for v_p in valid_phrases:
                        phrase = word
                        if v_p != "":
                            phrase = phrase + " " + v_p
                        word_list.append(phrase)

        return word_list
