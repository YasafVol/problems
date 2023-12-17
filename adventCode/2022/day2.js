// https://adventofcode.com/2022/day/2 

const fs = require(`fs`);
const temp = fs.readFileSync("C:/prog/problems/adventCode/2022/day2input.txt",`utf8`);
let firstSplit = temp.split("\n");

const valueX = 1;
const valueY = 2;
const valueZ = 3;

// X for Rock = 1 , Y for Paper = 2, and Z for Scissors =3

let countX = 0;
let countY = 0;
let countZ = 0;

firstSplit.forEach(item => {
    const [_, letter] = item.split(' ');
//  console.log (letter);
    if (letter === `X`) {
        countX++;
    } else if (letter === `Y`) {
        countY++; 
    } else if (letter === `Z`) {
        countZ++;
}});

let sumX = countX * valueX;
let sumY = countY * valueY;
let sumZ = countZ * valueZ;


console.log('Count of X:', countX, 'Sum of X:', sumX );
console.log('Count of Y:', countY, 'Sum of Y:', sumY );
console.log('Count of Z:', countZ, 'Sum of Z:', sumZ );

// Then, split each element in the resulting array by space (" ")
/*
let rps = temp.split("\n");
rps = rps.map(a => a.split(" "));
console.log(rps[0]);




A for Rock, B for Paper, and C for Scissors


win 6 draw 3 loss 0 

rock > Scissors
Scissors > paper
paper > rock

*/