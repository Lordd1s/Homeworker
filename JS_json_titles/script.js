let input = document.getElementById('siteExample');
let btn = document.getElementById('button');


btn.addEventListener("click", add);

function add() {
    $.ajax({
        url: 'https://jsonplaceholder.typicode.com/todos',
        datatype: 'json',
        success: function(result) {
            let titleDoc = result['title']
            $.each(titleDoc, function(index, title){
                console.log(title);
            })
        }
    })
}