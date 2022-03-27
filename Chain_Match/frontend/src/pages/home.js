import React, { useState } from 'react';
import homeButtons from './homeButtons';

const Home = () => {
  return (
    <>
      <div id="home-main-container">
        <header id="home-header">
          <h1>CHAIN MATCH</h1>
          <p>VERSION 0.0002</p>
        </header>
        <div id="home-button-container">
          {homeButtons()}
        </div>
        <footer id="home-footer">
          <p>Welcome to Chain Match!</p>
        </footer>
      </div>
    </>
  );
}
  
export default Home;
