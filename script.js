function addNumbers() {
    const num1 = document.getElementById('num1').value;
    const num2 = document.getElementById('num2').value;
    const result = parseInt(num1) + parseInt(num2);

    if (!isNaN(result)) {
        document.getElementById('result').textContent = result;
    } else {
        document.getElementById('result').textContent = 'Invalid input';
    }
}
