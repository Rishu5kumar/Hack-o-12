function SignUp(){
    var name =  document.getElementById("name").value;
    var email =  document.getElementById("email").value;
    var password =  document.getElementById("password").value;
    fetch(`http://127.0.0.1:5500/register/name=${name}&email=${email}&password=${password}`)
    .then(response=>response.json())
    .then(data=>window.location.href = '../index.html')
    
    }
    function Login(){
    var email =  document.getElementById("lname").value;
    var password =  document.getElementById("lpassword").value;
    fetch(`http://127.0.0.1:5500/login/email=${email}&password=${password}`)
    .then(response=>response.json())
    .then(data=>window.location.href = '../index.html')
    }