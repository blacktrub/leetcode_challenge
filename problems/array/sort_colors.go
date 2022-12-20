package main

func sortColors(nums []int) {
	var red, white, blue int
	for i := 0; i < len(nums); i++ {
		switch nums[i] {
		case 0:
			red++
		case 1:
			white++
		case 2:
			blue++
		}
	}

	for i := 0; i < len(nums); i++ {
		if red > 0 {
			nums[i] = 0
			red--
		} else if white > 0 {
			nums[i] = 1
			white--
		} else if blue > 0 {
			nums[i] = 2
			blue--
		}
	}

}
