# Agentic AI Bootcamp

This bootcamp is a hands-on path from inference to production-style agents. You will call **NVIDIA® NIM™** from local endpoints, expose and consume capabilities with the **Model Context Protocol (MCP)** (including a low-level server implementation), and orchestrate reasoning and tool use with **LangGraph**. You will then use **NeMo Agent Toolkit (NAT)** to connect MCP tools to NIM with **YAML** workflow configuration—plus observability and evaluation—before tying the stack together in a final **Challenge**.

## DGX / DGXC Deployment

### Tested environment

We tested and ran all labs on a DGX machine equipped with an A100 and H100 GPUs (80GB).

### Prerequisites

Participants are expected to have Python programming knowledge, basic prior knowledge of SQL databases and queries, Natural Language Processing knowledge, and NVIDIA NGC and API keys.

Ensure the following tools are installed on your system:
* [UV Package Manager](https://docs.astral.sh/uv/getting-started/installation/)
* [Python](https://docs.astral.sh/uv/guides/install-python/)
* [Git Version Control](https://github.com/git-guides/install-git)
* [Docker](https://docs.docker.com/engine/install/)

#### Setup environment variables

```bash
VSCODE_PORT=<dynamic_allocation> # Port to access VSCode (entry point to IDE)
PHOENIX_PORT=<dynamic_allocation> # Port to access phoenix server (used in lab 6)
MCP_PORT=<dynamic_allocation> # Port to access HTTP based MCP Server (used in labs 3,4,6 and challenge)
NIM_PORT=<dynamic_allocation> # Port to access NIM server (used in labs 2,5,6 and challenge)
INF_URL="http://${HOSTNAME}:${NIM_PORT}/v1" # NIM server URL (used in labs 2,5,6 and challenge)
```

#### Clone the git repository

```bash
https://github.com/openhackathons-org/agentic-ai-bootcamp
cd agentic-ai-bootcamp
```

#### Install project dependencies 

```bash
uv sync
```

#### Install OpenCode (Coding harness)

```bash
curl -fsSL https://opencode.ai/install | bash
```

#### 4. Installing VSCode Server (IDE)

```bash
curl -fsSL https://code-server.dev/install.sh | sh

# Install Python Extensions
code-server --install-extension ms-python.python --install-extension ms-toolsai.jupyter
code-server --bind-addr 0.0.0.0:$VSCODE_PORT --auth none <path to agentic ai bootcamp>
```

#### 5. Opening the labs

With **code-server** running, open **http://$HOSTNAME:$VSCODE_PORT**. In the workspace, open the **tutorial** directory and start from **start_here.ipynb**.

When you are finished with the labs close your shell or pressing **Ctrl+D** in the terminal. Congratulations, you've successfully built and deployed an Agentic AI Bootcamp!
