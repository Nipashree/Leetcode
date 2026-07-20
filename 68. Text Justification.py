class Solution:
    def fullJustify(self, words, maxWidth):

        result = []
        i = 0

        while i < len(words):

            line = []
            length = 0

            # Add words until the line is full
            while i < len(words) and length + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                length += len(words[i])
                i += 1

            # Last line or only one word
            if i == len(words) or len(line) == 1:
                s = " ".join(line)
                s += " " * (maxWidth - len(s))
                result.append(s)

            else:
                gaps = len(line) - 1
                spaces = maxWidth - length

                each = spaces // gaps
                extra = spaces % gaps

                s = ""

                for j in range(gaps):
                    s += line[j]
                    s += " " * each

                    if extra > 0:
                        s += " "
                        extra -= 1

                s += line[-1]
                result.append(s)

        return result
