/*
2. Сделать генерацию корзины динамической: верстка корзины не должна
находиться в HTML-структуре. Там должен быть только div, в который
будет вставляться корзина, сгенерированная на базе JS:
a. Пустая корзина должна выводить строку «Корзина пуста»;
b. Наполненная должна выводить «В корзине: n товаров на сумму m
рублей».
*/

document.querySelector('body').insertAdjacentHTML('afterbegin',
    '<div><a href="#" onclick="basket.totalPrice()" style="text-decoration: none"><h1>Корзина</h1></a></div>');

document.querySelector('div').insertAdjacentHTML('afterend',
    '<div><a href="#" onclick="basket.information()" style="text-decoration: none"><i>подробнее</i></a></div>');

const basket = {
    goods: [{ name: 'Jersey', cost: 3500, quantity: 3 },
    { name: 'Shoes', cost: 7500, quantity: 4 },
    { name: 'Shorts', cost: 2500, quantity: 3 }],
    totalPrice() {
        let h1Tag = document.querySelector('h1');
        let totalCost = 0
        let totalQuantity = 0
        for (let i = 0; i < this.goods.length; i++) {
            totalCost += this.goods[i]['cost'] * this.goods[i]['quantity']
            totalQuantity += this.goods[i]['quantity']
        }
        if (totalCost === 0) return h1Tag.textContent = 'Корзина пуста';
        else return h1Tag.textContent = `В корзине товаров: ${totalQuantity}. На сумму ${totalCost} рублей`
    },
    information() {
        let iTag = document.querySelector('i')
        let array = []
        for (let i = 0; i < this.goods.length; i++) {
            array.push(`Товар: ${this.goods[i].name}, 
            Стоимость: ${this.goods[i].cost}, 
            Количество: ${this.goods[i].quantity}`)
        }
        return iTag.textContent = `${array}`
    }
}
