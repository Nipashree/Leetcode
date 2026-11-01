Ayush is working on a strange algorithm where he wants to convert a string from A to
B, both the strings of equal length N
Below are the rules which can be performed to convert a string
• String A and B are of equal length
• Both of them are in lower case
• Choose a subset X from the string A, between the index 1 and N.
• Let ‘s’ be the letter which alphabetically comes before all other letters in the subset. Let
‘s’ be called the ‘smallest element’ in the subset.
• Replace all the elements of subset with the letter ‘s’
Find the minimum number of moves which is required to perform the conversion. If it
is not possible to convert the string from A to b then return -1
Let us try to understand it with and examples
Suppose there are 2 strings
A = abcab
B = aabab


n = int(input())
a = input()
b = input()
if a == b:
print(1)
res, res2 = "", ""
for x in range(n):
if a[x] != b[x]:
res += a[x]
res2 += b[x]
ans = 0
for i in a:
if ans != 0:
break
if i not in b:
print(-1)
break
else:
for x in set(res2):
if x not in a:
print(-1)
ans += 1
break
else:
print(len(set(res2)))
ans += 1
break
if ans == 1:
break
