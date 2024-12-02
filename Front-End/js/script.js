var attempt = 3; // Variable to count number of attempts.
// Below function Executes on click of login button.
function validate() {
    var username = document.getElementById("uname").value;
    var password = document.getElementById("psw").value;
    if (username == "Admin" && password == "Password") {
        alert("Login successfully");
        window.location = "app.html"; // Redirecting to other page.
        console.log('clicked!')
        return true;
    }
    else {
        attempt--;// Decrementing by one.
        alert("You have" + attempt + " attempts left");
        // Disabling fields after 3 attempts.
        if (attempt == 0) {
            document.getElementById("uname").disabled = true;
            document.getElementById("psw").disabled = true;
            document.getElementById("submit").disabled = true;
            return false;
        }
    }
}