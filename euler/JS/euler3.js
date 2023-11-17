const num = 600851475143;
const sqrtNum = Math.floor(Math.sqrt(num));
let largestPrimefactor=0;
let  factors = [2];

function isPrime (number, array) {
 for (let element of array){
   if (number % element === 0) {
     return false;
   }
 }
 return true;
}

function getFactors (sqrtNum, factors){
  for (let i = 3; i <= sqrtNum; i++) {
    if (isPrime(i, factors)===true) {
      factors.push(i);
    }
  }
}

getFactors(sqrtNum, factors);
for (let i = factors.length; 1>0; i--) {
  if (num % factors[i] === 0) {
    largestPrimefactor = factors[i];
    console.log( largestPrimefactor);
  }
}
