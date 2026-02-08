/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeElements(head *ListNode, val int) *ListNode {
    
    dummy := &ListNode{Next: head}
    current := head
    prev := dummy
    
    for current != nil {
        if current.Val == val {
            prev.Next = current.Next
        } else {
            prev = current    
        }
        
        current = current.Next
    }

    return dummy.Next
}