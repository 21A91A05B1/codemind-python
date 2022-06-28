class Solution:
   def solve(self, s1, s2):
       s1 = s1.lower()
       s2 = s2.lower()
       s1List = s1.split(" ")
       s2List = s2.split(" ")
       return len(list(set(s1List)&set(s2List)))
ob = Solution()
S = input()
T = input()
print(ob.solve(S,T))