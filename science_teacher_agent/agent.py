from google.adk.agents.llm_agent import Agent

science_teacher_agent = Agent(
    model='gemini-2.5-flash',
    name='science_teacher_agent',
    description='A helpful assistant for science related queries (physics, chemistry, biology) ',
    instruction= """ Help users with:
    - physics, chemistry, biology
    
    Always respond in a clear format
    
    Answer user questions to the best of your knowledge""",
)
