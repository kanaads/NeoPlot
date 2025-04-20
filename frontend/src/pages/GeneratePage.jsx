// File: src/pages/GeneratePage.js

import React, { useState, useEffect, useRef } from 'react';
import { generateVisualization } from '../api/generate';
import CodeEditor from '../components/CodeEditor';
import Loader from '../components/Loader';
import OutputPanel from '../components/OutputPanel';
import NavBar from '../components/NavBar'; 

export default function GeneratePage() {
  const [language, setLanguage] = useState('Python');
  const [library, setLibrary] = useState('matplotlib');
  const [code, setCode] = useState('');
  const [chartUrl, setChartUrl] = useState('');
  const [output, setOutput] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const resultRef = useRef(null);

  const LIBRARY_OPTIONS = {
    Python: ['matplotlib', 'plotly'],
    R: ['ggplot2', 'plotly'],
  };

  const SAMPLE_CODE = {
    Python: {
      matplotlib: `import matplotlib.pyplot as plt\nplt.plot([1, 2, 3], [4, 5, 6])\nplt.title("Sample Chart")`,
      plotly: `import plotly.express as px\nfig = px.bar(x=[1, 2, 3], y=[4, 5, 6])\nimport plotly.io as pio\npio.write_html(fig, file='output.html', auto_open=False)`
    },
    R: {
      ggplot2: `library(ggplot2)\ndata <- data.frame(x=c(1,2,3), y=c(4,5,6))\np <- ggplot(data, aes(x, y)) + geom_bar(stat='identity')\nggsave('output.png')`,
      plotly: `library(plotly)\nlibrary(htmlwidgets)\np <- plot_ly(x=c(1,2,3), y=c(4,5,6), type='bar')\nhtmlwidgets::saveWidget(p, file='output.html', selfcontained = FALSE)`
    }
  };

  useEffect(() => {
    setCode(SAMPLE_CODE[language][library]);
  }, [language, library]);

  const handleGenerate = async () => {
    setChartUrl('');
    setOutput('');
    setError('');
    setLoading(true);

    try {
      const data = await generateVisualization({ language, code, library });
      const timestampedUrl = `${data.url}?t=${Date.now()}`; // Cache busting
      setChartUrl(timestampedUrl);
      setOutput(data.executionOutput || '');

      setTimeout(() => {
        resultRef.current?.scrollIntoView({ behavior: 'smooth' });
      }, 100);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-[#161a1d] text-white font-sans">
      <NavBar /> {/* Render NavBar at the top */}
      
      <main className="pt-28 px-8 pb-12 max-w-7xl mx-auto">
        <div className="flex flex-col lg:flex-row gap-6 bg-[#1e2226] border border-gray-800 rounded-2xl shadow-2xl p-6">
          <div className="flex flex-col flex-1">
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
                className="ml-auto bg-gradient-to-r from-green-400 to-emerald-500 hover:to-emerald-600 text-white px-4 py-2 text-sm rounded-md font-semibold shadow"
              >
                {loading ? 'Generating...' : 'Generate'}
              </button>
            </div>

            <div className="flex-grow">
              <CodeEditor code={code} setCode={setCode} language={language} />
            </div>
          </div>

          <div className="flex-1 relative">
            {loading && <Loader />}
            <OutputPanel chartUrl={chartUrl} output={output} resultRef={resultRef} />
          </div>
        </div>
      </main>
    </div>
  );
}
