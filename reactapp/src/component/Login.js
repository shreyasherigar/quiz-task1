import React, { useState } from 'react';
import './Login.css';

import axios from 'axios';

import {useNavigate } from "react-router-dom";

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/login/', {
        username: username,
        password: password
      });
      console.log(response)
      if (response.status===200){
        localStorage.setItem('username',username);
        // console.log(response.data.user_id)
        navigate('/home',{state:{"user_id":response.data.user_id}})
      }
      
    } catch (error) {
      setError('Error logging in. Please check your credentials.');
      console.error('Error logging in:', error);
    }
  };

  return (
    <div>
        <h1>Login page</h1>
      <div className="login-page">
        <form className="login-form" onSubmit={handleLogin}>
          <input
            type="text"
            placeholder="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
          <input
            type="password"
            placeholder="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <button type="submit">Login</button>
        </form>
      </div>
      {error && <p className="error-message">{error}</p>}
    </div>
  );
};

export default Login;
