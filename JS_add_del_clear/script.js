let getImg = document.getElementById('formFileLg');
let addBtn = document.getElementById('btn');
let container = document.getElementById('img-cont');
let clearBtn = document.getElementById('clear');
btn.addEventListener("click", add);
clearBtn.addEventListener("click", clear);


function add() {
    let file = getImg.files[0]; // вот это не понял
    let reader = new FileReader(); // вот это тоже

    reader.readAsDataURL(file); // вот это
    // нижний код
    reader.onload = function() {
        let box = document.createElement('div')
        box.className = 'container'
        let img = document.createElement('img');
        img.src = reader.result; // this string
        img.alt = file.name; // this string
        img.style.width = '500px';
        img.style.height = 'auto';
        img.className = 'mt-2';
        let deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'Delete';
        deleteBtn.className = "btn btn-danger m-2 p-2";
        box.appendChild(img); // this
        box.appendChild(deleteBtn); // this
        container.appendChild(box) // and this

        deleteBtn.addEventListener('click', function() {
            box.remove();
        });
    }
}

function clear(){
    container.innerHTML = '';
}