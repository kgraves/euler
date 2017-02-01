package main

import (
  "fmt"
)

func multiples(max int) int {
  var sum int = 0

  for i := 0; i < max; i++ {
    if i % 3 == 0 || i % 5 == 0 {
      sum += i
    }
  }

  return sum
}

func main() {
  fmt.Printf("Now you have %d problems\n", multiples(1000))
}
