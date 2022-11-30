package main

type RandomizedSet struct {
	data map[int]int
	arr  []int
	r    uint32
}

func rand(x uint32) uint32 {
	x ^= (x << 13)
	x ^= (x >> 17)
	x ^= (x << 5)
	return x
}

func Constructor() RandomizedSet {
	return RandomizedSet{make(map[int]int), make([]int, 0), 10}
}

func (this *RandomizedSet) Insert(val int) bool {
	_, ok := this.data[val]
	if ok {
		return false
	}

	idx := len(this.arr)
	this.arr = append(this.arr, val)
	this.data[val] = idx
	return true
}

func (this *RandomizedSet) Remove(val int) bool {
	idx, ok := this.data[val]
	if !ok {
		return false
	}

	last := this.arr[len(this.arr)-1]
	this.arr[idx] = this.arr[len(this.arr)-1]
	this.arr = this.arr[:len(this.arr)-1]
	this.data[last] = idx

	delete(this.data, val)
	return true
}

func (this *RandomizedSet) GetRandom() int {
	this.r = rand(this.r)
	return this.arr[this.r%uint32(len(this.arr))]
}
