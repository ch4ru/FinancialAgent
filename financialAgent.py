from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
# Load environment variables from .env file

## web search agent
webSearchAgent = Agent(
    name= "Web Search Agent",
    role = "A web search agent that can search the web for information and answer questions.",
    model= Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=['search the web for information and always include sources in your answers.'],
    show_tool_calls=True,
    markdown=True,
    
)

## financial agent
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

multi_ai_agent = Agent(
    model = Groq(id="llama-3.1-70b-versatile"),
    name="Multi AI Agent",
    team=[
        webSearchAgent, financialAgent],
    instructions=["Always include sources in your answers.",
                  "Use the web search agent for general information and the financial agent for stock-related queries.",
                  "Use tables to present stock data and financial information."],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("summarize analyst recommendtion and share the latest news for NVDA", stream=True)