# Agentic AI Bootcamp

This bootcamp is a hands-on path from inference to production-style agents. You will call **NVIDIA® NIM™** from cloud and local endpoints, expose and consume capabilities with the **Model Context Protocol (MCP)** (including a low-level server implementation), and orchestrate reasoning and tool use with **LangGraph**. You will then use **NeMo Agent Toolkit (NAT)** to connect MCP tools to NIM with **YAML** workflow configuration—plus observability and evaluation—before tying the stack together in a final **Challenge**.

## Deploying the Labs

Two deployment options are supported:

- **DGX / DGXC clusters** — install dependencies directly on the host and run `phoenix` and `code-server` from your shell.
- **Local with Docker Compose** — build a self-contained image that bundles Python, the lab requirements, and `code-server`, and mount the repo as a workspace.

Pick whichever matches your environment and skip the other section.

## DGX / DGXC Deployment

### Tested environment

We tested and ran all labs on a DGX machine equipped with an A100 and H100 GPUs (80GB).

### Prerequisites

Participants are expected to have Python programming knowledge, basic prior knowledge of SQL databases and queries, Natural Language Processing knowledge, and NVIDIA NGC and API keys.

Ensure the following tools are installed on your system:
* [UV Package Manager](https://docs.astral.sh/uv/getting-started/installation/)
* [Python](https://docs.astral.sh/uv/guides/install-python/)
* [Git Version Control](https://github.com/git-guides/install-git)

For local run setups, ensure that port `8000` (used by local NIM and other local HTTP services in the labs) and port `6006` (used by Phoenix) are available before starting the notebooks.

#### 1. Setting up a Virtual Environment

First, clone this repository and navigate to the project directory:
```bash
https://github.com/openhackathons-org/agentic-ai-bootcamp
cd agentic-ai-bootcamp
```

Create and activate a new virtual environment using **Python 3.13 or newer**:

```bash
# Create virtual environment
python -m venv agentic-ai-env

# Activate virtual environment for Linux / macOS
source agentic-ai-env/bin/activate

# Activate virtual environment for Windows
# Command Prompt (cmd)
agentic-ai-env\Scripts\activate.bat

#PowerShell
.\agentic-ai-env\Scripts\Activate.ps1
```

#### 2. Installing Required Packages

With the virtual environment activated, install the required packages:
```bash
# Install requirements
uv pip install -r requirements.txt
```

#### 3. Run Phoenix UI Server

[Arize Phoenix](https://arize.com/docs/phoenix) is an open-source observability UI used in some labs to collect and inspect traces (for example, from LLM and agent runs). Start it in a **separate terminal** while your virtual environment is activated, and leave that terminal running while you work through the notebooks.

```bash
# Launch the Phoenix web UI and trace collector (default UI port is 6006)
phoenix serve
```

Example startup output (versions and paths may differ on your machine):

```
✅ Migrations completed in 0.613 seconds.
INFO:     Started server process [23099]
INFO:     Waiting for application startup.


██████╗ ██╗  ██╗ ██████╗ ███████╗███╗   ██╗██╗██╗  ██╗
██╔══██╗██║  ██║██╔═══██╗██╔════╝████╗  ██║██║╚██╗██╔╝
██████╔╝███████║██║   ██║█████╗  ██╔██╗ ██║██║ ╚███╔╝
██╔═══╝ ██╔══██║██║   ██║██╔══╝  ██║╚██╗██║██║ ██╔██╗
██║     ██║  ██║╚██████╔╝███████╗██║ ╚████║██║██╔╝ ██╗
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝ v14.5.0

|  ⭐️⭐️⭐️ Support Open Source ⭐️⭐️⭐️
|  ⭐️⭐️⭐️ Star on GitHub! ⭐️⭐️⭐️
|  https://github.com/Arize-ai/phoenix
|
|  🌎 Join our Community 🌎
|  https://join.slack.com/t/arize-ai/shared_invite/zt-3r07iavnk-ammtATWSlF0pSrd1DsMW7g
|
|  📚 Documentation 📚
|  https://arize.com/docs/phoenix
|
|  🚀 Phoenix Server 🚀
|  Phoenix UI: http://localhost:6006
|
|  Authentication: False
|  Log traces:
|    - gRPC: http://localhost:4317
|    - HTTP: http://localhost:6006/v1/traces
|  Storage: sqlite:////Users/krkalyan/.phoenix/phoenix.db
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:6006 (Press CTRL+C to quit)
```

From this output, the useful bits are:

- **Phoenix UI** — open **http://localhost:6006** in a browser to explore traces and experiments.
- **Storage** — Phoenix uses a local SQLite database under your home directory (the exact path is printed in the log).
- **Stopping the server** — press **Ctrl+C** in the terminal where `phoenix serve` is running when you no longer need the UI.

#### 4. Installing VS Code Server (code-server)

```bash
curl -fsSL https://code-server.dev/install.sh | sh

# Install Python Extensions
code-server --install-extension ms-python.python --install-extension ms-toolsai.jupyter
code-server --auth none --port 8888
```

After running the command, you should see output similar to:

```
[2026-04-15T08:04:15.280Z] info  Wrote default config file to /Users/krkalyan/.config/code-server/config.yaml
[2026-04-15T08:04:15.461Z] info  code-server 4.112.0 d7599ae360900ad55b503e3c840b417a1eae4798
[2026-04-15T08:04:15.462Z] info  Using user-data-dir /Users/root/.local/share/code-server
[2026-04-15T08:04:15.468Z] info  Using config file /Users/root/.config/code-server/config.yaml
[2026-04-15T08:04:15.468Z] info  HTTP server listening on http://127.0.0.1:8888/
[2026-04-15T08:07:10.214Z] info    - Authentication is disabled
[2026-04-15T08:04:15.468Z] info    - Not serving HTTPS
```

#### 5. Opening the labs

With **code-server** running, open **http://localhost:8888** in your browser (or use the URL printed in the terminal if it differs). In the workspace, open the **tutorial** directory and start from **start_here.ipynb**.

When you are finished with the labs close your shell or pressing **Ctrl+D** in the terminal. Congratulations, you've successfully built and deployed an Agentic AI Bootcamp!

### Troubleshooting

If you encounter any issues:

1. **Virtual Environment Issues**
   - Make sure you're in the correct directory when creating the virtual environment
   - Verify that the virtual environment is activated (you should see `(agentic-ai-env)` in your terminal prompt)

2. **Package Installation Issues**
   - Try updating pip before installing requirements: `pip install --upgrade pip`
   - If a package fails to install, try installing it separately

3. **GPU Access Issues**
   - Ensure NVIDIA drivers are properly installed
   - Check if CUDA toolkit is installed and matches your PyTorch version
   - Run `nvidia-smi` in terminal to verify GPU is recognized

4. **VSCode Access Issues**
   - Make sure port 8888 is not being used by another application
   - If accessing from another machine, ensure firewall settings allow the connection
   - Try a different port if 8888 is unavailable

For additional help, please open an issue in the GitHub repository.

## Local Deployment with Docker Compose

This option packages the entire environment — Python 3.13, the lab requirements, and `code-server` with the Python and Jupyter extensions — into a single container. It is the fastest way to run the bootcamp on a laptop or workstation without touching the host's Python installation.

### Prerequisites

- [Docker Engine](https://docs.docker.com/engine/install/) **24+** with the [Compose plugin](https://docs.docker.com/compose/install/) (`docker compose version` should succeed)
- Ports `8888` (code-server) and `6006` (Phoenix) free on the host
- Roughly **6 GB** of free disk space for the image

A GPU is **not** required for the local container; the labs reach NIM endpoints over the network. If you do have an NVIDIA GPU and want to use it, install the [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) and add a `deploy.resources.reservations.devices` block to `docker-compose.yml`.

### 1. Clone the repository

```bash
git clone https://github.com/openhackathons-org/agentic-ai-bootcamp
cd agentic-ai-bootcamp
```

### 2. Build and start the container

From the repo root, build the image and start the service in the background:

```bash
docker compose up --build -d
```

The first build takes a few minutes while `requirements.txt` is installed and `code-server` is downloaded. Subsequent starts reuse the cached image and come up in seconds.

The compose file mounts the repo at `/workspace/agentic-ai-bootcamp` and `settings.json` at `/workspace/agentic-ai-bootcamp/.vscode/settings.json`, so any edits you make on the host are visible inside the container immediately — no rebuild required.

### 3. Open the labs

Open **http://localhost:8888** in your browser. code-server will load the `agentic-ai-bootcamp` workspace; navigate to the `tutorial` directory and start from `start_here.ipynb`.

### 4. Run Phoenix UI Server

Phoenix is installed inside the container. Follow the instructions in [lab 5](./tutorial/jupyter_notebook/05_nemo_agent_toolkit.ipynb) to launch the Phoenix server.

The UI is published on the host at **http://localhost:6006** via the port mapping in `docker-compose.yml`.

### 5. Stopping and cleaning up

```bash
# Stop the container but keep the image
docker compose down

# Stop and remove the built image
docker compose down --rmi local
```

### Troubleshooting

1. **Port already in use** — another process is bound to `8888` or `6006`. Either free the port or remap it in `docker-compose.yml` (e.g. `"9000:8888"`).
2. **Permission denied on bind mount** — on Linux, the container writes as `root` by default; files it creates may be owned by `root` on the host. Run `sudo chown -R $USER:$USER .` after stopping the container if needed.
3. **Image rebuild after editing `requirements.txt`** — bind mounts only cover the repo; package changes require `docker compose up --build` to reinstall inside the image.
4. **Code-server unreachable from another machine** — `docker-compose.yml` binds to all interfaces inside the container, but Docker only publishes to `localhost` by default. Change the port mapping to `"0.0.0.0:8888:8888"` or use SSH port forwarding.

