package python

func countConsistentStrings(allowed string, words []string) int {
	allowMap := make(map[byte]struct{})
	for i := 0; i < len(allowed); i++ {
		allowMap[allowed[i]] = struct{}{}
	}
	count := 0
	for i := 0; i < len(words); i++ {
		for j := 0; j < len(words[i]); j++ {
			if _, exists := allowMap[words[i][j]]; !exists {
				break
			}
			if j == len(words[i])-1 {
				count++
			}
		}
	}
	return count
}

//runtime 31ms  memory 9.02
