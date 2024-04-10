const express = require('express');

const app = express();
const port = 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));


function calculateBMI(feet, inches, weight) {
  
  const totalInches = feet * 12 + inches;
  const meters = totalInches * 0.025;
  const kilograms = weight * 0.45;

  const bmi = kilograms / Math.pow(meters,2);
  return Math.round(bmi * 10) / 10;
  
}

function getBMICategory(bmi) {
  
  if (bmi < 18.5) return "Underweight";
  else if (bmi >= 18.5 && bmi <25) return "Normal weight";
  else if (bmi >= 25 && bmi < 30) return "Overweight";
  else return "Obese";
};


app.get('/', (req, res) => {
  res.sendFile('SW-Testing-Assn2/public/index.html');
});

app.post('/calculate', (req, res) => {
  const { feet, inches, weight } = req.body;
  const userBMI = calculateBMI(parseInt(feet), parseInt(inches), parseInt(weight));
  const userCategory = getBMICategory(userBMI);
  res.send(`You have a BMI of ${userBMI}. You are ${userCategory}.`);
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});

module.exports = {calculateBMI, getBMICategory};