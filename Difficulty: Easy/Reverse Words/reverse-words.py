class Solution:
    def reverseWords(self, s):
        result = ""
        i = len(s) - 1

        while i >= 0:
            # skip dots
            while i >= 0 and s[i] == ".":
                i -= 1

            if i < 0:
                break

            end = i

            # find word
            while i >= 0 and s[i] != ".":
                i -= 1

            word = s[i+1:end+1]

            if result != "":
                result += "."

            result += word

        return result
            
        # code here
        