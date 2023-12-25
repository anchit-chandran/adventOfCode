import 'dart:io';

int mapWordToNum(String numStr) {
  var wordToNumMap = {
    "zero":0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
  };

  return wordToNumMap[numStr]!;
}

void main() {
  var filePath = 'input.txt';

  var file = File(filePath);
  List<String> contents = [];

  try {
    contents = file.readAsStringSync().split('\n');
  } catch (e) {
    print("Error: $e");
  }

  var pattern = r"(one|two|three|four|five|six|seven|eight|nine|\d)";
  var regex = RegExp(pattern);

  int total = 0;

  for (var line in contents) {
    var matches = regex.allMatches(line).toList();

    var firstNumAsStr = matches.first.group(0)!;
    var lastNumAsStr = matches.last.group(0)!;

    int firstNum = 0;
    int lastNum = 0;

    try {
      firstNum = int.parse(firstNumAsStr);
    } catch (e) {
      firstNum = mapWordToNum(firstNumAsStr);
    }

    try {
      lastNum = int.parse(lastNumAsStr);
    } catch (e) {
      lastNum = mapWordToNum(lastNumAsStr);
    }

    int num = int.parse("$firstNum$lastNum");
    print(num);
    total += num;
  }
  // print(85 + 2)
  print(total);
}
