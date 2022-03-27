import React from 'react';
import { Link } from "react-router-dom";

const Opponent = () => {
  return (
    <div id="match">
      <div id="match-main-container">
        <div id="match-player1">
          <div id="match-player1-info">
            <h1>Player 1</h1>
          </div>
        </div>
      <div id="match-player2">
        <div id="match-player2-info">
          <h1>Player 2</h1>
            <div id="match-button-container">
              <Link to="/battle">
                <button>Accept</button>
              </Link>
              <button>Reject</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
  
export default Opponent;
