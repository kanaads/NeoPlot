export async function generateVisualization({ language, code, library }) {
  try {
    console.log("🔍 Sending payload:", { language, library });

    const response = await fetch('http://127.0.0.1:5000/api/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ language, code, library }),
    });

    const data = await response.json();
    console.log("📥 Response from server:", data);

    if (!response.ok) {
      throw new Error(data.error || 'An error occurred while generating the visualization.');
    }

    return data;
  } catch (err) {
    console.error("❌ Error from generateVisualization:", err.message);
    throw err;
  }
}
