a=[1,2,3,4,5,6]
b=[2, 4, 6, 8, 10]
function Sum(a){
su=0;
    for (const i of a) {
    // document.write(i)
    if(i%2==0){
    su+=i;
}
// document.write()
}
return su;
// document.write(su)
}
document.write(Sum(a))
document.write(Sum(b))
