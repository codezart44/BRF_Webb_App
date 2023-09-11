import React from 'react'
import "./login.css"

function Login() {
  return (
    <div class="login__section">
      <div class="login__container">
         <div class="login__containerLeft">
              <h1>Logga in</h1>
              <input type="email" placeholder="Email"/>
              <input type="password" placeholder="Lösenord"/><br/>
              <button className='login__buttonLeft'>Logga in</button>
         </div>
      </div>
      <div class="login__register">
          <div class="login__containerRight">
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
