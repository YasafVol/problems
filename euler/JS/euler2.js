let a = 1;
let b = 1;
let fib = 0;
let sum = 0;
const limit = 4000000;

while (fib < limit ) {
    if (fib % 2 ==0) { sum += fib; }
    //console.log(fib, "-->", sum);
    fib = a + b;
    a = b;
    b = fib;
}
console.log(sum);