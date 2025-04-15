# NeoPlot

[GitHub Repository](https://github.com/yourusername/NeoPlot)

NeoPlot is a language-agnostic visualization web application that allows users to generate and view visualizations by executing custom scripts written in Python or R. The backend dynamically executes user-submitted scripts in an isolated environment and returns the resulting visualization, while the frontend (built with React and styled with Tailwind CSS) provides an intuitive interface for code input and persistent visualization history.

## Table of Contents

- [Overview](#overview)
- [Design and Tools Used](#design-and-tools-used)
- [Issues Encountered and Resolutions](#issues-encountered-and-resolutions)
- [Setup and Installation](#setup-and-installation)
  - [Frontend](#frontend)
  - [Backend](#backend)
  - [Docker Deployment](#docker-deployment)
- [Usage](#usage)
- [Screen Recording](#screen-recording)
- [Sample Visualizations](#sample-visualizations)
  - [Python - Static Grouped Bar Chart (Matplotlib)](#1-python---static-grouped-bar-chart-matplotlib)
  - [Python - Interactive 3D Scatter Plot (Plotly)](#2-python---interactive-3d-scatter-plot-plotly)
  - [R - Static Boxplot with Jitter (ggplot2)](#3-r---static-boxplot-with-jitter-ggplot2)
  - [R - Interactive Bubble Chart (Plotly)](#4-r---interactive-bubble-chart-plotly)
- [Future Enhancements](#future-enhancements)
- [License](#license)

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

## Issues Encountered and Resolutions

1. **Module Compatibility:**  
   - *Issue:* Incompatibility between NumPy 2.x and components built with NumPy 1.x (e.g., in Matplotlib).
   - *Resolution:* Pin `numpy` to `<2` in `requirements.txt`.

2. **Werkzeug Import Error:**  
   - *Issue:* Flask expected `url_quote` from Werkzeug, which was removed in newer versions.
   - *Resolution:* Pin Werkzeug to `<2.3` in `requirements.txt`.

3. **Interactive Visualization Preview:**  
   - *Issue:* Loading interactive plots inline via iframes was resource-intensive.
   - *Resolution:* The History page now displays a text label ("Interactive Plot") for such entries. (A future enhancement is to generate a small screenshot thumbnail.)

4. **Network Binding in Docker:**  
   - *Issue:* Flask was binding to `127.0.0.1`, which didn’t allow access through Docker’s port mapping.
   - *Resolution:* Updated the Flask app to run on host `0.0.0.0`.

## Setup and Installation

### Frontend

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/NeoPlot.git
   cd NeoPlot/frontend
