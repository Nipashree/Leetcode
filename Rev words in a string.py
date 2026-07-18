
Code1:
# class Solution:
#     def reverseWords(self, s):
        
#         words = s.split()
#         words.reverse()
        
#         return " ".join(words)

Code2:
class Solution:
    def reverseWords(self,s):
        return " ".join(s.split()[::-1])
