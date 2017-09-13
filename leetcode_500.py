class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        result = []
        flags = []
        for word in words:
            lowerword = word.lower()
            if lowerword[0] in rows[0]:
                flags = [ch in rows[0] for ch in lowerword]
            elif lowerword[0] in rows[1]:
                flags = [ch in rows[1] for ch in lowerword]
            elif lowerword[0] in rows[2]:
                flags = [ch in rows[2] for ch in lowerword]
            if not False in flags:
                result.append(word)
        return result