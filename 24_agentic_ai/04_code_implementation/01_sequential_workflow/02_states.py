# First we need the graph but for graph we need to create the 
# state(a shared memory between every component of graph)

import os 

# 1st way to create a state typed Dict (Most common way to create a state)

from typing import TypedDict

class State(TypedDict):
    topic: str
    summary: str
    score: int

# 2nd way is using pydantic model
# it is good at data validation and type checking at runtime 

from pydantic import BaseModel, field_validator

class StateModel(BaseModel):
    topic: str
    summary: str
    score: int

    @field_validator("score")
    def positive_score(cls, v: int):
        if v < 0:
            raise ValueError(f"Score must be positive!")

# 3rd way is using standard python dataclass but its not that much usefull

from dataclasses import dataclass, field

@dataclass
class State():
    topic: str
    summary: str
    messages: str = field(default_factory=list)

# 4th way of creating state is your base langgraph 

from langgraph.graph import MessagesState

class State(MessagesState):
    topic: str
    summary: str
    score: int 