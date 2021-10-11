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