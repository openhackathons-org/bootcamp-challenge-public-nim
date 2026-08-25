FROM python:3.13-slim

ARG DEBIAN_FRONTEND=noninteractive
ARG CODE_SERVER_VERSION=4.112.0

ENV VIRTUAL_ENV=/opt/agentic-ai-env \
    PATH="/opt/agentic-ai-env/bin:${PATH}" \
    UV_PROJECT_ENVIRONMENT=/opt/agentic-ai-env \
    UV_LINK_MODE=copy \
    JUPYTER_PLATFORM_DIRS=1 \
    NAT_TELEMETRY_ENABLED=false \
    MCP_PORT=8000 \
    PHOENIX_PORT=6006

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        bash \
        build-essential \
        ca-certificates \
        curl \
        git \
        sqlite3 \
        tini \
    && rm -rf /var/lib/apt/lists/*

RUN python -m venv "${VIRTUAL_ENV}" \
    && pip install --no-cache-dir --upgrade pip uv

WORKDIR /workspace/agentic-ai-bootcamp

COPY pyproject.toml uv.lock ./
RUN uv sync
RUN python -m ipykernel install \
    --sys-prefix \
    --name python3 \
    --display-name "Python 3.13 (agentic-ai-env)"

RUN curl -fsSL https://code-server.dev/install.sh | sh -s -- --version "${CODE_SERVER_VERSION}" \
    && code-server --install-extension ms-python.python --install-extension ms-toolsai.jupyter \
    && code-server --uninstall-extension ms-python.vscode-python-envs

RUN curl -fsSL https://opencode.ai/install | bash

EXPOSE 8888 6006

CMD ["code-server", "/workspace/agentic-ai-bootcamp", "--bind-addr", "0.0.0.0:8888", "--auth", "none"]
