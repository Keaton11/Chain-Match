import React, { useState } from 'react';
import { Link } from "react-router-dom";

const HomeButtons = () => {
  const [selectMode, setSelectMode] = useState(false);

  return (
    (!selectMode) ? (
      <button className="home-button" onClick={() => setSelectMode(true)}>PLAY</button>
    ) : (
      <Link to="/matching" className="linked-buttons">
        <button className="home-button">QUICK MATCH</button>
        <button className="home-button">MATCH WITH FRIENDS</button>
        <button className="home-button">OTHER</button>
      </Link>
    )
  )
}

export default HomeButtons;