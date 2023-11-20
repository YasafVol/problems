let range = [];
const targetNum = 20;
for (let i = 1; i<= targetNum; i++) {range.push(i);}
let smallEvenDivisable = 0;
smallEvenDivisable = Math.max(...range);

while (range.length > 0) {
    smallEvenDivisable *= range[0];

    for (let element of range) {
        if (smallEvenDivisable%element===0) {
            let index = range.indexOf(element);
            range.splice(index,1);
        }
    }
}

console.log(smallEvenDivisable);