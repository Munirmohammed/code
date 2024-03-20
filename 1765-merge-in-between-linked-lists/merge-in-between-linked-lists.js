/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {number} a
 * @param {number} b
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeInBetween = function(list1, a, b, list2) {
    // Find the node before the removal range
    let prev = null;
    let curr = list1;
    for (let i = 0; i < a; i++) {
        prev = curr;
        curr = curr.next;
    }

    // Remove the nodes in the range [a, b]
    let nextNode = curr.next;
    for (let i = 0; i < b - a; i++) {
        curr.next = nextNode;
        curr = nextNode;
        if (nextNode) {
            nextNode = nextNode.next;
        }
    }

    // Insert list2 into the removed range
    if (prev) {
        prev.next = list2;
    } else {
        list1 = list2;
    }
    let curr2 = list2;
    while (curr2.next) {
        curr2 = curr2.next;
    }
    curr2.next = nextNode;

    return list1;
};