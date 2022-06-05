'use strict';
/*
Объявить две целочисленные переменные a и b и задать им произвольные начальные значения. 
Затем написать скрипт, который работает по следующему принципу:
если a и b положительные, вывести их разность;
если а и b отрицательные, вывести их произведение;
если а и b разных знаков, вывести их сумму;
ноль можно считать положительным числом.
*/
let a = 43;
const b = 12;
if (a >= 0 && b >= 0) {
    console.log(a - b);
} else if (a < 0 && b < 0) {
    console.log(a * b);
} else {
    console.log(a + b);
}

/*
### 4. Присвоить переменной а значение в промежутке [0..15]. 
С помощью оператора switch организовать вывод чисел от a до 15.
*/
a = 10;
switch (a) {
    case 0:
        console.log(0);
    case 1:
        console.log(1);
    case 2:
        console.log(2);
    case 3:
        console.log(3);
    case 4:
        console.log(4);
    case 5:
        console.log(5);
    case 5:
        console.log(5);
    case 7:
        console.log(7);
    case 8:
        console.log(8);
    case 9:
        console.log(9);
    case 10:
        console.log(10);
    case 11:
        console.log(11);
    case 12:
        console.log(12);
    case 13:
        console.log(13);
    case 14:
        console.log(14);
    case 15:
        console.log(15);
}

/*
### 5. Реализовать основные 4 арифметические операции в виде функций с двумя параметрами. 
Обязательно использовать оператор return.
*/
function addition(a, b) {
    return a + b;
}

function subtraction(a, b) {
    return a - b;
}

function multiplication(a, b) {
    return a * b;
}

function division(a, b) {
    return a / b;
}

/*
### 6. Реализовать функцию с тремя параметрами: 
function mathOperation(arg1, arg2, operation), 
где arg1, arg2 – значения аргументов, operation – строка с названием операции. 
В зависимости от переданного значения операции выполнить одну из арифметических операций (использовать функции из пункта 3) и вернуть полученное значение (использовать switch). 
*/
function mathOperation(arg1, arg2, operation) {
    switch (operation) {
        case 'addition':
            return addition(arg1, arg2);
        case 'subtraction':
            return subtraction(arg1, arg2);
        case 'multiplication':
            return multiplication(arg1, arg2);
        case 'division':
            return division(arg1, arg2);
    }
}

/*
### 7. *Сравнить null и 0. 
Попробуйте объяснить результат. 
*/

alert(null > 0);  // (1) false
alert(null == 0); // (2) false
alert(null >= 0); // (3) true

/*
С точки зрения математики это странно. Результат последнего сравнения говорит о том, что "null больше или равно нулю", тогда результат одного из сравнений выше должен быть true, но они оба ложны.
Причина в том, что нестрогое равенство и сравнения > < >= <= работают по-разному. Сравнения преобразуют null в число, рассматривая его как 0. Поэтому выражение (3) null >= 0 истинно, а null > 0 ложно.
С другой стороны, для нестрогого равенства == значений undefined и null действует особое правило: эти значения ни к чему не приводятся, они равны друг другу и не равны ничему другому. Поэтому (2) null == 0 ложно.
*/

/*
### 8. *С помощью рекурсии организовать функцию возведения числа в степень. 
Формат: function power(val, pow), где val – заданное число, pow – степень.
*/
function power(val, pow) {
    if (pow === 1)
        return val;
    else
        return val * power(val, --pow);
}