package python

func xorOperation(n int, start int) int {
	nums := make([]int, n, n)
	res := 0
	for i := 0; i < n; i++ {
		nums[i] = start + 2*i
		res = res ^ nums[i]
	}
	return res
}

//runtime 0ms  memory 4.04MB
