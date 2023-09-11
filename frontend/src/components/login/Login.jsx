import React, { useState } from 'react'
import "./login.css"

function Login() {

  const [loginData, setLoginData] = useState({
    email: '',
    password: ''
  });

  const [registerData, setRegisterData] = useState({
    first_name: '',
    last_name: '',
    email: '',
    password: ''
  });

  const handleLoginChange = (event) => {
    const { name, value } = event.target;
    setLoginData({ ...loginData, [name]: value })
  };

  const handleLoginSubmit = (event) => {
    event.preventDefault();
    console.log(loginData);
  }

  const handleRegisterChange = (event) => {
    const { name, value } = event.target;
    setRegisterData({ ...registerData, [name]: value })
  }

  const handleRegisterSubmit = (event) => {
    event.preventDefault();
    console.log(loginData);
  }


  return (
    <div class="login__section">
      <div class="login__container">
         <div class="login__containerLeft">
              <h1>Logga in</h1>
              <input type="email" name='email' placeholder="Email" value={loginData.email} onChange={handleLoginChange}/>
              <input type="password" name='password' placeholder="Lösenord" value={loginData.password} onChange={handleLoginChange}/><br/>
              <button className='login__buttonLeft' onClick={handleLoginSubmit}>Logga in</button>
         </div>
      </div>
      <div class="login__register">
          <div class="login__containerRight">
              <h2>Hallå granne!</h2>
              <p>Se till att komma igång och boka tvättider idag</p>
              <input type="text" name='first_name' placeholder='Förnamn' value={registerData.first_name} onChange={handleRegisterChange}/>
              <input type="text" name='last_name' placeholder='Efternamn' value={registerData.last_name} onChange={handleRegisterChange}/>
              <input type="email" name='email' placeholder="Email" value={registerData.email} onChange={handleRegisterChange}/>
              <input type="password" name='password' placeholder="Lösenord" value={registerData.password} onChange={handleRegisterChange}/><br/>
              <button className='login__buttonRight' onClick={handleRegisterSubmit}>Registrera dig</button>
          </div>
      </div>  
    </div>
  )
}

export default Login