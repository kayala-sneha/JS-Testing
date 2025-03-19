// test.js

// Testing the add function

function testAdd() {
    const result = add(2, 3);
    if (result === 5) {
        console.log('Test passed: add(2, 3) equals 5');
    } else {
        console.error(`Test failed: add(2, 3) equals ${result}`);
    }

    const result2 = add(-1, 1);
    if (result2 === 0) {
        console.log('Test passed: add(-1, 1) equals 0');
    } else {
        console.error(`Test failed: add(-1, 1) equals ${result2}`);
    }

    const result3 = add(0, 0);
    if (result3 === 0) {
        console.log('Test passed: add(0, 0) equals 0');
    } else {
        console.error(`Test failed: add(0, 0) equals ${result3}`);
    }
}

// Run the test
testAdd();
