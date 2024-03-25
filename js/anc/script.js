// script.js
function checkPassword() {
    const enteredPassword = document.getElementById('password').value;
    const secretPassword = 'reverie'; // Change this to your desired password

    if (enteredPassword === secretPassword) {
        document.getElementById('hidden-content').style.display = 'block';
    } else {
        alert('Incorrect password. Try again.');
    }
}

