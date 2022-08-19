function fibonacciGenerator (n) {
    //Do NOT change any of the code above 👆
        
        //Write your code here:
        var array = [0,1,1];
        if (n==1){
            return [0];
        } else if (n==2){
            return [0,1];
        }
        while (array.length < n){
            var length = array.length;
            array.push(array[length - 1] + array[length - 2]);
        }
        return array;
        //Return an array of fibonacci numbers starting from 0.
        
    //Do NOT change any of the code below 👇
}

console.log(fibonacciGenerator(15));