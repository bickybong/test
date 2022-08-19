function Pet(type, legs) {
    this.type = type;
    this.legs = legs;
    this.logInfo = () =>{
      console.log(this === myCat); // => false
      console.log(`The ${this.type} has ${this.legs} legs`);
    }
  }
  const myCat = new Pet('Cat', 4);
  // logs "The undefined has undefined legs"
  // or throws a TypeError in strict mode
//   const boundLogInfo = myCat.logInfo.bind(myCat);

  setTimeout(myCat.logInfo, 1000);