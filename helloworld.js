var names = ["NICOLE", "NIKI", "NIK", "NIKKI", "NICO", "NICHOLAS"];
var pos = 0;
var loc = document.getElementById("name")


function changenames(){
  loc.innerHTML = name[pos];
  pos ++;
  if (pos >= names.length){
    pos = 0;
  }
}


var foz = document.getElementById("name");
console.log(foz)

var colors = ["black", "red", "green", "blue", "yellow", "purple", "orange"];
var coz = 0;

function changeFontColor(){
  foz.style.fontcolor = colors[coz];
  coz ++;
  if (coz >= colors.length){
    coz = 0;
  }
  foz.style.color = "red", "blue", "black", "green", "yellow";
}


var fonts = ["'Darker Grotesque', sans-serif", "'Bonbon', cursive", "'Hanalei', cursive"];
var poz = 0;

function changeFont(){
  foz.style.fontFamily = fonts[poz];
  //foz.setAttribute("style", 'font-family: ${fonts[poz]}');
  //like f"{}" in python
  poz ++;
  if (poz >= fonts.length){
    poz = 0;
  }
}
