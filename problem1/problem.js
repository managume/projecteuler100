function multiplesOf3and5(number) {
    let sum=0;
    for(let i=1;i<number;i++){
      if(i%3 == 0){
        sum+=i;
      }else if(i%5 == 0){
        sum+=i;
      }
    }
    return sum;
  }
  
  console.log(multiplesOf3and5(1000));
  console.log(multiplesOf3and5(49));
  console.log(multiplesOf3and5(19564));
  console.log(multiplesOf3and5(8456));