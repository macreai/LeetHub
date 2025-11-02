func lengthOfLongestSubstring(s string) int {
    if len(s) == 0 {
        return 0
    }

    runes := []rune(s)
    
    charIndex := make(map[rune]int)
    
    left := 0 
    
    maxLength := 0 

    for right := 0; right < len(runes); right++ {
        currentChar := runes[right]

        if lastIndex, found := charIndex[currentChar]; found && lastIndex >= left {
            left = lastIndex + 1
        }

        charIndex[currentChar] = right

        currentLength := right - left + 1
        
        if currentLength > maxLength {
            maxLength = currentLength
        }
    }

    return maxLength
}