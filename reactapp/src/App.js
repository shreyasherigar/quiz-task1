import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import './App.css';
import Login from './component/Login';
import Home from './component/Home'; 
const user = localStorage.getItem('token');

function App() {
  return (
    <div>
   
    <BrowserRouter>
      <Routes>
        
        <Route path="/home" element={<Home />} />
       <Route path="/" element={<Login />} />
       
        </Routes>
    </BrowserRouter>

    </div>
  );
}

export default App;
