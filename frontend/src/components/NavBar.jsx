import React from 'react';
import { Link, useLocation } from 'react-router-dom';

export default function NavBar() {
  const location = useLocation();

  const getLinkClass = (path) => {
    const isActive = location.pathname === path;
    return `text-sm font-medium ${isActive ? 'text-green-400' : 'text-white hover:text-green-600'}`;
  };

  return (
    <header className="fixed top-0 left-0 w-full bg-black/80 backdrop-blur-sm shadow-lg border-b border-gray-700 z-50 px-6 py-4 flex justify-between items-center">
      <h1 className="text-xl font-bold tracking-wide text-white">NeoPlot</h1>
      <nav className="space-x-6">
        <Link to="/" className={getLinkClass("/")}>Home</Link>
        <Link to="/generate" className={getLinkClass("/generate")}>Generate</Link>
        <Link to="/history" className={getLinkClass("/history")}>History</Link>
      </nav>
    </header>
  );
}
