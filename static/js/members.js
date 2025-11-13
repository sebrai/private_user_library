console.log("hello")
let raw = document.getElementById("data").textContent


function py_to_json(str = raw) {
    return str.replaceAll("(", "[").replaceAll(")", "]").replaceAll("'", '"');
}
let data = JSON.parse(py_to_json(raw))
console.table(data)