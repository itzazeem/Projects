n=parseInt(prompt("Enter The Table Number"))
document.write(`square root without float value<br>`)

i=1;
s=0;
while(i<=10){
    // document.write(i)
    j=1;
    while(j<=n){
        s=i*j;
        d=1/2
        e=Math.floor(s**d)
        document.write(`(square root ${s} = ${e})\t` )
        j++
    }
    document.write("<br>")
    i++
}
// document.write(i)