package main

import (
  "fmt"
)

func evenFibs(max int) int {
  var first, second int = 1, 2
  var sum int = 0

  for second < max {
    if second % 2 == 0 {
      sum += second
      fmt.Printf("%d\n", second)
    }

    first, second = second, first+second
  }

  return sum
}

func main() {
  fmt.Printf("%d\n", evenFibs(4000000))
}
