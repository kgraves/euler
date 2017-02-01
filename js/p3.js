function factorize(number) {
  var roots=[], product=1; x=2, y=number;

  while (product < number) {
    while (y % x === 0) {
      roots.push(x);
      y = y/x;
      product *= roots[ roots.length-1 ];
    }

    x += 1;
  }

  return roots;
}

var facts = factorize(600851475143);
console.log(facts[ facts.length-1 ]);
