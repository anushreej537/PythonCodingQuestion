# str='sdjfhdsjkfhdsjkf^%^&%^&%$%^$%^$!@#$%^&*(7656646545645646313213'
# t=''
# s=[]
# for i in str:
#     if i.isdigit():
#         t=t+i
# for j in t:
#     s.append(j)
# print(s)
#
#
# str1='anushree'
# str2='joshi'
# t={}
#
# t.update({str1:str2})
# print(t)
#
#
# str1='anushreEEEEEe'
# v='aeiou'
# c=0
# # for i in v:
# #     if i in str1:
# #         c=c+1
# # print(c)
# for i in str1:
#     if i in v:
#         c=c+1
# print(c)
# d={}
# d['vowel_count']=c
# print(d)
#
#
# num=int(input('enter a num'))
# if num==0 or num==1:
#     print(num,' not prime')
# else:
#     for i in range(2,num):
#         if num%i==0:
#             print(num,' not prime')
#             break
#
#     else:
#         print(num,'prime')
# # ------------------------------------------------------------
#
# s='google.com'
# d={}
# l=[]
# for i in s:
#     v=l.count(i)
#     d[i]=v+int(i)
# print(d)


# g:1 o=2
# d = {}
# for i in s:
#     if i in d:
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1
# print(d)


# def word(s):
#
#     t = {}
#     f = ''
#     for i in s:
#         if i in t:
#             t[i] = t[i] + 1
#         else:
#             t[i] = 1
#     return t
# print(word('goooooooooooosdfdsfsdbsahdgahgahgdhasgdj'))

# s='anu is a good girl .'
# t=s.split(' ')
# s=''
# for i in t[::-1]:
#     if i!='.':
#         s=s+' '+i
# s=s+t[len(t)-1]
# print(s)

# output='girl good a is anu.'

# n=5
# s=0
# for i in range(n+1):
#     s=s+i
#
# print(s)

# N=[1,2,3,4,5]
# S=5
# for i in range(len(N)):
#     for j in range(i+1,len(N)):
#         if N[i]+N[j] == S:
#             print('true',N[i],N[j])
#         else:
#             pass
# ===============================================

# def name(s):
#     t = s.split(' ')
#     l = len(t[0])
#     print(l)
#     k = t[0]
#     for i in t:
#         if len(i)>l:
#             l=len(i)
#             k=i
#     return l,k

# s = 'sh raju an mes dsa dasddhsgdhjsghgsjdf asd sdfd'
# s=s.split()
# d={}
# for i in s:
#     v=len(i)
#     d[v]=i
# print(d)
# print(max(d.items()))
# v=max(d)
# print(v,d[v])
# print(d.keys())


# s=[2,3,4,2,0,0,4,5,6,0,5,0,4,5,6]
# z=[]
# n=[]
# for i in s:
#     if i>0:
#         n.append(i)
#     else:
#          z.append(i)
#
# n.extend(z)
# print(n)


# s=[2,3,4,2,0,0,4,5,6,0,5,0,4,5,6]
# z=[]
# k=[]
# # b=[z.append(i) for i in s if i>0 else  ]
# l1=[i for  i in s if i==0]
# l2=[j for j in s if j!=0]
# print(l2+l1)

# lst=[]
# for i in s:
#     if i>0:
#         lst.append(i)
#     elif i==0:
#         length=len(lst)
#         lst.append(lst.index(length,i))
#         # lst.remove(i)
# print

# s = [2, 3, 4, 2, 0, 0, 4, 5, 6, 0, 5, 0, 4, 5, 6]
# for i in range(len(s)):
#     for j in range(i+1,len(s)):
#         if s[i]>s[j]:
#             s[i],s[j]=s[j],s[i]
#
# print(s)
# l=[0,2,3,4,5,6,'2','2']

# s = [2, 3, 4, 2, 0, 0, 4, 5, 6, 0, 5, 0, 4, 5, 6]
# t=[]
# p=[]
# for i in s:
#     if i in t:
#         p.append('*')
#     else:
#         t.append(i)
#
# t.extend(p)
# print(t)

# s=['the','quick','brown','fox','quick','fox']
# f='the'
# f1='fox'
# for i in range(len(s)):
#     if s[i]==f1:
#         print(s.index(s[i]),s[i])


# s=[15, 21, 3, 12, 5]
# N=5
# for i in s:
#     if s.index(i)+1 == i:
#         print(i)

# s=[1,2,3,4,5]
# g=[]
# for i in range(0,len(s),2):
#     g.append(s[i])
# print(g)

# def fun(n):
#     if n>=-1:
#         fun(n-1)
#         print(n)
#
# fun(5)

# def palin(n):
#     a=0
#     l=len(n)
#     n=int(n)
#     t=n
#     while n>0:
#         r=n%10
#         a=a*10+r
#         n=n//10
#     if t==a:
#         return 'palin'
#     else:
#         return 'not'
# print(palin('123'))

# n='121'
# s=n[len(n)-1::-1]
# if n==s:
#     print('palin')
# else:
#     print('not')


# s=[1,2,3,4,5]
# n=len(s)//2
# print(s[n])


# def arm(n):
#     l=len(n)
#     n=int(n)
#     t=n
#     a=0
#     while n>0:
#         r=n%10
#         a=a+r**l
#         n=n//10
#     if a==t:
#         return 'arm'
#     else:
#         return 'not'
# print(arm('1634'))

# check a num is binary or not
# def bin_num(n):
#     for i in range(len(n)):
#         for j in range(i+1,len(n)):
#             if n[i]==0 or n[i]==1 or n[j]==0 or n[j]==1:
#                 return 'true'
#             else:
#                 return 'false'
# print(bin_num('101'))

# n=101
# s=[]
# while n>0:
#     r=n%10
#     if r==0 or r==1:
#         s.append(str(r))
#     else:
#         pass
#     n=n//10
# print(s)
# s1=''.join(s)
# print(s1)
# n=str(n)
#
# if len(s1)!=len(n):
#     print('bin')
# else:
#     print('not bin')

# Given an sorted array A of size N. Find number of elements which are less than or equal
# to given element X.
# n=[1,2,4,5,8,10]
# x=9
# s=0
# for i in n:
#     if i<=x:
#         s=s+1
# print(s)

# n=[1,2,3,4]
# s=0
# for i in n:
#     s=s+i
# print(s)


# You are given an integer N, reverse the digits of given number N, ensuring that the reversed number
# has no leading zeroes. Return the resulting reversed number.
# n=124
# s=''
# while n>0:
#     r=n%10
#     s=s+str(r)
#     n=n//10
# print(s)


# Given an array arr of size n, swap the kth element from the beginning with kth element from the end.
# a=[1,2,3,4,5,9,7,8,18,11,12]
# k=2
# p=a[k]
# s=a[-(k+1)]
# print(p)
# print(s)


# Given a list of names, display the longest name. If there are multiple names of the longest size then
# return the first occurring name .
# v=['anushree','anamika','cow']
# l=len(v[0])
# nm=v[0]
# for i in v:
#     if len(i)>l:
#         l=len(i)
#         nm=v[i]
# print(l)
# print(nm)

# Given two positive integers a and b, find GCD of a and b.( "gcd" stands for the
# "greatest common divisor" of two numbers)
# when we do lcm then 6 is common in both
# a=12
# b=18
# c=[]
# d=[]
# for i in range(1,100):
#     if b%i==0:
#         c.append(i)
#     if a%i==0:
#         d.append(i)
# g=c[0]
# for i in c:
#     if i in d:
#         if i>g:
#             g=i
# print(c)
# print(d)
# print(g)

# Given a string s. The task is to convert characters of string to lowercase.
# a='ABSUDYE'
# print(a.lower())

# Given an array arr of n integers and an index key(0-based index). Your task is to return the element
# present at the index key in the array.
# a=[1,2,3,4,5]
# k=4
# for i in range(len(a)):
#     if i==k:
#         print(a[i])

# Given a string, remove spaces from it.
# a='this is my book'
# s=''
# for i in a:
#     if i!=' ':
#         s=s+i
# print(s)


# Given two integers, n and m. The task is to check the relation between n and m.
# n1=int(input('enter first num'))
# n2=int(input('enter second num'))
# if n1>n2:
#     print(n1,' is greater')
# elif n1<n2:
#     print(n1,' is lesser')
# elif n1==n2:
#     print('both are equal')


# Given a positive integer N, determine whether it is odd or even
# n=int(input('enter a num'))
# if n%2==0:
#     print(n,' is even')
# else:
#     print(n,' is odd')


# addition of two num
# def fun(a,b):
#     return a+b
# print(fun(2,3))


# Given a sorted array Arr of size N and a value X, find the number of array elements less than or equal
# to X and elements more than or equal to X.
# a=[1,2,3,5,6,7,8,9]
# x=7
# g=[]
# for i in a:
#     if i<x or i==x:
#         g.append(i)
# print(g, 'which is less than ',x)


# t=(('a','b'),('c','d'))
# d={i[0]:j for i in t for j in i}
# print(d)
# d={}
# for i in t:
#     for j in i:
#         # print(j)
#         d[i[0]]=j
# print(d)


# Given a string s , return reverse of the string as output.
# s="GeeksforGeeks"
# print(s[::-1])


# two to three greatest number or arrange in sorted order(ascending)
# def greatest_num(n):
#     for i in range(len(n)):
#         for j in range(i+1,len(n)):
#             if n[i]>n[j]:
#                 n[i],n[j]=n[j],n[i]
#     return n[:4]
# n=[2,8,7,1,5]
# print(greatest_num(n))

# Create the multiplication table of a given number N and return the table as an array.
# def table_of_num(n):
#     g=[]
#     for i in range(1,11):
#         g.append(n*i)
#     return g
# print(table_of_num(9))


# n=int(input('enter a num'))
# for i in range(1,n+1):
#     print(n*i)


# Swap given two numbers and print them. (Try to do it without a temporary variable.) and return it.
# n1=int(input('enter fir num'))
# n2=int(input('enter sec num'))
# n1,n2=n2,n1
# print(n1,n2)


# Given a string str, convert the first letter of each word in the string to uppercase.
# s='i love programming'
# t=s.split()
# f=''
# l=[]
# for i in t:
#     l.append(i[0].upper()+i[1::])
# print(l)

# Given a string consisting of lowercase english alphabets, reverse only the vowels present in it
# and print the resulting string.
# s='this is a girl'
# v='aeiou'
# g=''
# for i in v:
#     if i in s:
#         g=g+i
# print(g)
# print(g[::-1])

# a=[1,2,3]
# b=[4,5,2]
# c=[(x+y) for x,y in zip(a,b)]
# print(c)

# a=[1,2,3]
# b=[4,9,4]
# c=[(i+j) for i,j in zip(a,b)]
# print(c)


# You are given a cubic dice with 6 faces. All the individual faces have a number printed on them.
# The numbers are in the range of 1 to 6, like any ordinary dice. You will be provided with a face
# of this cube, your task is to guess the number on the opposite face of the cube.

# def find_dice_num_opsit(n):
#     if n<1 or n>6:
#         return 'Invalid dice num'
#     else:
#         return 7-n
# n=int(input('enter a face num'))
# print('opposite side of the n face',find_dice_num_opsit(n))


# def opp_of_dice_num(n):
#     if n<0 or n>6:
#         return 'Invalid'
#     else:
#         return 7-n
# n=int(input('enter a dice num'))
# print('opposite of this num',opp_of_dice_num(n))


# Given a stream of incoming numbers, find average or mean of the stream at every point.
# def stream_mean(n):
#     total_sum = 0
#     count = 0
#     for i in n:
#         total_sum += i
#         count +=1
#         average = total_sum/count
#         print('Average at this point:',average)
# n=[2,4,6,8,10]
# stream_mean(n)


# Given a string, check if all its characters are the same or not.
# s='gggf'
# p=s[0]
# d=''
# for i in range(len(s)):
#     if p==s[i]:
#         d=d+p
#         if len(d)==len(s):
#             print('all letters are same')
#     else:
#         print('inv')


# Given two strings S1 and S2 as input. Your task is to concatenate two strings and then reverse the string.
# Finally print the reversed string.
# s1='hello'
# s2='world'
# d=s1+s2
# print(d[::-1])


# Given a string S as input. Delete the characters at odd indices of the string.
# s='anshika'
# t=s[0::2]
# print(t)

# Given a number, reverse it and add it to itself unless it becomes a palindrome or number
# of iterations becomes more than 5.
# a=23
# r=str(a)
# r1 = r[::-1]
# print(a+int(r1))


# A and B are good friend and programmers. They are always in a healthy competition with each other. They decide to judge the best among them by competing. They do so by comparing their three skills as per their values. Please help them doing so as they are busy.
#
# Set for A are like [a1, a2, a3]
# Set for B are like [b1, b2, b3]
#
# Compare ith skill of A with ith skill of B
# if a[i] > b[i] , A's score increases by 1
# if a[i] < b[i] , B's score increases by 1
# if a[i] = b[i] , nothing happens
# def score_fun(A,B):
#     a_score = 0
#     b_score = 0
#     for i in range(3):
#         if A[i] > B[i]:
#             a_score += 1
#         elif A[i] < B[i]:
#             b_score += 1
#     return a_score,b_score
# A=[7,5,8]
# B=[9,2,10]
# print(score_fun(A,B))


# Given a string. Count the number of Camel Case characters in it.
# s="AiVXPhhe"
# d=''
# for i in range(len(s)):
#     if s[i].isupper():
#         d=d+s[i]
#     else:
#         pass
# print(d)


# First letter in capital only
# c='this is a boy'
# c=c.split()
# for i in c:
#     print(i.title())


# remove spaces from the beginning
# s='   he llo  '
# print(s.strip())


s='hello','world'
f=','.join(s)
print(f)