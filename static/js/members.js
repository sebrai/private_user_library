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
    let alterbtn = document.createElement("button")
    alterbtn.appendChild(document.createTextNode("change"))
    let alter = document.createElement("a")
    alter.appendChild(alterbtn)
    alter.href = "members/alter/" + element[0]

    let deletebtn = document.createElement("button")
    deletebtn.appendChild(document.createTextNode("delete"))
    let del = document.createElement("a")
    del.appendChild(deletebtn)
    del.href = "members/delete/" + element[0]

    let control = document.createElement("td")
    control.appendChild(alter)
    control.appendChild(del)
    row.appendChild(control)
    datatable.appendChild(row)
}