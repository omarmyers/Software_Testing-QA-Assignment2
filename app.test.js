const { calculateBMI, getBMICategory} = require('./app');

test('Tests correctness of BMI calculator', () => {
  expect(calculateBMI(5, 3, 125)).toBe(22.7);
  expect(calculateBMI(5, 3, 150)).toBe(27.2);
  expect(calculateBMI(5, 9, 178)).toBe(26.9);
  expect(calculateBMI(5, 11, 110)).toBe(15.7);
  expect(calculateBMI(5, 9, 185)).toBe(28);
  
});

test('determines BMI category correctly', () => {
  expect(getBMICategory(18.4)).toBe("Underweight");
  expect(getBMICategory(18.5)).toBe("Normal weight");
  expect(getBMICategory(24.9)).toBe("Normal weight");
  expect(getBMICategory(25)).toBe("Overweight");
  expect(getBMICategory(29.9)).toBe("Overweight");
  expect(getBMICategory(30)).toBe("Obese");
});