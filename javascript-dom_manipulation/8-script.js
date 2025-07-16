async function getData() {
  const url = "https://hellosalut.stefanbohacek.dev/?lang=fr";
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const json = await response.json();
    var head = document.querySelector("#hello").innerText=json.hello
  } catch (error) {
    console.error(error.message);
  }
}
getData();


