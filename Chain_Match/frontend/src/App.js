import React from 'react';
import { Routes, Route } from 'react-router-dom';
import './styles.css';

import Home from './pages/home';
import Match from './pages/match';
import Matching from './pages/matching';
import Battle from './pages/battle';

const App = () => {
  return (
    <Routes>
      <Route exact path='/' element={<Home />}></Route>
      <Route exact path='/match' element={<Match />}></Route>
      <Route exact path='/matching' element={<Matching />}></Route>
      <Route exact path='/battle' element={<Battle />}></Route>
    </Routes>
  );
}

export default App;
