/* 1. Написать функцию, преобразующую число в объект. Передавая на вход число от 0 до 999, 
надо получить на выходе объект, в котором в соответствующих свойствах описаны единицы, десятки и сотни. 
Например, для числа 245 надо получить следующий объект: {‘единицы’: 5, ‘десятки’: 4, ‘сотни’: 2}. 
Если число превышает 999, необходимо выдать соответствующее сообщение с помощью console.log и вернуть пустой объект. */

var numberObject = {
    'сотни': 0,
    'десятки': 0,
    'единицы': 0
};


var testNumber = 1245;
var testResult = numberToObject(testNumber);

function numberToObject(number) {

    if (number > 999) {
        console.log("Число не в диапазоне [0;999]");
        return null;
    }

    var hundreds = Math.trunc(number / 100);
    var ten = Math.trunc((number - hundreds * 100) / 10);
    var units = Math.trunc(number - hundreds * 100 - ten * 10);

    numberObject.сотни = hundreds;
    numberObject.десятки = ten;
    numberObject.единицы = units;

    return numberObject;
}