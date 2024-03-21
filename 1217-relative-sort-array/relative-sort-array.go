func relativeSortArray(arr1 []int, arr2 []int) []int {
    count := make(map[int]int)
	for _, num := range arr1 {
		count[num]++
	}

	res := make([]int, 0)
	for _, num := range arr2 {
		for i := 0; i < count[num]; i++ {
			res = append(res, num)
		}
		delete(count, num)
	}

	remaining := make([]int, 0)
	for num := range count {
		remaining = append(remaining, num)
	}
	sort.Ints(remaining)

	for _, num := range remaining {
		for i := 0; i < count[num]; i++ {
			res = append(res, num)
		}
	}

	return res
}