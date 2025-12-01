datatable = document.getElementById("table")
for (let J = 0; J < data.length; J++) {
    const element = data[J];

    let row = document.createElement("tr")
    for (let i = 0; i < element.length; i++) {
        const item = element[i];
        let text = document.createTextNode(item)
        let tbox;
        if (i == 5) {
            
            tbox = document.createElement("input")
            tbox.type = "checkbox"
            tbox.disabled = true
            tbox.checked = Boolean(item)
        }
        else {
            tbox = document.createElement("div")
            tbox.appendChild(text)
        }

        let box = document.createElement("td")
        box.appendChild(tbox)
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