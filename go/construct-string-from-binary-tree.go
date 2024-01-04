package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func tree2str(root *TreeNode) string {
	var dfs func(node *TreeNode) string
	dfs = func(node *TreeNode) string {
		if node == nil {
			return ""
		}

		if node.Left == nil && node.Right == nil {
			return fmt.Sprintf("%d", node.Val)
		}

		if node.Right == nil {
			return fmt.Sprintf("%d(%s)", node.Val, dfs(node.Left))
		}

		return fmt.Sprintf("%d(%s)(%s)", node.Val, dfs(node.Left), dfs(node.Right))
	}

	return dfs(root)
}
