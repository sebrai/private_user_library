datatable = document.getElementById("datatable")
for (let J = 0; J < data.length; J++) {
    const element = data[J];

    let row = document.createElement("tr")
    for (let i = 0; i < element.length; i++) {
        const item = element[i];
        let text = document.createTextNode(item)
        let tbox = document.createElement("div")
        tbox.appendChild(text)
        let box = document.createElement("td")
        box.appendChild(tbox)
        row.appendChild(box)
    }

    datatable.appendChild(row)
}