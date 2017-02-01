function sumEvenFibs(max) {
  var first = 1, second = 2;
  var sum = 0;

  while (second < max) {
    if (second % 2 === 0) {
      sum += second;
    }

    var tmp = second;
    second += first;
    first = tmp;
  }

  return sum
}

console.log( sumEvenFibs(4000000) );
