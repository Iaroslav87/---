/* 1. Продолжаем реализовывать модуль корзины:
a. Добавлять в объект корзины выбранные товары по клику на кнопке
«Купить» без перезагрузки страницы;
b. Привязать к событию покупки товара пересчет корзины и обновление
ее внешнего вида.
*/

cart = {
    items: [],
}

function newItem(name, price) {
    let item = {
        name: name,
        price: price,
    }
    return item
}

item1 = newItem('Кружка', 150)
item2 = newItem('Кружка2', 500)
item3 = newItem('Кружка3', 15)


function countCartPrice(fullCart) {
    let result = 0
    for (let currItem of fullCart.items) {
        result += currItem.price
    }

    return (result)
}

function reloadCart() {
    let textForCart;
    let cart_div = document.getElementById("cart")
    cart_div.innerHTML = ""
    if (cart.items.length > 0) {
        textForCart = 'В корзине: \n' + cart.items.length + ' товар(а, ов)  на сумму ' + countCartPrice(cart) + ' рублей';
    } else {
        textForCart = 'Корзина пуста';
    }
    let p = document.createElement('p')
    p.innerText = textForCart
    cart_div.style.maxWidth = "100px"
    cart_div.appendChild(p)
}

function addToCart(event) {
    cart.items.push(eval(event.target.id))
    reloadCart()
}

window.addEventListener('load', reloadCart)
var buttons = document.getElementsByTagName('button')
for (let button of buttons) {
    button.addEventListener('click', addToCart)
}
