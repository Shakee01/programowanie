let size = 10;
let orderElement = 1;

const init = () => {
const btn = document.createElement('button');
const btnreset = document.createElement('button');
btn.textContent = "Dodaj 10 elementów listy";
btnreset.textContent = "Wyczyść listę";
btn.style.fontSize = "28px";
document.body.appendChild(btn);
const ul = document.createElement('ul');
ul.style.listStyleType = "none";
document.body.appendChild(ul);
btn.addEventListener('click', createLiElements);
btnreset.addEventListener('click', cleanList)
}

const createLiElements = () => {
for (let i = 0; i < 10; i++) {
    const li = document.createElement('li');
    li.textContent = `Element ${orderElement++}`;
    li.style.fontSize = `${size++}px`;
    document.querySelector('ul').appendChild(li);
}
}

const cleanList = () => {
document.querySelector('ul').innerHTML = '';
 size = 10;
 orderElement = 1;
init();
}