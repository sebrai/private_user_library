datatable = document.getElementById("table")
for (let J = 0; J < data.length; J++) {
    const element = data[J];

    let row = document.createElement("tr")
    for (let i = 0; i < element.length; i++) {
        const item = element[i];
        let text = document.createTextNode(item)
        if (i== 5) {
            text.textContent = Boolean(item)
        }
        let box = document.createElement("td")
        box.appendChild(text)
        row.appendChild(box)
    }
    let add_memberbtn = document.createElement("button")
    add_memberbtn.appendChild(document.createTextNode("join effort"))
    let add_member = document.createElement("a")
    add_member.appendChild(add_memberbtn)
    add_member.href = "/events/add_member/" + element[0]

    let finishbtn = document.createElement("button")
    finishbtn.appendChild(document.createTextNode("finish"))
    let finish = document.createElement("a")
    finish.appendChild(finishbtn)
    finish.href = "/events/finish/" + element[0]

    let control = document.createElement("td")
    control.appendChild(add_member)
    control.appendChild(finish)
    row.appendChild(control)
    datatable.appendChild(row)
}