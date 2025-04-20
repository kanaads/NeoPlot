// File: src/components/OutputPanel.jsx

export default function OutputPanel({ chartUrl, output, resultRef }) {
  if (!chartUrl) {
    return (
      <p className="text-sm text-gray-400 italic text-center" ref={resultRef}>
        Your generated visualization will appear here.
      </p>

    );
  }

  // Build the full URL.
  const fullUrl = `http://localhost:5000${chartUrl}`;
  // Remove query parameters to accurately determine the file type.
  const urlWithoutQuery = fullUrl.split('?')[0];
  const isHtml = urlWithoutQuery.endsWith('.html');

  return (
    <div ref={resultRef}>
      <h2 className="text-lg font-semibold mb-3">Visualization</h2>

      {isHtml ? (
        <iframe
          src={fullUrl}
          title="Interactive Plot"
          className="w-full h-[400px] border border-gray-700 rounded-lg"
          onError={(e) => {
            e.target.outerHTML = `<p class="text-sm text-red-400 italic">❌ Failed to load interactive plot.</p>`;
          }}
        />
      ) : (
        <img
          src={fullUrl}
          alt="Static Chart"
          className="w-full border border-gray-700 rounded-lg shadow"
          onError={(e) => {
            e.target.onerror = null;
            e.target.src = '';
            e.target.alt = '⚠️ Failed to load image.';
            e.target.className = 'text-sm text-red-400 italic';
          }}
        />
      )}

    </div>
  );
}
