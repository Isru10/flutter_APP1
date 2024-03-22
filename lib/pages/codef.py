"""n=int(input())
arr=list(map(int,input().split()))
even=[]
odd=[]
for i in arr:
    if i%2==0:
        even.append(i) 
    else:
         odd.append(i) 
even.sort(reverse=True)
odd.sort(reverse=True)
if abs(len(even)-len(odd))<=1:
    print(0)
elif len(even)>len(odd):
    print(sum(even[len(odd)+1:]))
else:
        print(sum(odd[len(even)+1:]))
        """
'''n=int(input())
arr=list(map(int,input().split()))
crr=0
mxlen=0
for i in range(2*n):
    if arr[i%n]==1:
        crr+=1
        mxlen=max(mxlen,crr)
    else:
        crr=0
print(mxlen)'''
'''5
1 0 1 0 1'''
'''n=int(input())
arr=list(map(int,input().split()))
if n<=2:
    print(0)
else:
    arr.sort()
    arr.pop()
    print(max(arr)-min(arr))'''
'''l=input()
l2=l.replace(' ','')
vowel=['A', 'E', 'I', 'O', 'U', 'Y']
consonant=[ 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
lst=l2[-2].upper()
if lst in vowel:
    print("YES")
if lst in consonant:
    print("NO")

'''
s=input()
s2=input()
if s[::-1]==s2:
    print("YES")
else:
    print("NO")