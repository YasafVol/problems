// https://adventofcode.com/2022/day/1

// const { isUtf8 } = require('buffer');
const fs = require('fs');

const inventory = fs.readFileSync("C:/prog/problems/adventCode/2022/day1input.txt",`utf8`);
// console.log(inventory);
const invList = inventory.split("\n");
// console.log(invList);
const splitArrays = [];
let currentArray =[];


for ( const item of invList ) {
    if (item ===""){
        if (currentArray.length > 0){
            splitArrays.push(currentArray);
            currentArray = [];
        }
    } else {
        currentArray.push(parseInt(item));
    }
}

const elfCalorieList = [];
for (subSet of splitArrays){
    let sum = 0;
    subSet.forEach(num => {sum+=num})
    elfCalorieList.push(sum);
}

console.log("top 1 elf => ", Math.max(...elfCalorieList));

// https://adventofcode.com/2022/day/1#part2

elfCalorieList.sort((a,b) => b-a);
//console.log(elfCalorieList);

let top3=0;
for (let i =0; i<3;i++) {
    top3 +=elfCalorieList[i];
}

console.log("top 3 elves => ", top3);

