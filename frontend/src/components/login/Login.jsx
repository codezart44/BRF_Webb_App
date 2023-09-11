import React, { useState, useEffect } from 'react';
import './login.css';

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

  const [successModalVisible, setSuccessModalVisible] = useState(false);
  const [failModalVisible, setFailModalVisible] = useState(false);

  const handleLoginChange = (event) => {
    const { name, value } = event.target;
    setLoginData({ ...loginData, [name]: value });
  };

  const handleLoginSubmit = (event) => {
    event.preventDefault();
    console.log(loginData);
  };

  const handleRegisterChange = (event) => {
    const { name, value } = event.target;
    setRegisterData({ ...registerData, [name]: value });
  };

  const handleRegisterSubmit = (event) => {
    event.preventDefault();
    console.log(registerData);
    fetch('http://127.0.0.1:5000/auth/register', 
        {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify(registerData)
        })
        .then(response => response.text())
        .then(response => console.log(response))
        .catch(error => console.error('Error with register', error))
    
  };

  return (
    <div className="login__section">
      <div className="login__container">
        <div className="login__containerLeft">
          <h1>Logga in</h1>
          <p>Se om tvättstugan är ledig genom att logga in</p>
          <input
            type="email"
            name="email"
            placeholder="Email"
            value={loginData.email}
            onChange={handleLoginChange}
          />
          <input
            type="password"
            name="password"
            placeholder="Lösenord"
            value={loginData.password}
            onChange={handleLoginChange}
          />
          <br />
          <button className="login__buttonLeft" onClick={handleLoginSubmit}>
            Logga in
          </button>
          <button
            onClick={() => {
              setSuccessModalVisible(!successModalVisible);
              setFailModalVisible(false);
            }}
          >
            success
          </button>
          <button
            onClick={() => {
              setFailModalVisible(!failModalVisible);
              setSuccessModalVisible(false);
            }}
          >
            fail
          </button>
        </div>
      </div>
      <div className="login__register">
        <div className="login__containerRight">
          <h2 className="login__textRight">Hallå granne!</h2>
          <p className="login__textRight">Om du inte har ett konto, gör ett idag!</p>
          <input
            type="text"
            name="first_name"
            placeholder="Förnamn"
            value={registerData.first_name}
            onChange={handleRegisterChange}
          />
          <input
            type="text"
            name="last_name"
            placeholder="Efternamn"
            value={registerData.last_name}
            onChange={handleRegisterChange}
          />
          <input
            type="email"
            name="email"
            placeholder="Email"
            value={registerData.email}
            onChange={handleRegisterChange}
          />
          <input
            type="password"
            name="password"
            placeholder="Lösenord"
            value={registerData.password}
            onChange={handleRegisterChange}
          />
          <br />
          <button className="login__buttonRight" onClick={handleRegisterSubmit}>
            Registrera dig
          </button>
        </div>
      </div>

      {successModalVisible && (
        <div className="modal">
          <div className="modal-content">
            <h3>Bra jobbat!</h3>
            <p>Kontot är skapat nu är det bara att boka din tvättid</p>
            <button
              onClick={() => {
                setSuccessModalVisible(false);
              }}
            >
              Close
            </button>
          </div>
        </div>
      )}

      {failModalVisible && (
        <div className="modal">
          <div className="modal-content">
            <h3>Fel!</h3>
            <p>Mejl adressen som du angett används redan, testa att avända en annan</p>
            <button
              onClick={() => {
                setFailModalVisible(false);
              }}
            >
              Close
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

export default Login;

