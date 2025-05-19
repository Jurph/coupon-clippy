"""Base agent class for the multi-agent system."""
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field
from langchain.agents import AgentExecutor
from langchain.tools import BaseTool
from langchain.schema import AgentAction, AgentFinish

class AgentMessage(BaseModel):
    """Message format for inter-agent communication."""
    sender: str = Field(..., description="Name of the sending agent")
    recipient: str = Field(..., description="Name of the receiving agent")
    content: str = Field(..., description="Message content")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional message metadata")

class BaseAgent:
    """Base class for all agents in the system."""
    
    def __init__(
        self,
        name: str,
        description: str,
        tools: Optional[List[BaseTool]] = None,
        **kwargs: Any
    ):
        """Initialize the base agent.
        
        Args:
            name: Unique identifier for the agent
            description: Description of the agent's capabilities
            tools: List of tools available to the agent
            **kwargs: Additional arguments passed to the agent
        """
        self.name = name
        self.description = description
        self.tools = tools or []
        self.message_queue: List[AgentMessage] = []
        self._setup_agent_executor(**kwargs)
    
    def _setup_agent_executor(self, **kwargs: Any) -> None:
        """Set up the LangChain agent executor."""
        # This will be implemented by specific agent types
        pass
    
    def receive_message(self, message: AgentMessage) -> None:
        """Receive a message from another agent.
        
        Args:
            message: The message to receive
        """
        self.message_queue.append(message)
    
    def send_message(self, recipient: str, content: str, metadata: Optional[Dict[str, Any]] = None) -> AgentMessage:
        """Send a message to another agent.
        
        Args:
            recipient: Name of the receiving agent
            content: Message content
            metadata: Optional metadata to include with the message
            
        Returns:
            The created message
        """
        message = AgentMessage(
            sender=self.name,
            recipient=recipient,
            content=content,
            metadata=metadata or {}
        )
        return message
    
    async def process_messages(self) -> None:
        """Process any pending messages in the queue."""
        while self.message_queue:
            message = self.message_queue.pop(0)
            await self._handle_message(message)
    
    async def _handle_message(self, message: AgentMessage) -> None:
        """Handle a received message.
        
        Args:
            message: The message to handle
        """
        # This will be implemented by specific agent types
        pass
    
    async def execute_task(self, task: str) -> Any:
        """Execute a task using the agent's capabilities.
        
        Args:
            task: Description of the task to execute
            
        Returns:
            The result of the task execution
        """
        # This will be implemented by specific agent types
        pass 