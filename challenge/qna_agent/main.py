import subprocess
from typing import NotRequired
from langchain.tools import tool
from langchain.agents import create_agent
from langchain.agents.middleware import ModelRequest, ModelResponse, AgentMiddleware, AgentState
from langchain.messages import SystemMessage
from langchain.chat_models import init_chat_model
from typing import Callable
from pathlib import Path
from .skills_ref.utils import list_skills
from .skills_ref.models import SkillProperties

class SkillsState(AgentState):
    """State for the skills middleware."""

    skills_metadata: NotRequired[list[SkillProperties]]
    """List of loaded skill metadata (name, description, path)."""

script_base_path = Path(__file__).parent.resolve() 
chinook_db_path = script_base_path / "notobvious.db"

# Create bash tool for filesystem-based agent
@tool
def bash(command: str) -> str:
    """Execute a bash command and return the output.

    Use this to access skills and resources on the filesystem:
    - Read skill files: cat /path/to/skill/SKILL.md
    - List directories: ls /path/to/dir
    - Execute SQL queries: sqlite3 /path/to/database.db "SELECT ..."
    - Run Python scripts: python script.py

    Args:
        command: The bash command to execute
    """
    if not command.startswith(('ls','cat','sqlite3')):
        return 'only "ls","cat" and "sqlite3" commands are allowed'
    result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
    output = result.stdout
    if result.returncode != 0 and result.stderr:
        output = f"Error (exit {result.returncode}): {result.stderr}\n{output}"
    return output or result.stderr

# Create skill middleware
class SkillMiddleware(AgentMiddleware):
    """Middleware that injects skill descriptions into the system prompt."""

    state_schema = SkillsState

    # Register the bash tool as a class variable
    tools = [bash]

    def __init__(self,skills_dir):
        self.skills_dir = skills_dir

    def before_agent(self, state:SkillsState, runtime):
        skills = list_skills(self.skills_dir)
        return SkillsState(skills_metadata=skills)

    def wrap_model_call(
        self,
        request: ModelRequest,
        handler: Callable[[ModelRequest], ModelResponse],
    ) -> ModelResponse:
        """Sync: Inject skill descriptions into system prompt."""

        skills = request.state.get("skills_metadata", [])
        skills_list = []
        for skill in skills:
            skills_list.append(
                f"- **{self.skills_dir / skill.name}**: {skill.description}"
            )
        self.skills_prompt = "\n".join(skills_list)

        # Build the skills addendum
        skills_addendum = (
            f"\n\n## Available Skills\n\n{self.skills_prompt}\n\n"
            "Use the bash tool to read skill instructions, e.g., "
            "`bash('cat /path/to/skill/SKILL.md')`. "
            "You can also use the bash tool to execute SQL queries with sqlite3. e.g., "
            "`bash('sqlite3 database.db \"SELECT ...\"')`."
            "Do not run sqlite3 before reading SKILL.md"
        )

        # Append to system message content blocks
        new_content = list(request.system_message.content_blocks) + [
            {"type": "text", "text": skills_addendum}
        ]
        new_system_message = SystemMessage(content=new_content)
        modified_request = request.override(system_message=new_system_message)
        response = handler(modified_request)
        return response

def create_sql_agent(skills_dir,inf_url,nvidia_api_key,debug=False):
    model_id = "nvidia/nemotron-3-nano-30b-a3b"
    nvidia_model = init_chat_model(model=model_id,base_url=inf_url,api_key=nvidia_api_key,model_provider="nvidia")
    # Create the agent with skill support
    agent = create_agent(
        nvidia_model,
        system_prompt=(
            f"""
            Follow these steps to answer the question from the user.
            1) Generate the SQL query based on the schema
            2) Retrieve data from {chinook_db_path} using the SQL query generated in 1).
            """
        ),
        middleware=[SkillMiddleware(skills_dir)],
        debug=debug
    )
    return agent
