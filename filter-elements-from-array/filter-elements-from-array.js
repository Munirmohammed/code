var filter = function(arr, fn) {
   let newArray = [];
   arr.forEach((x,i) => {
      if(fn(x,i)){
         newArray.push(x);
      }
   });
   return newArray;
};