"use strict";

// Практическая работа №3
// Тема: функции и циклы.
// Заполните только участки TODO.
// Названия функций, параметры и module.exports не изменяйте.

// 1. Сумма диапазона
function sumRange(from, to) {
  let sum = 0;
  for (let i = from; i <= to; i++) {
    sum = sum + i;
  }
  return sum;
}

// 2. Возведение в степень
function power(base, exponent) {
  let result = 1;
  for (let i = 0; i < exponent; i++) {
    result = result * base;
  }
  return result;
}

// 3. Факториал
function factorial(n) {
  let result = 1;
  for (let i = 1; i <= n; i++) {
    result = result * i;
  }
  return result;
}

// 4. Количество чётных чисел
function countEven(from, to) {
  let count = 0;
  for (let i = from; i <= to; i++) {
    if (i % 2 === 0) {
      count = count + 1;
    }
  }
  return count;
}

// 5. Первое число, кратное делителю
function findFirstDivisible(from, to, divisor) {
  let answer = null;
  for (let i = from; i <= to; i++) {
    if (i % divisor === 0) {
      answer = i;
      break;
    }
  }
  return answer;
}

// 6. Строка таблицы умножения
function multiplicationLine(number, count) {
  let str = "";
  for (let i = 1; i <= count; i++) {
    str = str + (number * i);
    if (i < count) {
      str = str + " ";
    }
  }
  return str;
}

module.exports = {
  sumRange,
  power,
  factorial,
  countEven,
  findFirstDivisible,
  multiplicationLine,
};
