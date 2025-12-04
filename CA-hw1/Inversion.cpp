/*
问题2: 逆序对计数 (Inversion Count)
题目：给定一个数组，计算数组中逆序对的数量
逆序对定义：如果 i < j 且 arr[i] > arr[j]，则 (i, j) 是一个逆序对

算法：使用归并排序计算逆序对数量
- 在归并过程中，如果右半部分的元素小于左半部分的元素
- 则说明该右半部分元素与左半部分剩余的所有元素都构成逆序对

时间复杂度: O(n log n)

输入格式：
第一行：测试用例数量 T
对于每个测试用例：
  第一行：数组长度 n
  第二行：n 个整数

输出格式：
对于每个测试用例，输出逆序对的数量

示例：
输入：
1
5
5 2 3 4 1
输出：
10
*/

#include <iostream>
#include <vector>
using namespace std;

// 合并并统计逆序对数量
long long merge_and_count(vector<int>& arr, vector<int>& temp, int left, int mid, int right) {
    int i = left, j = mid + 1, k = left;
    long long inv_count = 0;

    // 复制到临时数组
    for (int idx = left; idx <= right; idx++) {
        temp[idx] = arr[idx];
    }

    // 合并两个有序子数组并统计逆序对
    while (i <= mid && j <= right) {
        if (temp[i] <= temp[j]) {
            arr[k++] = temp[i++];
        } else {
            arr[k++] = temp[j++];
            // 左半部分剩余元素都与当前右元素构成逆序对
            inv_count += (mid - i + 1);
        }
    }

    // 复制左半部分剩余元素
    while (i <= mid) {
        arr[k++] = temp[i++];
    }
    // 右半部分剩余元素无需处理（已在原数组）

    return inv_count;
}

// 归并排序并统计逆序对总数
long long merge_sort_and_count(vector<int>& arr, vector<int>& temp, int left, int right) {
    long long inv_count = 0;
    if (left < right) {
        int mid = left + (right - left) / 2; // 避免溢出

        // 分治处理左右子数组
        inv_count += merge_sort_and_count(arr, temp, left, mid);
        inv_count += merge_sort_and_count(arr, temp, mid + 1, right);
        // 合并并统计当前层逆序对
        inv_count += merge_and_count(arr, temp, left, mid, right);
    }
    return inv_count;
}

int main() {
    ios::sync_with_stdio(false); // 加速cin/cout
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int n;
        cin >> n;

        vector<int> arr(n);
        vector<int> temp(n); // 临时数组，避免重复分配

        // 读取数组元素
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }

        // 计算逆序对总数
        long long result = merge_sort_and_count(arr, temp, 0, n - 1);
        cout << result << '\n';
    }

    return 0;
}