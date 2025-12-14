"""
问题2: 逆序对计数 (Inversion Count)
题目：给定一个数组，计算数组中逆序对的数量
逆序对定义：如果 i < j 且 arr[i] > arr[j]，则 (i, j) 是一个逆序对

时间复杂度: O(n log n)

输入格式：
第一行：测试用例数量 T
对于每个测试用例：
  第一行：数组长度 n
  第二行：n 个整数，用空格分隔

输出格式：
对于每个测试用例，输出逆序对的数量

输入：
1
5
5 2 3 4 1
输出：
10
"""

def merge_sort(arr,temp,left,right):
    """ 递归执行归并 """
    count = 0
    mid = left+(right-left)//2 #分成左右递归执行
    if left < right: 
        count += merge_sort(arr,temp,left,mid)
        count += merge_sort(arr,temp,mid+1,right)
        count += merge(arr,temp,left,mid,right) #合并

    return count

def merge(arr,temp,left,mid,right):
    """归并排序的合并部分"""
    for inx in range(left,right+1): #复制临时数组
        temp[inx] = arr[inx] 
    
    i,j,k = left,mid+1,left #k表示当前真实数组arr更新的位置
    count = 0
    while i<= mid and j <=right: #正序
        if temp[i]<=temp[j]:
            arr[k] = temp[i]
            i += 1
            k += 1
        else: #发现逆序
            arr[k] = temp[j]
            k += 1
            j += 1
            count += mid-i+1 #左右部分内部有序，小于第i个 就是 小于i后面所有
    
    while i<=mid: #更新因为逆序而跳过的数
        arr[k] = temp[i]
        i += 1
        k += 1
    
    return count

try:
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        arry = list(map(int,input().split()))
        temp = [0]*n
        count = merge_sort(arry,temp,0,n-1)
        print(count)
except EOFError:
    exit()



    

