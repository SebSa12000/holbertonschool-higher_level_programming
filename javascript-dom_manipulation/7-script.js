async function getData() {
  const url = "https://swapi-api.hbtn.io/api/films/?format=json";
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const json = await response.json();
    

    var ul = document.querySelector("#list_movies");

    for (var elem in json.results)
    {
        var li = document.createElement("li");
        li.appendChild(document.createTextNode(json.results[elem].title));
        ul.appendChild(li);
    }
  } catch (error) {
    console.error(error.message);
  }
}
getData();


