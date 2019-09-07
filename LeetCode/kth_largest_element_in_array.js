
// 215
// Kth Largest Element in an Array

var findKthLargest = function (nums, k) {
    buildMaxHeap(nums);
    while (k > 1) {
        nums.shift();
        buildMaxHeap(nums);
        k--;
    }

    return nums[0];
};

function buildMaxHeap(nums) {
    const size = nums.length;
    let i = Math.floor(size / 2 - 1);

    while (i >= 0) {
        heapify(nums, i, size);
        i--;
    }
}

function heapify(arr, root, max) {
    let toSwapIdx;
    let leftIdx;
    let rightIdx;

    while (root < max) {
        toSwapIdx = root;
        leftIdx = root * 2 + 1;
        rightIdx = root * 2 + 2;

        if (arr[toSwapIdx] < arr[leftIdx]) {
            toSwapIdx = leftIdx;
        }

        if (arr[toSwapIdx] < arr[rightIdx]) {
            toSwapIdx = rightIdx;
        }

        if (root === toSwapIdx) return;

        [arr[toSwapIdx], arr[root]] = [arr[root], arr[toSwapIdx]];
        root = toSwapIdx;
    }
}
