/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func isPalindrome(head *ListNode) bool {
    slow := head
    fast := head
    stored := []int{}

    for fast != nil && fast.Next != nil {
        stored = append(stored, slow.Val)
        slow = slow.Next
        fast = fast.Next.Next
    }

    if fast != nil {
        slow = slow.Next
    }
    
    i := len(stored) - 1
    for slow != nil {
        if slow.Val != stored[i] {
            return false
        }
        slow = slow.Next
        i--
    }

    return true
}