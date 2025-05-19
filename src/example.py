"""Example usage of the multi-agent system."""
import asyncio
from typing import Any, Dict, List, Optional
from langchain.tools import BaseTool
from langchain_openai import ChatOpenAI

from agents.base import BaseAgent
from agents.project_manager import ProjectManagerAgent
from config.settings import settings

class SimpleTool(BaseTool):
    """A simple example tool."""
    name: str = "simple_tool"
    description: str = "A simple tool that returns its input"
    args_schema: Optional[type] = None
    
    def _run(self, query: str) -> str:
        """Run the tool."""
        return f"Processed: {query}"
    
    async def _arun(self, query: str) -> str:
        """Run the tool asynchronously."""
        return self._run(query)

async def main():
    """Run the example."""
    # Initialize the LLM using settings
    llm = ChatOpenAI(
        api_key=settings.OPENAI_API_KEY,
        model="gpt-3.5-turbo",
        temperature=0
    )
    
    # Create tools
    tools = [SimpleTool()]
    
    # Create the project manager
    project_manager = ProjectManagerAgent(
        tools=tools,
        llm=llm
    )
    
    # Example task
    task = "Find the best deals on frozen vegetables at Giant this week"
    
    # Execute the task
    result = await project_manager.execute_task(task)
    print(f"Task result: {result}")

if __name__ == "__main__":
    asyncio.run(main()) 