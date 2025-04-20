// File: src/pages/HomePage.js

import React from 'react';
import { useNavigate } from 'react-router-dom';
import NavBar from '../components/NavBar';

export default function HomePage() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen relative bg-gradient-to-b from-green-600 to-black text-white font-sans">
      {/* Watermark Background */}
      <div
        className="absolute inset-0 opacity-10 pointer-events-none"
        style={{
          backgroundImage:
            'url(https://images.unsplash.com/photo-1557682260-967a9a9c2c2a?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80)',
          backgroundSize: 'cover',
          backgroundRepeat: 'no-repeat',
          backgroundPosition: 'center',
        }}
      ></div>

      {/* Top Navigation Bar */}
      <NavBar />

      {/* Hero Section */}
      <section className="relative h-screen flex flex-col items-center justify-center text-center px-6 pt-20">
        <h1 className="text-5xl font-extrabold drop-shadow-lg mb-6">
          NeoPlot: Effortless Data Visualization
        </h1>
        <p className="text-white/90 text-lg max-w-2xl mb-8">
          Select your language and library, then generate stunning data visualizations.
        </p>
        <button
          onClick={() => navigate('/generate')}
          className="bg-white text-green-700 font-bold border-2 border-green-600 rounded-full px-8 py-3 transition-all duration-300 hover:text-green-400 hover:shadow-lg"
        >
          Start Generating
        </button>
        <div className="mt-16 grid grid-cols-1 md:grid-cols-3 gap-12">
          <div className="bg-black bg-opacity-60 p-6 rounded-md shadow-lg">
            <h3 className="text-xl font-bold mb-2">🧠 Language Agnostic</h3>
            <p>
              Supports both Python and R, with clean syntax-based code detection and library-specific rendering.
            </p>
          </div>
          <div className="bg-black bg-opacity-60 p-6 rounded-md shadow-lg">
            <h3 className="text-xl font-bold mb-2">📊 Interactive or Static</h3>
            <p>
              Render interactive charts with Plotly or static charts with Matplotlib and ggplot2.
            </p>
          </div>
          <div className="bg-black bg-opacity-60 p-6 rounded-md shadow-lg">
            <h3 className="text-xl font-bold mb-2">📁 Persistent History</h3>
            <p>
              Every visualization is saved with metadata and can be downloaded or viewed anytime in your session.
            </p>
          </div>
        </div>
      </section>
    </div>
  );
}
