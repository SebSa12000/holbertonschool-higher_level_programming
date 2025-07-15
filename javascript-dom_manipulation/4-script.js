document.querySelector('#add_item').addEventListener('click', function() {

    var ul = document.querySelector(".my_list");
    var li = document.createElement("li");
    li.appendChild(document.createTextNode('Item'));
    ul.appendChild(li);
  
  });

