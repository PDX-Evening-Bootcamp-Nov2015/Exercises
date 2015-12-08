// Creation of a DOM Element

var element = document.createElement(tagName);

// Adding created element to the DOM

var child = element.appendChild(child);

//Styling an HTML element

element.style.color = "#ff3300";
element.style.marginTop = "30px";
element.style.paddingBottom = "30px";

// get HTML of element

var content = element.innerHTML;

// or setting the HTML

otherElement.innterHTML = content;

// getting and setting the class name

var cName = element.className;
otherElement.className = cName;

// getting and setting the ID

var idStr = element.id;
otherElement.id = idStr;

// ACCESSING THE DOM
    // by ID
    element = document.getElementById(id);

    // by class
    elements = document.getElementsByClassName(names); //notice plurals

    //by tag Name
    var elements = document.getElementsByTagName(name);

    // by first found selector
    element = document.querySelector(selectors);

    // by array of selectors
    elementList = document.querySelectorAll(selectors);

// Relationships
    // children
    ndList = elementNodeReference.childNodes;

    //next sibling
    nextNode = node.nextSibling
