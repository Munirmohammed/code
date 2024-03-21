var reverseList = function(head) {
    // Create an array to store the values of the linked list
    let array = [];
    
    // Traverse the linked list and add the values to the array
    let current = head;
    while (current !== null) {
        array.push(current.val);
        current = current.next;
    }
    
    // Reverse the array
    array.reverse();
    
    // Create a new linked list using the reversed array
    let reversedHead = null;
    let reversedCurrent = null;
    for (let i = 0; i < array.length; i++) {
        let newNode = new ListNode(array[i]);
        if (reversedHead === null) {
            reversedHead = newNode;
            reversedCurrent = newNode;
        } else {
            reversedCurrent.next = newNode;
            reversedCurrent = newNode;
        }
    }
    
    return reversedHead;
};