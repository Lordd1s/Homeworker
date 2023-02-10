function isPrime(num) {
  if (num <= 1) return false;
  for (let i = 2; i < num; i++) {
    if (num % i === 0) return false;
  }
  return true;
}

function findFactors(num) {
  let factors = [];
  for (let i = 1; i <= num; i++) {
    if (num % i === 0) factors.push(i);
  }
  return factors;
}
