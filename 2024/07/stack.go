package main

import "slices"

type Stack[T any] struct {
	vals []T
}

func NewStack[T any](initialElements []T) Stack[T] {
	return Stack[T]{
		vals: slices.Clone(initialElements),
	}
}

func (s Stack[T]) Empty() bool {
	return len(s.vals) <= 0
}

func (s Stack[T]) Size() int {
	return len(s.vals)
}

func (s *Stack[T]) Push(v T) {
	s.vals = append(s.vals, v)
}

// Assumes stack is not empty
func (s *Stack[T]) Pop() T {
	top := s.vals[len(s.vals)-1]
	s.vals = s.vals[:len(s.vals)-1]
	return top
}
