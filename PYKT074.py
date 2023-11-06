# t = int(input())
# while t>0:
#     t-=1
#     s = str(input())
#     if len(s)<=100:
#         print(s)
#     else:
#         s = s[:101]
#         for i in range(100,0,-1):
#             if s[i] == ' ':
#                 print(len(s[:i]))
#                 break
import textwrap

t = int(input())
for i in range(t) :
    print(textwrap.shorten(input(), width = 100, placeholder = ''))