const naturalNambersSeries = 100;
let sumOfSquares = 0;
let squaredSum = 0;

for (let i = 1; i<= naturalNambersSeries; i++) {
    sumOfSquares+=i**2;
    squaredSum+=i;
}

console.log(sumOfSquares);
console.log(squaredSum, "^2 =", (squaredSum**2));

console.log((squaredSum**2)-sumOfSquares);