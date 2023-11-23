const primeList=[2];
let i=2;

function isPrime (number, array) {
    for (let element of array){
      if (number % element === 0) {
        return false;
      }
    }
    return true;
   }
const limit = 2000000;

for (let i = 2; i<=limit; i++) {
    if (isPrime(i,primeList)==true) {primeList.push(i);}
}

console.log(primeList);
console.log(primeList.reduce((a,b)=>a+b,0))