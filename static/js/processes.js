console.log("hello")
let raw = document.getElementById("data").textContent


function py_to_json(str = raw) {
    
    result = str.replaceAll("(", "[").replaceAll(")", "]").replaceAll("'", '"');
     console.table(JSON.parse(result))
    return result
}
let data = JSON.parse(py_to_json(raw))
console.table(data)