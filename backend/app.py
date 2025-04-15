import os
import uuid
import subprocess
import json
import logging
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

# Set up logging to show debug messages in the console.
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__, static_folder='results', static_url_path='/results')
CORS(app)
os.makedirs('results', exist_ok=True)

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.get_json()
    language = data.get('language')
    library = data.get('library')
    code = data.get('code')

    if not all([language, library, code]):
        app.logger.error("Missing language, library, or code in the request.")
        return jsonify({'error': 'Missing language, library, or code'}), 400

    uid = str(uuid.uuid4())
    output_dir = os.path.join('results', uid)
    os.makedirs(output_dir, exist_ok=True)

    # Determine output file type and set relative filename.
    is_html = library.lower() == 'plotly'
    filename = 'output.html' if is_html else 'output.png'
    output_filepath = os.path.join(output_dir, filename)
    
    # Determine script extension based on the language.
    # Determine script extension based on the language.
    ext = "py" if language.lower() == "python" else "R"
    script_filename = f'script.{ext}'
    script_path = os.path.join(output_dir, script_filename)

    # Build the dynamic script using relative filename so that files are written in the working directory.
    if language.lower() == 'python':
        # Ensure we are in the current directory within the subprocess.
        script = f"import os\nos.makedirs('.', exist_ok=True)\n{code}\n"
        if library.lower() == 'matplotlib' and 'plt.savefig' not in code:
            script += f"plt.savefig(r'{filename}')\n"
        elif library.lower() == 'plotly' and 'write_html' not in code:
            script += (
                "import plotly.express as px\n"
                "fig = px.bar(x=[1, 2, 3], y=[4, 5, 6])\n"
                "import plotly.io as pio\n"
                f"pio.write_html(fig, file=r'{filename}', auto_open=False)\n"
            )
    elif language.lower() == 'r':
        header = ""
        if library.lower() == 'plotly':
            header += (
                "if (!require('plotly')) install.packages('plotly', repos='http://cran.us.r-project.org')\n"
                "if (!require('htmlwidgets')) install.packages('htmlwidgets', repos='http://cran.us.r-project.org')\n"
                "library(plotly)\n"
                "library(htmlwidgets)\n"
            )
        elif library.lower() == 'ggplot2':
            header += (
                "if (!require('ggplot2')) install.packages('ggplot2', repos='http://cran.us.r-project.org')\n"
                "library(ggplot2)\n"
            )
        script = header + code + "\n"
        if library.lower() == 'ggplot2' and 'ggsave' not in code:
            script += f"ggsave('{filename}')\n"
        elif library.lower() == 'plotly' and 'saveWidget' not in code:
            script += f"htmlwidgets::saveWidget(p, file='{filename}', selfcontained = FALSE)\n"

    with open(script_path, 'w') as f:
        f.write(script)

    app.logger.debug("Script written to %s:", script_path)
    app.logger.debug("\n%s", script)

    # Set the command using just the script filename (not the full path)
    if language.lower() == 'python':
        command = ['python', script_filename]
    else:
        command = ['Rscript', script_filename]

    app.logger.debug("Command to be executed: %s", command)
    app.logger.debug("Working directory for subprocess: %s", output_dir)

    try:
        result = subprocess.run(
            command,
            check=True,
            timeout=30,
            capture_output=True,
            text=True,
            cwd=output_dir  # Execute command inside the output directory.
        )
        app.logger.debug("Subprocess stdout: %s", result.stdout)
        app.logger.debug("Subprocess stderr: %s", result.stderr)
        
        # Check if output file was generated
        if not os.path.exists(os.path.join(output_dir, filename)):
            app.logger.error("Output file not found in %s", output_dir)
            return jsonify({'error': 'Script ran, but no output file was found.'}), 500

        # Save metadata for history
        meta = {
            'filename': filename,
            'url': f'/results/{uid}/{filename}',
            'language': language,
            'library': library,
            'type': 'html' if is_html else 'png'
        }
        meta_path = os.path.join(output_dir, 'meta.json')
        with open(meta_path, 'w') as meta_file:
            json.dump(meta, meta_file)
        app.logger.debug("Metadata saved: %s", meta)

        return jsonify({
            'url': f'/results/{uid}/{filename}',
            'executionOutput': result.stdout or 'Success'
        })

    except subprocess.CalledProcessError as e:
        app.logger.error("Script execution failed: %s", e.stderr or e.stdout)
        return jsonify({'error': e.stderr or e.stdout}), 500
    except subprocess.TimeoutExpired:
        app.logger.error("Script execution timed out.")
        return jsonify({'error': 'Script execution timed out'}), 500


@app.route('/api/history', methods=['GET'])
def get_history():
    history_entries = []
    results_dir = 'results'
    for uid in os.listdir(results_dir):
        dir_path = os.path.join(results_dir, uid)
        if os.path.isdir(dir_path):
            meta_path = os.path.join(dir_path, 'meta.json')
            if os.path.exists(meta_path):
                with open(meta_path, 'r') as f:
                    meta = json.load(f)
                history_entries.append(meta)
    app.logger.debug("Returning history: %s", history_entries)
    return jsonify(history_entries)

@app.route('/results/<uid>/<filename>')
def serve_result(uid, filename):
    return send_from_directory(os.path.join('results', uid), filename)

if __name__ == '__main__':
    # If file watcher is interfering, consider disabling the auto-reloader:
    app.run(debug=True, use_reloader=False)
