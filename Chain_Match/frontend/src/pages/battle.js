import React, {useState, useEffect} from 'react';

const Battle = () => {
  const [countDown, setCountDown] = useState(100);

  useEffect(() => {
    const timer = setInterval(() => { setCountDown(countDown-1) }, 120);
    return () => clearInterval(timer);
  });

  const displayTimer = () => {
    if (countDown < 0) {
      return "TIME UP!";
    } else {
      let minutes = Math.floor(countDown / 60);
      let seconds = countDown % 60;
      (minutes < 10) && (minutes = '0' + minutes);
      (seconds < 10) && (seconds = '0' + seconds);
      return minutes + ":" + seconds;
    }
  }

  return (
    <div id="battle">
      <div id="battle-timer">
        <h1>{displayTimer()}</h1>
      </div>
      <button id="battle-select-winner">Select Winner</button>
      <div id="battle-rounds">
        <div></div>
        <div></div>
        <div></div>
        <div></div>
      </div>
      <div id="battle-chatbox">
        <span>
          <h2>Chat</h2>
        </span>
        <div></div>
      </div>
    </div>
  );
}

export default Battle;
    
