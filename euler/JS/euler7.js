// What is the 10001st prime numbe
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

while (primeList.length<=10000) {
    if (isPrime(i,primeList)==true) {primeList.push(i);}
    i++;
}

console.log(primeList[10000]);