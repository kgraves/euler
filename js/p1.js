function multiples(max) {
  var sum = 0;
  for (var i=1; i<max; i++) {
    if (i % 3 === 0 || i % 5 === 0) {
      sum += i;
    }
  }
  return sum;
}

console.log( multiples(1000) );
