// С помощью цикла while вывести все простые числа в промежутке от 0 до 100.

var startCount = 2;
var endCount = 100;
var currentCount = startCount;

while (endCount >= startCount) {
    var currentCount = 2;
    var simple = true;

    while (currentCount <= endCount / 2) {
        if (endCount % currentCount == 0) {
            simple = false;
            break;
        }
        currentCount++;
    }
    if (simple)
        console.log(endCount);
    endCount--;
}