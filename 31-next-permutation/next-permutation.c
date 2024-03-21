void swap(int* a, int* b) {
    int t = *a;
    *a = *b;
    *b = t;
}

void reverse(int* arr, int start, int end) {
    while (start < end) {
        swap(&arr[start], &arr[end]);
        start++;
        end--;
    }
}

void nextPermutation(int* nums, int numsSize) {
    if (numsSize < 2) {
        return;
    }
    int i = numsSize - 2;
    while (i >= 0 && nums[i] >= nums[i + 1]) {
        i--;
    }
    if (i >= 0) {
        int j = numsSize - 1;
        while (j > i && nums[j] <= nums[i]) {
            j--;
        }
        swap(&nums[i], &nums[j]);
    }
    reverse(nums, i + 1, numsSize - 1);
}