func twoSum(nums []int, target int) []int {
    remainder := make(map[int]int)

    for index, num := range nums {

        complement := target - num

        if i, ok := remainder[complement]; ok {
            return []int{i, index}
        }

        remainder[num] = index
    }

    return []int{}
}