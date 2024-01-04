package main

type Node struct {
	Val         bool
	IsLeaf      bool
	TopLeft     *Node
	TopRight    *Node
	BottomLeft  *Node
	BottomRight *Node
}

func construct(grid [][]int) *Node {
	var dfs func(row, col, width int) *Node
	dfs = func(row, col, width int) *Node {
		if width == 1 {
			return &Node{
				Val:    grid[row][col] == 1,
				IsLeaf: true,
			}
		}

		w := width / 2
		tl := dfs(row, col, w)
		tr := dfs(row, col+w, w)
		bl := dfs(row+w, col, w)
		br := dfs(row+w, col+w, w)

		var node *Node

		if tl.IsLeaf && tr.IsLeaf && bl.IsLeaf && br.IsLeaf && tl.Val == tr.Val && bl.Val == br.Val && tl.Val == bl.Val {
			node = &Node{
				Val:    tl.Val,
				IsLeaf: true,
			}
		} else {
			node = &Node{
				Val:         true,
				IsLeaf:      false,
				BottomLeft:  bl,
				BottomRight: br,
				TopLeft:     tl,
				TopRight:    tr,
			}
		}

		return node
	}

	return dfs(0, 0, len(grid))
}
