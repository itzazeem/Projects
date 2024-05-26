n=prompt("Enter The Input")
// var b="great";
// document.write(`azeem hai ${b}'`)
function sum(a) {
    const regex = /\d+/g;
    const n = a.match(regex);
    
    if (!n) {
        return 0;
    }
    
    let s=0;
    for (const i of n){ 
        s+=parseInt(i)
    }
    return s;
}
document.write(sum(n));
// console.log(sum("123xyz"));
// console.log(sum("1xyz23"));
// console.log(sum("xyz"));
