/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
    
    current := head
    var previous *ListNode
    dict := make(map[int]bool)

    for current != nil {
        if _, isExist := dict[current.Val]; isExist {
            previous.Next = current.Next
        } else {
            dict[current.Val] = true
            previous = current
        }
        current = current.Next
    }

    return head
}