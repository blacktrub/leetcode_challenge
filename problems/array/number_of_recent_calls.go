package main

type Node struct {
	val  int
	next *Node
}

type Deque struct {
	start *Node
	end   *Node
	n     int
}

func (d *Deque) Add(n *Node) {
	d.n++
	if d.start == nil {
		d.start = n
	}
	if d.end == nil {
		d.end = n
		return
	}

	d.end.next = n
	d.end = n
}

func (d Deque) Len() int {
	return d.n
}

func (d *Deque) PopLeft() {
	d.start = d.start.next
	d.n--
}

func (d *Deque) Min() int {
	return d.start.val
}

type RecentCounter struct {
	q Deque
}

func Constructor() RecentCounter {
	return RecentCounter{Deque{}}
}

func (this *RecentCounter) Ping(t int) int {
	this.q.Add(&Node{t, nil})
	for this.q.Min() < t-3000 {
		this.q.PopLeft()
	}
	return this.q.Len()
}
