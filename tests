"use strict";

const assert = require("node:assert/strict");
const student = require("./student-template.js");

function test(name, fn) {
  try {
    fn();
    console.log(`✓ ${name}`);
  } catch (error) {
    console.error(`✗ ${name}`);
    console.error(`  ${error.message}`);
    process.exitCode = 1;
  }
}

test("1. Сумма диапазона", () => {
  assert.equal(student.sumRange(1, 5), 15);
  assert.equal(student.sumRange(5, 5), 5);
  assert.equal(student.sumRange(-3, 3), 0);
  assert.equal(student.sumRange(10, 12), 33);
});

test("2. Возведение в степень", () => {
  assert.equal(student.power(2, 5), 32);
  assert.equal(student.power(7, 0), 1);
  assert.equal(student.power(5, 1), 5);
  assert.equal(student.power(-2, 4), 16);
  assert.equal(student.power(-2, 3), -8);
});

test("3. Факториал", () => {
  assert.equal(student.factorial(0), 1);
  assert.equal(student.factorial(1), 1);
  assert.equal(student.factorial(5), 120);
  assert.equal(student.factorial(7), 5040);
});

test("4. Количество чётных чисел", () => {
  assert.equal(student.countEven(1, 10), 5);
  assert.equal(student.countEven(2, 2), 1);
  assert.equal(student.countEven(3, 3), 0);
  assert.equal(student.countEven(-4, 4), 5);
});

test("5. Первое число, кратное делителю", () => {
  assert.equal(student.findFirstDivisible(10, 20, 7), 14);
  assert.equal(student.findFirstDivisible(1, 5, 6), null);
  assert.equal(student.findFirstDivisible(12, 20, 4), 12);
  assert.equal(student.findFirstDivisible(-5, 5, 3), -3);
});

test("6. Строка таблицы умножения", () => {
  assert.equal(student.multiplicationLine(3, 5), "3 6 9 12 15");
  assert.equal(student.multiplicationLine(5, 1), "5");
  assert.equal(student.multiplicationLine(2, 4), "2 4 6 8");
  assert.equal(student.multiplicationLine(-2, 3), "-2 -4 -6");
});

if (!process.exitCode) {
  console.log("\nВсе тесты пройдены.");
}
