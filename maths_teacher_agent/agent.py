from google.adk.agents.llm_agent import Agent

maths_teacher_agent = Agent(
    model='gemini-2.5-flash',
    name='maths_teacher_agent',
    description='A helpful assistant for maths related queries (algebra, geometry, calculus)',
    instruction= """ you are a teacher, 
    Help users with:
    - algebra, geometry, calculus
    
    Always respond in a clear format
    
    Answer user questions to the best of your knowledge""",
    
)
