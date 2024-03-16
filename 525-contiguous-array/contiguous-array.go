func findMaxLength(nums []int) int {
    maxLen := 0
    diffMap := make(map[int]int)
    diff := 0

    // Initialize the map with a difference of 0 at index -1 to handle the case where the first encountered difference is 0
    diffMap[0] = -1

    for i, num := range nums {
        if num == 0 {
            diff--
        } else {
            diff++
        }

        // Check if the current difference has been encountered before
        if index, ok := diffMap[diff]; ok {
            maxLen = max(maxLen, i-index)
        } else {
            // Store the index of the first occurrence of the current difference
            diffMap[diff] = i
        }
    }

    return maxLen
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
