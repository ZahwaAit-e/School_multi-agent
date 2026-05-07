from google.adk.agents.llm_agent import Agent

history_teacher_agent = Agent(
    model='gemini-2.5-flash',
    name='history_teacher_agent',
    description='A helpful assistant for history related queries (events, civilisations, freedom struggle)',

    instruction= """ 
    you are a teacher, 
    Help users with:
    - events, civilisations, freedom struggle
    
    Always respond in a clear format
    
    Answer user questions to the best of your knowledge""",
)
