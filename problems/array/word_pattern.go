package main

import "strings"

func wordPattern(pattern string, s string) bool {
	words := strings.Split(s, " ")

	if len(pattern) != len(words) {
		return false
	}

	mapping := map[rune]string{}
	reserved := map[string]bool{}

	for i, ch := range pattern {
		word := words[i]
		val, ok := mapping[ch]
		if !ok {
			_, busy := reserved[word]
			if busy {
				return false
			}

			mapping[ch] = word
			reserved[word] = true
			continue
		}

		if val != word {
			return false
		}

	}
	return true
}
