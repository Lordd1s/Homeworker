let str = ''
for (i = 0; i < 8; i++) {
    for (j = 0; j < 8; j++) {
        if ((i + j) % 2 !== 0) {
            str += ' ' 
        }
        else {
            str += '#'
        }
    }
    str += '\n'
}

function arrayToObj(arr) {
    const obj = {};
    for (let i = 0; i < arr.length; i++){
        const [key, value] = arr[i]
        obj[key] = value;
    }
    return obj;
}
const arr = [['a', 1], ['b', 2]];
console.log(arrayToObj(arr))



