function whosPaying(names) {
    
    /******Don't change the code above*******/
        
        //Write your code here.
        var noNames = names.length;
        var ran = Math.floor(Math.random() * noNames);
        var chosen = names[ran];
        return `${chosen} is going to buy lunch today!`;
    
    /******Don't change the code below*******/    
    }

console.log(whosPaying(["Angela", "Ben", "Jenny", "Michael", "Chloe"])) ;