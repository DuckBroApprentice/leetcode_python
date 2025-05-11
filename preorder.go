package python

type Node struct {
	Val      int
	Children []*Node
}

func preorder(root *Node) []int {
	var res []int
	res = append(res, root.Val)
	if root == nil {
		return res
	}
	for _, next := range root.Children {
		res = append(res, preorder(next)...)
	}
	return res
}

//runtime 0ms memory 7.88MB
