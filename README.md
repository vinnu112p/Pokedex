
<body>
    <h1>Pokedex</h1>
    <blockquote>
        "Gotta catch 'em all!" - Pokémon
    </blockquote>
<br>
    <h2>Live Link</h2>
    <p>Check out the live version of the Pokedex <a href="https://flask-project-j9yc.onrender.com" target="_blank">here</a>.</p>
<br>
    <h2>Technologies Used</h2>
    <ul>
        <li>Flask</li>
        <li>HTML</li>
        <li>CSS</li>
        <li>JavaScript</li>
        <li>Spline</li>
        <li>PokeAPI</li>
    </ul>
<br>
    <h2>How It Works</h2>
    <p>This Pokedex application allows users to search for Pokémon by name and view their details, including an image, height, weight, abilities, and types. The application fetches data from the PokeAPI and displays it in a user-friendly interface with a 3D animated background.</p>
<br>
    <h3>Features</h3>
    <ul>
        <li>Search for Pokémon by name</li>
        <li>View Pokémon details: image, height, weight, abilities, and types</li>
        <li>Responsive design suitable for mobile devices</li>
        <li>3D animated background using Spline</li>
    </ul>
<br>
    <h2>Installation</h2>
    <p>To run this project locally, follow these steps:</p>
    <ol>
        <li>Clone the repository:<br>
            <pre><code>git clone https://github.com/your-username/pokedex.git<br>cd pokedex</code></pre>
        </li>
        <li>Create a virtual environment:<br>
            <pre><code>python -m venv venv</code></pre>
        </li>
        <li>Activate the virtual environment:<br>
            <ul>
                <li>On Windows:<br>
                    <pre><code>venv\Scripts\activate</code></pre>
                </li>
                <li>On macOS and Linux:<br>
                    <pre><code>source venv/bin/activate</code></pre>
                </li>
            </ul>
        </li>
        <li>Install the dependencies:<br>
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>Run the Flask application:<br>
            <pre><code>python app.py</code></pre>
        </li>
        <li>Open your browser and go to <code>http://127.0.0.1:8000</code> to view the application.</li>
    </ol>
<br>
    <h2>Deployment with Gunicorn</h2>
    <p>To deploy the application using Gunicorn, use the following command:</p>
    <pre><code>gunicorn -w 4 -b 0.0.0.0:8000 app:app</code></pre>
<br>
    <h2>Project Structure</h2>
      <pre><code>Flask_Project/
│
├── static/
│   ├── style.css
│   └── background.jpg (if used)
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
└── README.md</code></pre>
    <h2>Dependencies</h2>
    <ul>
        <li>Flask</li>
        <li>requests</li>
        <li>gunicorn</li>
    </ul>
<br>
    <h2>Contributing</h2>
    <p>Feel free to submit issues or pull requests if you have any suggestions or improvements.</p>
<br>
    <h2>License</h2>
    <p>This project is licensed under the MIT License.</p>
<br>
    <h2>Acknowledgements</h2>
    <ul>
        <li><a href="https://pokeapi.co/" target="_blank">PokeAPI</a> for providing the Pokémon data</li>
        <li><a href="https://spline.design/" target="_blank">Spline</a> for the 3D animated background</li>
    </ul>
</body>
</html>
