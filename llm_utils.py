from langchain_ollama import OllamaLLM

mistral = OllamaLLM(model="mistral")

def generate_subtasks(project_title: str, description: str):
    prompt = f"""
    Break down the project titled '{project_title}' with the description:
    '{description}' into a set of prioritized subtasks.
    Return in a list format with estimated days.
    """
    return mistral.invoke(prompt)
