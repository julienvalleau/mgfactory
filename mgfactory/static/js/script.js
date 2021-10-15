let buttonFilter = document.getElementById("button-filter");
let buttonFilterClose = document.getElementById("button-filter-close")
let formFilter = document.getElementById("sidebar-filter");

function toggleFormFilter() {
  if(getComputedStyle(formFilter).getPropertyValue("min-width") != "0px"){
    formFilter.style.animation = "disparitionSideBarFilter 0.8s forwards";
  }
  else {
    formFilter.style.animation = "apparitionSideBarFilter 0.8s forwards";
  }
};

buttonFilter.onclick = toggleFormFilter; 
buttonFilterClose.onclick = toggleFormFilter;

function startTime() {
  const today = new Date();
  let h = today.getHours();
  let m = today.getMinutes();
  let s = today.getSeconds();
  m = checkTime(m);
  s = checkTime(s);
  document.getElementById('hour').innerHTML =  h + ":" + m + ":" + s;
  setTimeout(startTime, 1000);
}

function checkTime(i) {
  if (i < 10) {i = "0" + i};  // Ajout un 0 devant le nombre si < 10
  return i;
}