# NeoPlot

NeoPlot is a language-agnostic visualization web application that allows users to generate and view visualizations by executing custom scripts written in Python or R. The backend dynamically executes the submitted code in an isolated environment and returns the resulting visualization, while the frontend provides an intuitive interface for code input, generation, and persistent history of visualizations.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture & Design](#architecture--design)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
  - [Frontend](#frontend)
  - [Backend](#backend)
  - [Docker Deployment](#docker-deployment)
- [Usage](#usage)
- [Sample Visualizations](#sample-visualizations)
- [Issues and Resolutions](#issues-and-resolutions)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Overview

NeoPlot is designed to simplify the creation and viewing of visualizations. It supports both static and interactive visualizations as well as 3D plots using a mix of libraries such as Matplotlib, Plotly (for Python), and ggplot2, Plotly (for R). The application allows users to select the scripting language (Python or R), input visualization code, and generate charts dynamically, which are then stored in a persistent history.

## Features

- **Language-Agnostic:** Supports both Python and R scripts.
- **Dynamic Code Execution:** The backend safely executes user-submitted scripts in an isolated environment.
- **Visualization Display:** Render static (PNG) and interactive (HTML) visualizations.
- **Persistent History:** Every generated visualization is saved with metadata (including creation timestamp) for later viewing and download.
- **Dockerized Backend:** The backend is containerized using Docker, ensuring a consistent and isolated execution environment.
- **Sample Visualization Demos:** Predefined sample codes for various visualization types (e.g., 3D scatter plots, grouped bar charts, interactive bubble charts, etc.).

## Architecture & Design

NeoPlot’s architecture is split into two main parts:

1. **Frontend:**  
   - Developed with React.
   - Provides a user-friendly interface for language selection, code input (via a code editor), a “Generate” button, and a history page that lists all generated visualizations.
   - Uses components like NavBar, CodeEditor, OutputPanel, and HistoryPage to ensure consistency in UI and UX.

2. **Backend:**  
   - Developed using Flask (Python).
   - Exposes an API endpoint `/api/generate` that accepts POST requests containing the language, library, and code.
   - Dynamically generates a script, executes it (using `subprocess`), and returns a URL pointing to the generated visualization.
   - Maintains a persistent history of visualizations by saving metadata (including creation timestamps) in separate directories.
   - Also supports running R scripts via `Rscript` for generating R-based visualizations.

## Technologies Used

- **Frontend:** React, Tailwind CSS, JavaScript (ES6+)
- **Backend:** Python, Flask, Flask-CORS, subprocess, JSON
- **Visualization Libraries:** 
  - For Python: Matplotlib, Plotly, NumPy, Pandas
  - For R: ggplot2, Plotly, htmlwidgets
- **Containerization:** Docker
- **Other Tools:** Git for version control

## Setup and Installation

### Frontend

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/NeoPlot.git
   cd NeoPlot/frontend
