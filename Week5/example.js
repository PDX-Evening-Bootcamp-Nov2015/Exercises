var captureTab = function (event) {
    var newTab = event.target;
    var currentClass = newTab.parentElement.className;
    var contentId = newTab.getAttribute('href').slice(1);
    if (!currentClass) {
        switchTab(newTab, contentId);
    }
};

var switchTab = function (tab, contentId) {
    var elems = document.getElementsByClassName("active");
    for (var i = elems.length -1; i >=  0; i -= 1) {
        elems[i].classList.remove("active");
    }
    var contentDiv = document.getElementById(contentId);
    tab.parentElement.className = "active";
    contentDiv.classList.add("active");
};

var bindListener = function (index, tab) {
    tab.addEventListener('click', captureTab, false);
};

(function() {
    var tabs = document.querySelector('.tabs .tab-links ul').getElementsByTagName('li');
    for (var i = 0; i < tabs.length; i += 1) {
        bindListener(i, tabs[i]);
    }
}());
