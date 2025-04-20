import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import HistoryPage from './pages/HistoryPage';
import GeneratePage from './pages/GeneratePage';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/generate" element={<GeneratePage />} />
      <Route path="/history" element={<HistoryPage />} />
    </Routes>
  );
}

export default App;
  