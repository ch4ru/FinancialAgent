import typer
from typing import Optional, List
from phi.assistant import Assistant
from phi.storage.assistant.postgres import PgAssistantStorage
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.pgvector import PgVector2

import os
from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"]= os.getenv("GROQ_API_KEY")
db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db = PgVector2(collection="recipes", db_url=db_url) 
)

knowledge_base.load()
storage = PgAssistantStorage(db_url=db_url, table_name="pdf_assistant")

#table name should be equal to function name below for the assistant
def pdf_assistant(new:bool = False, user : str = "user"):
    run_id: Optional[str] = None,

    if not new:
        existing_run_ids: List[str] = storage.get_run_ids(user)
        if len(existing_run_ids) > 0:
            run_id = existing_run_ids[0]

    assistant = Assistant(
        run_id=run_id,
        storage=storage,
        user_id=user,
        knowledge_base=knowledge_base,

        #show tool calls in the response
        show_tool_calls=True,
        #enable assistant to search the knowledge base
        search_knowledge_base=True,
        #enable it to read chat history
        read_chat_history=True,

    )
    if run_id is None:
        run_id = assistant.run_id
        print(f"New run started with ID: {run_id}")
    else:
        print(f"Continuing run with ID: {run_id}")

    assistant.cli_app(markedown=True)

if __name__ == "__main__":
    typer.run(pdf_assistant)