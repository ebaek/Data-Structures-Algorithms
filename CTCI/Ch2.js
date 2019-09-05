// Chapter 2
// Linked Lists

// 2.1 
// Remove Dups 
// remove duplicates from an unsorted linked list

function removeDups(head) {
}

// 2.2: Return Kth to Last Node from End of List

function kthNode(head, n) {
    let startPointer = head;
    let endPointer = head;

    for (let i = 0; i < n; i++) {
        endPointer = endPointer.next;
    }

    if (!endPointer) return head.next;

    while (endPointer.next) {
        startPointer = startPointer.next;
        endPointer = endPointer.next;
    }

    startPointer.next = startPointer.next.next;

    return head;
}

// 2.3: Delete Middle Node

function deleteMiddleNode(head) {
}

// 2.4: Partition List