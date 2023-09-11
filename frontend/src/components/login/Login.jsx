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
    <div className="login__section">
      <div className="login__container">
         <div className="login__containerLeft">
              <h1>Logga in</h1>
              <p className='login__textLeft'>Se till att logga in idag och boka din tvättid!</p>
              <input type="email" name='email' placeholder="Email" value={loginData.email} onChange={handleLoginChange}/>
              <input type="password" name='password' placeholder="Lösenord" value={loginData.password} onChange={handleLoginChange}/><br/>
              <button className='login__buttonLeft' onClick={handleLoginSubmit}>Logga in</button>
         </div>
      </div>
      <div className="login__register">
          <div className="login__containerRight">
              <h2>Hallå granne!</h2>
              <p>Se till att komma igång och boka tvättider idag</p>
              <input type="text" placeholder='Förnamn' />
              <input type="text" placeholder='Efternamn' />
              <input type="email" placeholder="Email"/>
              <input type="password" placeholder="Lösenord"/><br/>
              <button className='login__buttonRight'>Registrera dig</button>
          </div>
      </div>  
    </div>
  )
}

export default Login
