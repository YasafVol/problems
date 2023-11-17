let plaindromList = [];
let A = 0;
let Atag = 0;
let upperLimit = 1000;
let lowerLimit = 100;


for (let i = upperLimit; i >= lowerLimit; i--){
    for (let j = upperLimit; j >= lowerLimit; j--){
        A = i*j;
        Atag = A.toString().split('').reverse().join('');
        if (A-Atag===0) { plaindromList.push(A);}
    }
}

console.log(Math.max(...plaindromList));
