"use client";
import React, { useState } from "react";
import axios from 'axios';
import "./styles/homepage.css";

function Page() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [balance, setBalance] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://127.0.0.1:8000/api/user/", {
        email: email,
        password: password,
        balance: balance,
      });
      console.log(response.data);
    } catch (error) {
      console.error("Error:", error);
    }
  };



  return (
    <div className="homepage">
      <div className="container">
        <form>
          <div className="input-container">
            <label htmlFor='email'>Email:</label>
            <input type="email" id="email" value={email} onChange={(e) => setEmail(e.target.value)} />
          </div>

          <div className="input-container">
            <label>Password:</label>
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
          </div>

          <div className="input-container">
            <label>Balance:</label>
            <input type="number" value={balance} onChange={(e) => setBalance(e.target.value)} />
          </div>

          <button type="submit" onClick={handleSubmit}>Submit</button>
        </form>
      </div>
    </div>
  );
}

export default Page;
