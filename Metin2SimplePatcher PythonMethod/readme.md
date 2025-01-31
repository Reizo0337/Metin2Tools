<h1>Sapphire2 Game Launcher</h1>

<h2>Description</h2>
<p>This is a custom game launcher for a private Metin2 server. The launcher checks for updates, downloads necessary files, and launches the game.</p>

<h2>Features</h2>
<ul>
    <li>Custom UI with a background image.</li>
    <li>Automatic game updates.</li>
    <li>Frameless window with draggable functionality.</li>
    <li>Launches the game after updating.</li>
</ul>

<h2>Installation</h2>
<p>To run this launcher, you need to install the required dependencies.</p>

<h3>Requirements</h3>
<ul>
    <li>Python 3.x</li>
    <li>PyQt5</li>
</ul>

<h3>Install Dependencies</h3>
<pre><code>pip install PyQt5</code></pre>

<h2>How It Works</h2>
<h3>1. Checking for Updates</h3>
<p>The launcher fetches a file list from the server and compares the hash of local files. If a file is missing or outdated, it downloads the new version.</p>

<h3>2. Downloading Files</h3>
<p>The launcher downloads necessary files and places them in the correct directories.</p>

<h3>3. Launching the Game</h3>
<p>Once all updates are complete, the launcher allows the user to start the game by running the <code>Metin2Release.exe</code> file.</p>

<h2>Configuration</h2>
<ul>
    <li><strong>SERVER_URL</strong>: The base URL where the patcher files are hosted.</li>
    <li><strong>CLIENT_FOLDER</strong>: The directory where game files are stored.</li>
    <li><strong>GAME_EXECUTABLE</strong>: The executable file used to launch the game.</li>
</ul>

<h2>File Structure</h2>
<pre><code>.
??? launcher.py  # Main script
??? img/
?   ??? patcher_bg.png  # Background image
?   ??? close.png  # Close button icon
?   ??? play_btn.png  # Play button icon
??? patcher_test/  # Testing directory for updates
</code></pre>

<h2>Running the Launcher</h2>
<p>To start the launcher, run the following command:</p>
<pre><code>python launcher.py</code></pre>

<h2>Notes</h2>
<ul>
    <li>The launcher is designed for Windows.</li>
    <li>If packaged with PyInstaller, ensure all necessary files are included.</li>
</ul>

<h2>License</h2>
<p>This project is for educational purposes, is not made for LAST CUSTOMERS USING.</p>
