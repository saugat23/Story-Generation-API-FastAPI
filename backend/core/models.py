from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class StoryOptionLLM(BaseModel):
    text:str = Field(description="the text of option shown to the user")
    nextNode: Dict[str, Any] = Field(description="the next node content and its options")

class StoryNodeLLM(BaseModel):
    content: str = Field(description="the main content of the story node")
    isEnding: bool = Field(description="check if this node is the ending node")
    isWinningEnding: bool = Field(description="check if this node is the winning ending node")
    options: Optional[List[StoryOptionLLM]] = Field(default=None, description="the options for this node")

class StoryLLMResponse(BaseModel):
    title: str = Field(description="The title of the story")
    rootNode: StoryOptionLLM = Field(description="the root node of the story")