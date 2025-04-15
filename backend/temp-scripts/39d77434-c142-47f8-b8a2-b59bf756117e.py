// File: src/pages/Home.js

import React, { useState, useEffect, useRef } from 'react';
import { generateVisualization } from '../api/generate';
import CodeEditor from '../components/CodeEditor';
import Loader from '../components/Loader';
import OutputPanel from '../components/OutputPanel';
import VisualizationHistory from '../components/VisualizationHistory';

export default function Home() {
  const [language, setLanguage] = useState('Python');
  const [library, setLibrary] = useState('matplotlib');
  const [code, setCode] = useState('');
  const [chartUrl, setChartUrl] = useState('');
  const [output, setOutput] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState([]);
  const genRef = useRef(null);
  const resultRef = useRef(null);

  const LIBRARY_OPTIONS = {
    Python: ['matplotlib', 'plotly'],
    R: ['ggplot2', 'plotly']
  };

  const SAMPLE_CODE = {
    Python: {
      matplotlib: `import matplotlib.pyplot as plt\nplt.plot([1, 2, 3], [4, 5, 6])\nplt.title("Sample Chart")\nplt.savefig('results/39d77434-c142-47f8-b8a2-b59bf756117e.png')`,
      plotly: `import plotly.express as px\nfig = px.bar(x=[1, 2, 3], y=[4, 5, 6])\nfig.write_html('results/39d77434-c142-47f8-b8a2-b59bf756117e.html')`
    },
    R: {
      ggplot2: `library(ggplot2)\ndata <- data.frame(x=c(1,2,3), y=c(4,5,6))\np <- ggplot(data, aes(x, y)) + geom_bar(stat='identity')\nggsave('results/39d77434-c142-47f8-b8a2-b59bf756117e.png', plot=p)`,
      plotly: `library(plotly)\np <- plot_ly(x=c(1,2,3), y=c(4,5,6), type='bar')\nhtmlwidgets::saveWidget(p, 'results/39d77434-c142-47f8-b8a2-b59bf756117e.html')`
    }
  };

  useEffect(() => {
    setCode(SAMPLE_CODE[language][library]);
    fetchHistory();
  }, [language, library]);

  const handleGenerate = async () => {
    setChartUrl('');
    setOutput('');
    setError('');
    setLoading(true);

    try {
      const data = await generateVisualization({ language, code, library });
      setChartUrl(data.chartUrl);
      setOutput(data.executionOutput);

      setTimeout(() => {
        resultRef.current?.scrollIntoView({ behavior: 'smooth' });
      }, 100);

      fetchHistory();
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const fetchHistory = async () => {
    try {
      const res = await fetch('http://127.0.0.1:5000/api/history');
      const data = await res.json();
      setHistory(data.files || []);
    } catch {
      console.warn('Could not fetch history.');
    }
  };

  const scrollToGenerator = () => {
    genRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-sky-500 to-emerald-500 text-white font-sans">
      {/* Top Navigation Bar */}
      <header className="fixed top-0 left-0 w-full backdrop-blur-sm bg-white/10 border-b border-white/10 z-50 px-6 py-4 flex justify-between items-center">
        <h1 className="text-xl font-bold tracking-wide text-white">NeoPlot</h1>
        <nav className="space-x-6 text-sm font-medium">
          <a href="#" className="text-white hover:underline">Home</a>
          <a href="#" onClick={scrollToGenerator} className="text-white hover:underline">Generate</a>
          <a href="#history" className="text-white hover:underline">History</a>
        </nav>
      </header>

      {/* Hero Section */}
      <section className="h-screen flex flex-col items-center justify-center text-center px-6 pt-20">
        <h1 className="text-5xl font-extrabold text-white drop-shadow-lg mb-4">
          Visualize with Code
        </h1>
        <p className="text-white/80 text-lg max-w-2xl mb-8">
          Select your language and library, then generate stunning data visualizations.
        </p>
        <button
          onClick={scrollToGenerator}
          className="bg-white text-gray-900 px-8 py-3 rounded-lg font-semibold shadow-lg hover:bg-gray-100 transition text-lg"
        >
         Start Generating
        </button>
      </section>

      {/* Generation Area */}
      <section ref={genRef} className="py-20 px-6">
        <div className="max-w-8xl mx-auto bg-[#161a1d] border border-gray-800 rounded-2xl shadow-2xl p-10 grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Code & Controls Left */}
          <div className="flex flex-col">
            <div className="flex items-center gap-4 mb-4">
              <select
                value={language}
                onChange={(e) => setLanguage(e.target.value)}
                className="p-2 bg-gray-900 border border-gray-700 rounded-md text-sm"
              >
                <option value="Python">Python</option>
                <option value="R">R</option>
              </select>
              <select
                value={library}
                onChange={(e) => setLibrary(e.target.value)}
                className="p-2 bg-gray-900 border border-gray-700 rounded-md text-sm"
              >
                {LIBRARY_OPTIONS[language].map((lib) => (
                  <option key={lib} value={lib}>{lib}</option>
                ))}
              </select>
              <button
                onClick={handleGenerate}
                className="ml-auto bg-gradient-to-r from-indigo-500 to-sky-500 hover:to-sky-600 text-white px-4 py-2 text-sm rounded-md font-semibold shadow"
              >
                {loading ? 'Generating...' : 'Generate'}
              </button>
            </div>

            <div className="flex-grow">
              <CodeEditor code={code} setCode={setCode} />
            </div>
          </div>

          {/* Output Right */}
          <div className="relative">
            {loading && <Loader />}
            <OutputPanel chartUrl={chartUrl} output={output} resultRef={resultRef} />
          </div>
        </div>
      </section>

      {/* History Section */}
      <section id="history">
        <VisualizationHistory history={history} />
      </section>
    </div>
  );
}
