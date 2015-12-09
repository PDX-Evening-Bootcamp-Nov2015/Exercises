
var hello = function (event){
  event.preventDefault(); // stop page reload.

  var new_list_text = document.getElementById("new_list_text").value;
  console.log("new_list_text: " + new_list_text);
  /* alert("button clicked " + new_list_text); */

  // var test_changing_me = document.getElementById("test_changing_me");
  // console.log(test_changing_me.innerText);
  // test_changing_me.textContent = new_list_text;

  var new_li = document.createElement("li");
  new_li.textContent = new_list_text;

  /* assign a new automatic id */
  var new_li_id = next_list_item_id();
  new_li.setAttribute("id", new_li_id);
  new_li_self_destruct = document.createElement("button");
  new_li_self_destruct.textContent = "Remove Me";
  new_li_self_destruct.setAttribute('onclick'
                                  , 'remove_li("' + new_li_id + '")');
  new_li.appendChild(new_li_self_destruct);

  var ul = document.getElementById("todo_list");
  ul.appendChild(new_li);
};

var remove_li = function(li_id) {
  var victim = document.getElementById(li_id);
  victim.parentNode.removeChild(victim);
};

var next_list_item_id = (function () {
  var counter = 0;
  return function () {
    counter += 1;
    return "li_autonumber_" + counter;
  }
}());

var goodbye = function (event){
  event.preventDefault(); // stop page reload.

  var ul = document.getElementById("todo_list");
  var first_todo = ul.children[0];
  ul.removeChild(first_todo);
};
