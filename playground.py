from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
import phi
from dotenv import load_dotenv
import phi.api
from phi.model.openai import OpenAIChat
from phi.playground import Playground, serve_playground_app

load_dotenv()

phi.api = os.getenv("phi-52PJxHgb3r3P0lfr6ddxZz1-DTs4QlfOUVLt2parRbc")


webSearchAgent = Agent(
    name= "Web Search Agent",
    role = "A web search agent that can search the web for information and answer questions.",
    model= Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=['search the web for information and always include sources in your answers.'],
    show_tool_calls=True,
    markdown=True,
    
)
financialAgent = Agent(
    name="Financial Agent",
    role="A financial agent that can answer questions about stocks, financial news, and market trends.",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True), 
    ],
    instructions=[
        "Answer questions about stocks, financial news, and market trends.",
        "Use tables to present stock data and financial information."],
    show_tool_calls=True,
    markdown=True,
)

app = Playground(
    agents=[financialAgent, webSearchAgent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)