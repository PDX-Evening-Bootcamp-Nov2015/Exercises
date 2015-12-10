var addButton = document.getElementById("addButton");
var incompleteList = document.getElementById("incomplete-tasks");
var addItemText = document.getElementById("new-task");

var createNewTask = function(toDoText) {
    console.log("Add");
    var listItem = document.createElement("li");
    var label = document.createElement("label");
    label.innerText = addItemText.value;
    listItem.appendChild(label);
    incompleteList.appendChild(listItem);
    addItemText.value = "";
}

addButton.addEventListener('click', createNewTask);
