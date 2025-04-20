// File: src/pages/HistoryPage.js

import React, { useEffect, useState } from 'react';
import { fetchVisualizationHistory } from '../api/history';
import NavBar from '../components/NavBar';

export default function HistoryPage() {
  const [entries, setEntries] = useState([]);

  useEffect(() => {
    const loadHistory = async () => {
      const data = await fetchVisualizationHistory();
      // Sort by createdAt descending (newest first)
      const sortedData = data.sort((a, b) => b.createdAt - a.createdAt);
      setEntries(sortedData);
    };
    loadHistory();
  }, []);

  return (
    <div className="min-h-screen bg-[#161a1d] text-white font-sans">
      <NavBar />
      <main className="pt-32 px-8 pb-12 max-w-7xl mx-auto">
        <h1 className="text-4xl font-extrabold mb-8 text-white drop-shadow">
          Visualization History
        </h1>
        <div className="overflow-x-auto bg-[#1e2226] border border-gray-800 rounded-2xl shadow-2xl p-6">
          <table className="w-full text-left border-collapse">
            <thead className="bg-gray-800 text-sm uppercase tracking-wider">
              <tr>
                <th className="p-3 border-b border-gray-700">SL No</th>
                <th className="p-3 border-b border-gray-700">Preview</th>
                <th className="p-3 border-b border-gray-700">Filename</th>
                <th className="p-3 border-b border-gray-700">Type</th>
                <th className="p-3 border-b border-gray-700">Language</th>
                <th className="p-3 border-b border-gray-700">Library</th>
                <th className="p-3 border-b border-gray-700">Created On</th>
                <th className="p-3 border-b border-gray-700">Actions</th>
              </tr>
            </thead>
            <tbody>
              {entries.map((entry, index) => (
                <tr key={entry.url} className="hover:bg-gray-800 transition text-sm">
                  <td className="p-3 border-b border-gray-700">{index + 1}</td>
                  <td className="p-3 border-b border-gray-700">
                    {entry.type === 'png' ? (
                      <img
                        src={`http://localhost:5000${entry.url}`}
                        alt={entry.filename}
                        className="h-16 w-auto object-contain"
                      />
                    ) : (
                      <div className="h-16 flex items-center justify-center text-xs italic text-gray-400">
                        Interactive Plot
                      </div>
                    )}
                  </td>
                  <td className="p-3 border-b border-gray-700">{entry.filename}</td>
                  <td className="p-3 border-b border-gray-700">{entry.type}</td>
                  <td className="p-3 border-b border-gray-700">{entry.language}</td>
                  <td className="p-3 border-b border-gray-700">{entry.library}</td>
                  <td className="p-3 border-b border-gray-700">
                    {new Date(parseFloat(entry.createdAt) * 1000).toLocaleString()}
                  </td>
                  <td className="p-3 border-b border-gray-700 space-x-4">
                    <a
                      href={`http://localhost:5000${entry.url}`}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-sky-400 hover:underline"
                    >
                      View
                    </a>
                    <a
                      href={`http://localhost:5000${entry.url}?download=true`}
                      download={entry.filename}
                      className="text-blue-400 hover:underline"
                    >
                      Download
                    </a>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </main>
    </div>
  );
}
