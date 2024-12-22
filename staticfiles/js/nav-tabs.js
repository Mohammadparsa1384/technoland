function openTab(evt, tabName) {
    var i, x, tablinks;
    x = document.getElementsByClassName("tabs-container");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < x.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" selected", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " selected";
}
