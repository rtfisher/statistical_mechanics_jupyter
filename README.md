README: Running the Statistical Mechanics Jupyter Notebook 

Overview
--------
If you have a Python environment including Jupyter already installed on your computer, you may simply load the notebook directly on your machine. The remainder of this guide will help you run the Statistical Mechanics Jupyter notebook from this repository using a Docker container, without the need to install any additional software. Even if you’ve never used Docker before, these steps will guide you through the process.

Steps to Get Started
--------------------

1. Install Docker
   --------------
   If you don’t have Docker installed on your computer, you can download and install it from the Docker website: https://www.docker.com/products/docker-desktop. Follow the installation instructions for your operating system.

2. Clone the Repository
   --------------------
   First, download (or "clone") the repository to your computer. The command is the same across all operating systems, but on Windows, make sure you're running the command in **Command Prompt** or **PowerShell**. On Linux or OS/X, use the **terminal**.

   - **For OS/X, Linux, and Windows**:
     Type:
     ```
     git clone https://github.com/rtfisher/statistical_mechanics_jupyter.git
     cd statistical_mechanics_jupyter
     ```

3. Build the Docker Image
   ----------------------
   We use a Dockerfile (renamed to `statmech_dockerfile`) to set up the environment for the Jupyter notebook. Again the command is the same across all operating systems.

   - **For OS/X, Linux, and Windows**:
     ```
     docker build -t statistical_mechanics_jupyter -f statmech_dockerfile .
     ```

4. Run the Docker Container
   ------------------------
   To start the Jupyter Notebook server inside a Docker container:

   - **For OS/X and Linux**:
     ```
     docker run -p 8888:8888 -v "$(pwd)":/app statistical_mechanics_jupyter
     ```

   - **For Windows**:
     ```
     docker run -p 8888:8888 -v "%cd%":/app statistical_mechanics_jupyter
     ```

     - `$(pwd)` on OS/X and Linux gets replaced by `%cd%` on Windows.
     - The rest of the command remains the same, ensuring the notebook server inside the container is connected to your computer on port 8888 and the files in this directory are available inside the container.

5. Access the Jupyter Notebook
   ---------------------------
   After running the command, Docker will start the Jupyter Notebook server. You’ll see a message in the terminal (or Command Prompt/PowerShell) like this:

   To access the notebook, open this file in a browser:
       file:///root/.local/share/jupyter/runtime/nbserver-1-open.html
   Or copy and paste one of these URLs:
       http://127.0.0.1:8888/?token=your_token_here

   Important: Use the Token
   ------------------------
   To access the notebook:
   1. **Copy** the URL that looks like `http://127.0.0.1:8888/?token=your_token_here`.
   2. **Paste** it into your web browser’s address bar.
   3. **Press Enter** to open the Jupyter Notebook.

   This URL includes a special token that lets you access the notebook securely.

6. Start Coding!
   -------------
   Once you’re in, you can start working on your Jupyter Notebooks just like normal. All the files in this repository are available in the notebook interface.

Need Help?
----------
If you encounter any issues, make sure Docker is installed correctly and that you followed each step carefully. If the notebook doesn’t open, double-check the terminal (or Command Prompt/PowerShell) for the correct URL and token.

Happy coding!
