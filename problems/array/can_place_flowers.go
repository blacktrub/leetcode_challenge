package main

func canPlaceFlowers(flowerbed []int, n int) bool {
	put := 0
	skip := false
	for i := 0; i < len(flowerbed); i++ {
		if skip {
			skip = false
			continue
		}
		if flowerbed[i] == 1 {
			skip = true
			continue
		}

		if i < len(flowerbed)-1 {
			if flowerbed[i+1] == 1 {
				continue
			}
		}

		put++
		skip = true
	}
	return put >= n
}
