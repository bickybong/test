var links = [2,4,5]
for (var i = 0; i < links.length; i++) {
  (function () {
    console.log(this);
  }).call(links[i]);
}

var myModule = (function() {//IIFE, instantly called at end by () bracket
  'use strict';
  console.log('Hello World!1');//instantly called
  return {
    publicMethod: function() {//globally scoped
      console.log('Hello World!');
    }
  };
})();
myModule.publicMethod(); // calls function, outputs 'Hello World'

var log = (function (vars) { //IIFE, instantly called at end by () bracket
    // Outputs: "foo"
    console.log(vars);
})("dummy");


const Formatter = (function() {
  const log = (message) => console.log(`[${Date.now()}] Logger: ${message}`);

  const makeUppercase = (text) => {
    log("Making uppercase");
    return text.toUpperCase();
  };  

  return {
    makeUppercase, log
  }
})();

console.log(Formatter.makeUppercase("gwas"));
