from langchain_ollama import OllamaLLM
from langchain.memory import ConversationSummaryBufferMemory

mistral_llm = OllamaLLM(model="mistral")

memory = ConversationSummaryBufferMemory(llm=mistral_llm, max_token_limit=1000)
