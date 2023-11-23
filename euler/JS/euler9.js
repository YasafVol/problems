
let pyTrip = [];
for (let a = 998; a>=0; a--){
    for (let b = a+1; b>=0; b--) {
        let c = Math.sqrt(a**2 + b**2);
        if ((a + b + c)==1000) {
            pyTrip = [a, b, c];
            break;
        }
    }
}

console.log( pyTrip);
//this uses the reduce and callback func to multiply all array elements
console.log(pyTrip.reduce((a, b)=> a*b, 1))