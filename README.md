# NeoPlot

[GitHub Repository](https://github.com/yourusername/NeoPlot)

NeoPlot is a language-agnostic visualization web application that allows users to generate and view visualizations by executing custom scripts written in Python or R. The backend dynamically executes user-submitted scripts in an isolated environment and returns the resulting visualization, while the frontend (built with React and styled with Tailwind CSS) provides an intuitive interface for code input and persistent visualization history.

## Overview

NeoPlot simplifies the process of creating and viewing visualizations by:
- **Supporting multiple languages:** Users can write scripts in Python or R.
- **Dynamic code execution:** The backend executes code on the fly and returns visualizations.
- **Persistent storage:** Every visualization is saved along with metadata for later review.
- **Isolated execution environment:** The backend is containerized using Docker for consistent and secure operation.
- **Variety of visualization types:** Both static (e.g., PNG) and interactive (e.g., HTML) visualizations are supported.

## Design and Tools Used

**Frontend:**
- **Framework:** React
- **Styling:** Tailwind CSS
- **Components:** NavBar, CodeEditor, OutputPanel, HistoryPage
- **Functionality:**  
  - Dropdown for language selection
  - Code input area with sample code
  - "Generate" button that sends code to the backend
  - History page showing generated visualizations with previews and metadata

**Backend:**
- **Framework:** Flask with Flask-CORS
- **Dynamic Execution:** Uses `subprocess` to run Python or R scripts based on user input.
- **File Storage:** Visualizations and metadata are saved in a `results` folder.
- **APIs:**  
  - `/api/generate` to execute code
  - `/api/history` to retrieve visualization history
  - `/results/<uid>/<filename>` to serve generated visualizations, with options to view or force download
- **Containerization:** Deployed in Docker to provide an isolated environment.

**Visualization Libraries:**
- **Python:** Matplotlib, Plotly, NumPy, Pandas
- **R:** ggplot2, Plotly, htmlwidgets

## Issues Encountered and Their Resolutions

### 1. Module Compatibility Issue
- **Context:** While integrating Matplotlib in the Python backend, runtime errors occurred due to incompatibility between NumPy 2.x and components built with NumPy 1.x.
- **Solution:** The `requirements.txt` was updated to pin `numpy` to a version below 2 (e.g., `numpy<2`), ensuring compatibility with Matplotlib.
- **Outcome:** This adjustment allowed the Matplotlib-based visualizations to execute smoothly, with the system reliably generating static plots.

### 2. Werkzeug Import Error
- **Context:** An import error was encountered because Flask expected the `url_quote` function from Werkzeug, which was removed in newer versions.
- **Solution:** The `requirements.txt` was revised to pin Werkzeug to a version earlier than 2.3 (`Werkzeug<2.3`), aligning the dependency with Flask's requirements.
- **Outcome:** The Flask backend now runs without errors, ensuring uninterrupted service and improved stability.

### 3. Interactive Visualization Preview Performance
- **Context:** Rendering interactive visualizations inline using iframes on the History page was resource-intensive and degraded the performance.
- **Solution:** The History page was updated to display a simple text label ("Interactive Plot") for interactive visualizations instead of embedding the full iframe. (Plans for future enhancement include generating a thumbnail preview.)
- **Outcome:** This change significantly improved page performance while still informing users that an interactive visualization is available.

### 4. Docker Network Binding
- **Context:** The Flask backend was initially set to bind to `127.0.0.1`, which prevented proper access through Docker’s port mapping.
- **Solution:** The Flask server configuration was updated to bind to `0.0.0.0`, allowing it to listen on all network interfaces.
- **Outcome:** With this update, the Dockerized backend is now accessible via the host (e.g., at `http://localhost:5000`), resolving all connectivity issues.


## Future Enhancements

- **Enhanced Security:**  
  Explore more granular sandboxing for code execution and implement additional resource limiting to further secure the production environment.

- **Automated Thumbnail Generation:**  
  Integrate an automated process (using tools like Puppeteer or wkhtmltoimage) to generate thumbnail previews for interactive visualizations, improving the History page performance and user experience.

- **Expanded Visualization Support:**  
  Incorporate support for additional visualization libraries and types, broadening NeoPlot’s capabilities for diverse data analysis and presentation.
