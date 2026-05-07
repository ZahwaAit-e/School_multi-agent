from google.adk.agents.llm_agent import Agent

english_teacher_agent = Agent(
    model='gemini-2.5-flash',
    name='english_teacher_agent',
    description='A helpful assistant for english related queries (grammar, essay, literatture)',
    instruction= """ 
    you are a teacher, 
    
    Help users with:
    - grammar, essay, literatture
    
    Always respond in a clear format"""

)

    
