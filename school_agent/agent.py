from google.adk.agents.llm_agent import Agent

from english_teacher_agent.agent import english_teacher_agent
from history_teacher_agent.agent import history_teacher_agent
from maths_teacher_agent.agent import maths_teacher_agent
from science_teacher_agent.agent import science_teacher_agent

# THIS IS THE MAGIC WORD: root_agent
root_agent = Agent(
    model="gemini-2.5-flash",
    name="school_agent",
    description="main router agent that sends tasks to sub-agents",
    instruction="""
Act as a school coordinator.

Help users with:
- if user asks about english related queries (grammar, essay, literatture) -> use english_teacher_agent
- if user asks about maths related queries (algebra, geometry, calculus) -> use maths_teacher_agent
- if user asks about science related queries (physics, chemistry, biology) -> use science_teacher_agent
- if user asks about history related queries (events, civilisations, freedom struggle) -> use history_teacher_agent

If unsure, respond directly.
""", 
    sub_agents=[english_teacher_agent, history_teacher_agent, maths_teacher_agent, science_teacher_agent]
)