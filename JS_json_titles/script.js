let input = document.getElementById('siteExample');
let btn = document.getElementById('button');
let resultList = document.getElementById('resultList');

btn.addEventListener("click", add);

function add() {
    $.ajax({
        url: 'https://jsonplaceholder.typicode.com/todos',
        datatype: 'json',
        success: function(result) {
            let titles = [];
            for (let i = 0; i < result.length; i++) {
                titles.push(result[i].title);
                };

            $.each(titles, function(index, title) {
                let li = document.createElement("li");
                li.textContent = title;
                resultList.appendChild(li);
            });
        }
    })
}

