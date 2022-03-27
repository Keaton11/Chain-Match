import React, { useState, useCallback } from 'react';
import { Link } from "react-router-dom";

const Matching = () => {
  const [username, setUsername] = useState("");
  const handleChange = useCallback((newValue) => setUsername(newValue.target.value));

  const serverConnect = () => {
    // var xhr = new XMLHttpRequest();
    // xhr.open('POST', '127.0.0.1:8000');
    // xhr.send(JSON.stringify({}));
    const playerInfo = { id: username, adddress: "terra1r3z46gdgtzzjjjweldwsuvdtv8hf2859t5vl0"};
    fetch("127.0.0.1:8000", { method: "POST", body: JSON.stringify(playerInfo)})
		.then((response) => {
            console.log(response);
        });
  }

  return (
    <>
      <div id="home-main-container">
        <header id="home-header">
          <h1>CHAIN MATCH</h1>
          <p>VERSION 0.0002</p>
        </header>
        <div id="matching-container">
          <form id="matching-form">
            <label for="username">Input a username:</label>
            <input type="text" id="username" name="username" onChange={handleChange}></input>
          </form> 
          <Link to="/match">
            <button id="matching-button" onClick={serverConnect}>
              Submit
            </button>
          </Link>
        </div>
        <footer id="home-footer">
          <p>Looking for a match ...</p>
        </footer>
      </div>
    </>
  );
}
  
export default Matching;
