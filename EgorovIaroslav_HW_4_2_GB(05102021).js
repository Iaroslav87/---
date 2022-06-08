/* 2. Продолжить работу с интернет-магазином:
    a. В прошлом домашнем задании вы реализовали корзину на базе массивов. 
    Какими объектами можно заменить их элементы?
    b. Реализуйте такие объекты.
    c. Перенести функционал подсчета корзины на объектно-ориентированную базу.
*/

var basket = [
    { product: "Sprite", count: 5, price: 90 },
    { product: "Fanta", count: 2, price: 85 },
    { product: "Juice", count: 1, price: 110 },
    { product: "Water", count: 1, price: 25 },
];

var price = [
    { product: "Sprite", price: 90 },
    { product: "Fanta", price: 85 },
    { product: "Juice", price: 110 },
    { product: "Water", price: 25 },
];

var summBasket = countBasketPrice(basket);

function countBasketPrice(items) {
    var summ = 0;
    var index = 0;
    for (items in basket) {
        summ += basket[items].count * basket[items].price;
        console.log(
            basket[items].product + ": " +
            basket[items].count + "*" +
            basket[items].price + "=" +
            basket[items].count * basket[items].price
        )
    }
    return (summ);
}