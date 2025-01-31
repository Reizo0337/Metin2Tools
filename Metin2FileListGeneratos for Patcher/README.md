<h1>Update Patcher Tool</h1>

This tool allows you to connect to the server and upload updates for the patcher. It automatically generates an MD5 hash for the file and uploads it to the server. Additionally, it features a simple key check for logging purposes, which is currently basic but can be improved for better functionality.

  <h2>Features</h2>
  <ul>
      <li><strong>MD5 Hash Generation</strong>: Automatically generates the MD5 hash of the file to be uploaded.</li>
      <li><strong>File Upload</strong>: Uploads the file to the server once the hash is generated.</li>
      <li><strong>Simple Key Check</strong>: A basic key check for logging and validation, meant for testing purposes.</li>
      <li><strong>Easy UI</strong>: Built using PyQt5 to provide a user-friendly interface for interacting with the tool.</li>
  </ul>

  <h2>Libraries Needed</h2>
  <p>To run this tool, the following Python libraries are required:</p>
  <ul>
      <li><code>PyQt5</code>: Used for easy creation of the user interface.</li>
      <li><code>hashlib</code>: Used for generating the MD5 hash of files.</li>
      <li><code>requests</code>: Used for handling HTTP requests to upload the file.</li>
  </ul>

  <h3>Installation</h3>
  <p>Make sure you have Python 3.x installed. Then, you can install the required libraries by running:</p>
  <pre><code>pip install PyQt5 hashlib requests</code></pre>

  <h2>Usage</h2>
  <ol>
      <li>Launch the tool.</li>
      <li>Select the file you wish to upload.</li>
      <li>The MD5 hash will be generated automatically.</li>
      <li>Upload the file to the server.</li>
      <li>Use the simple key check for logging purposes. (This is a basic implementation, feel free to improve it as needed!)</li>
  </ol>

  <h2>Contributing</h2>
  <p>Feel free to improve or add features to the tool! Pull requests are welcome. Here are some suggestions on areas you could improve:</p>
  <ul>
      <li>Improve the <code>key_check</code> for better logging and validation.</li>
      <li>Enhance the user interface to make it more polished.</li>
      <li>Add error handling for network issues or file upload failures.</li>
  </ul>

  <h2>License</h2>
  <p>This project is open-source. You are free to use, modify, and distribute it as long as you include this README file.</p>
