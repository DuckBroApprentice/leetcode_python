package python

// func transformArray(nums []int) []int {
// 	var res []int
// 	for i := 0; i < len(nums); i++ {
// 		if nums[i]%2 == 0 {
// 			nums[i] = 0
// 			res = append([]int{0}, res...)
// 			continue
// 		}
// 		nums[i] = 1
// 		res = append(res, 1)
// 	}
// 	return res
// }
//runtime 1ms memory8.26MB

func transformArray(nums []int) []int {
	len0 := 0
	len1 := 1
	for i := 0; i < len(nums); i++ {
		if nums[i]%2 == 1 {
			len1++
		} else {
			len0++
		}
	}
	res := make([]int, len0+len1-1, len0+len1-1)
	for i := 0; i < len(res); i++ {
		if i < len0 {
			res[i] = 0
		} else {
			res[i] = 1
		}
	}
	return res
}

//runtime 0ms memory5.04MB
