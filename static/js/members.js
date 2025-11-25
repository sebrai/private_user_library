datatable = document.getElementById("table")
for (let J = 0; J < data.length; J++) {
    const element = data[J];
    
    let row = document.createElement("tr")
    for (let i = 0; i < element.length; i++) {
        const item = element[i];
        let text = document.createTextNode(item)
        let box = document.createElement("td")
        box.appendChild(text)
        row.appendChild(box)
    }
    datatable.appendChild(row)
}