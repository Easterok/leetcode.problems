package main

import "fmt"

func main() {
	fmt.Println(tree2str(&TreeNode{
		Val: 1,
		Right: &TreeNode{
			Val: 3,
		},
		Left: &TreeNode{
			Val: 2,
			Left: &TreeNode{
				Val: 4,
			},
		},
	}))
}
