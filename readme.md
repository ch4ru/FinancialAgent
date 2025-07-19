# AI Financial & Web Search Agent

This project demonstrates a multi-agent system built using `phidata` that combines a financial agent with a web search agent to answer queries related to stock markets, financial news, and general web information. The system leverages Groq's `llama3-groq-70b-8192-tool-use-preview` model for intelligent responses and integrates with `yfinance` and `duckduckgo-search` for data retrieval.

## Features

* **Multi-Agent Architecture:** Combines a specialized Financial Agent and a Web Search Agent.
* **Financial Analysis:** Provides stock prices, analyst recommendations, fundamental data, and company news using `yfinance`.
* **Web Search Capabilities:** Answers general questions and includes sources using `duckduckgo-search`.
* **Structured Output:** Presents stock data and financial information in tables.
* **Playground Interface:** Includes a `phidata` Playground application for interactive testing and demonstration.
* **API Key Management:** Securely loads API keys from a `.env` file.

## Project Structure

* `financialAgent.py`: Defines the `Web Search Agent`, `Financial Agent`, and the `Multi AI Agent` with their respective roles, models, tools, and instructions.
* `playground.py`: Sets up the `phidata` Playground application, integrating the defined agents for a web-based interactive experience.
* `requirements.txt`: Lists all necessary Python dependencies.
* `.env`: Example file for storing API keys.

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

* Python 3.8+
* `pip` (Python package installer)

### 1. Clone the Repository

```bash
git clone <repository_url>
cd <repository_directory>