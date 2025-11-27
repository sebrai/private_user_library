datatable = document.getElementById("table")
let tnid = document.createTextNode("id")
let tnname = document.createTextNode("name")
let tncolor = document.createTextNode("email")
let tnjoin = document.createTextNode("joined on")
let t_options = document.createTextNode("actions")

let eid = document.createElement("th")
let ename = document.createElement("th")
let ecolor = document.createElement("th")
let ejoin = document.createElement("th")
let eopt = document.createElement("th")

eid.appendChild(tnid)
ename.appendChild(tnname)
ecolor.appendChild(tncolor)
ejoin.appendChild(tnjoin)
eopt.appendChild(t_options)

let headrow = document.createElement("tr")
headrow.appendChild(eid)
headrow.appendChild(ename)
headrow.appendChild(ecolor)
headrow.appendChild(ejoin)
headrow.appendChild(eopt)

table.appendChild(headrow)
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
    alter.href = "/members/alter/" + element[0]

    let deletebtn = document.createElement("button")
    deletebtn.appendChild(document.createTextNode("delete"))
    let del = document.createElement("a")
    del.appendChild(deletebtn)
    del.href = "/members/delete/" + element[0]

    let control = document.createElement("td")
    control.appendChild(alter)
    control.appendChild(del)
    row.appendChild(control)
    datatable.appendChild(row)
}