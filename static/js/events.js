datatable = document.getElementById("table")
let tnid = document.createTextNode("id")
let tnname = document.createTextNode("title")
let tdesc = document.createTextNode("description")
let tscale = document.createTextNode("event scale")
let tneed = document.createTextNode("members needed")
let tdone = document.createTextNode("finished")

let eid = document.createElement("th")
let ename = document.createElement("th")
let edesc = document.createElement("th")
let escale = document.createElement("th")
let eneed = document.createElement("th")
let eopt = document.createElement("th")

eid.appendChild(tnid)
ename.appendChild(tnname)
edesc.appendChild(tdesc)
escale.appendChild(tscale)
eneed.appendChild(tneed)
eopt.appendChild(tdone)

let headrow = document.createElement("tr")
headrow.appendChild(eid)
headrow.appendChild(ename)
headrow.appendChild(edesc)
headrow.appendChild(escale)
headrow.appendChild(eneed)
headrow.appendChild(eopt)


table.appendChild(headrow)
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
   
    datatable.appendChild(row)
}