var names = ["NICOLE", "NIKI", "NIK", "NIKKI", "NICO", "NICHOLAS"];
var nam = 0;

var nam = document.getElementById("specialfont");
function changenames(){
  nam.innerHTML = names[pos];
  pos ++;
  if (pos >= names.length){
    pos = 0;
  }
}

var colors = ["black", "red", "green", "blue", "yellow", "purple", "orange"];
var coz = 0;

function changeColor(){
  document.getElementById("specialfont").style.color = colors[coz];
  coz ++;
  if (coz >= colors.length){
    coz = 0;
  }
}


var fonts = ["'Darker Grotesque', sans-serif", "'Bonbon', cursive", "'Hanalei', cursive"];
var poz = 0;

function changeFont(){
document.getElementById("specialfont").style.fontFamily = fonts[poz];
  //foz.setAttribute("style", 'font-family: ${fonts[poz]}');
  //like f"{}" in python
  poz ++;
  if (poz >= fonts.length){
    poz = 0;
  }
}


document.getElementById("specialfont").addEventListener("click",
function(){
  alert("You've downloaded a virus!");
  document.getElementById("specialfont").style.color = "pink";
  }
)
