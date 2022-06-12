/*
Урок 5. Задание 1
1. Создать функцию, генерирующую шахматную доску. 
Можно использовать любые html-теги. 
Доска должна быть верно разлинована на черные и белые ячейки.
Строки должны нумероваться числами от 1 до 8, столбцы – латинскими буквами A, B, C, D, E, F, G, H.
*/

var chars = ["A", "B", "C", "D", "E", "F", "G", "H"];

function CreateChessDesk() {

    chessTable = document.createElement("table");
    chessTable.setAttribute("id", "ChessTable");
    document.body.appendChild(chessTable);

    chessTable.border = "0";
    ChessTable.align = "center"

    var whiteCellColor = "DarkGray"
    var blackCellColor = "Gray"

    var colorSwitcher = false;
    for (var i = 0; i < 9; i++) {
        var row = chessTable.insertRow(i);
        colorSwitcher = !colorSwitcher;
        for (var j = 0; j < 9; j++) {
            var cell = row.insertCell(j);
            cell.align = "center";
            if (j == 0 && i > 0) {
                cell.innerHTML = 9 - i;
                cell.style.backgroundColor = "white";
            }
            else {
                if (i == 0 & j > 0) {
                    cell.innerHTML = chars[j - 1];
                }
                else {
                    if (colorSwitcher) {
                        cell.style.backgroundColor = whiteCellColor;
                    }
                    else {
                        cell.style.backgroundColor = blackCellColor;
                    }
                    colorSwitcher = !colorSwitcher;
                }
            }
            cell.style.color = "black";
            cell.style.height = "75px";
            cell.style.width = "75px";
            if (i == 0 && j == 0) {
                cell.style.backgroundColor = "white";
            }
        };
    };
}


CreateChessDesk();