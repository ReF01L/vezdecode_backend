<template>
    <div id="hello"></div>
</template>

<script>
import axios from "axios";

export default {
    name: 'HelloWorld',
    mounted() {
        axios.get('http://127.0.0.1:8000/dashboard')
            .then(res => {
                let elem = document.getElementById('hello')

                let title = document.createElement('h2')
                title.innerText = 'Best'
                elem.appendChild(title)
                elem.appendChild(this.buildHtmlTable(res.data.best))

                title = document.createElement('h2')
                title.innerText = 'Last interactions'
                elem.appendChild(title)
                elem.appendChild(this.buildHtmlTable(res.data.last_interaction))
            })
            .catch(err => {
                console.log(err)
            })
    },
    methods: {
        addAllColumnHeaders(arr, table) {
            let columnSet = [],
                tr = document.createElement('tr').cloneNode(false);
            for (let i = 0, l = arr.length; i < l; i++) {
                for (let key in arr[i]) {
                    // eslint-disable-next-line no-prototype-builtins
                    if (arr[i].hasOwnProperty(key) && columnSet.indexOf(key) === -1) {
                        columnSet.push(key);
                        let th = document.createElement('th').cloneNode(false);
                        th.appendChild(document.createTextNode(key));
                        tr.appendChild(th);
                    }
                }
            }
            table.appendChild(tr);
            return columnSet;
        },
        buildHtmlTable(arr) {
            let table = document.createElement('table', {'border': '1px'}).cloneNode(false),
                columns = this.addAllColumnHeaders(arr, table);
            table.setAttribute("border", "1")
            for (let i = 0, maxi = arr.length; i < maxi; ++i) {
                let tr = document.createElement('tr').cloneNode(false);
                for (let j = 0, maxj = columns.length; j < maxj; ++j) {
                    let td = document.createElement('td', 'class="col"').cloneNode(false);
                    td.appendChild(document.createTextNode(arr[i][columns[j]] || ''));
                    tr.appendChild(td);
                }
                table.appendChild(tr);
            }
            return table;
        }
    }
}
</script>
<style scoped>
* {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}
#hello {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 90vh
}
</style>
