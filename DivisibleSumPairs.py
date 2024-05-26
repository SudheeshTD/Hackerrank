# def divisibleSumPairs(n, k, ar):
#     # Write your code here
#     l = len(ar)
#     count = 0
#     for i in range(0,l-1):
#         for j in range(i+1,l):
#             if (ar[i] + ar[j] == k):
#                 count+=1
                
#     return count
 
result = divisibleSumPairs(6,3,[1, 3, 2, 6, 1, 2])