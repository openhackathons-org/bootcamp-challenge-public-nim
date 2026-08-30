# Agentic AI Bootcamp

This bootcamp is a hands-on path from inference to production-style agents. You will call **NVIDIA® NIM™** from local endpoints, expose and consume capabilities with the **Model Context Protocol (MCP)** (including a low-level server implementation), and orchestrate reasoning and tool use with **LangGraph**. You will then use **NeMo Agent Toolkit (NAT)** to connect MCP tools to NIM with **YAML** workflow configuration—plus observability and evaluation—before tying the stack together in a final **Challenge**.

### Prerequisites

Participants are expected to have Python programming knowledge, basic prior knowledge of SQL databases and queries, Natural Language Processing knowledge, and NVIDIA NGC and API keys.

Ensure the following tools are installed on your system:
* [UV Package Manager](https://docs.astral.sh/uv/getting-started/installation/)
* [Python](https://docs.astral.sh/uv/guides/install-python/)
* [Git Version Control](https://github.com/git-guides/install-git)
* [Docker](https://docs.docker.com/engine/install/)
* [VSCode](https://code.visualstudio.com/) or your IDE of choice

### Labs

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

#### Attempt the labs

Open [start_here.ipynb](./tutorial/start_here.ipynb)
