export async function fetchVisualizationHistory() {
    try {
      const response = await fetch('http://127.0.0.1:5000/api/history');
      const data = await response.json();
  
      if (!response.ok) {
        throw new Error(data.error || 'Error fetching history.');
      }
  
      return data;
    } catch (err) {
      console.error("❌ fetchVisualizationHistory error:", err.message);
      return [];
    }
  }
  