console.log("hello")
let raw = document.getElementById("data").textContent

function pdate(y, m, d) {
    return `${d}/${m}/${y}`
}
function py_to_json(str = raw) {
    
    result = str.replaceAll("(", "[").replaceAll(")", "]").replaceAll("'", '"').replaceAll('datetime.date(.*)','pdate(.*)');
     console.table(JSON.parse(result))
    return result
}
let data = JSON.parse(py_to_json(raw))
console.table(data)