from langchain_core.prompts import ChatPromptTemplate
from langchain import hub


def Code_Generator_prompt():
    """
    Generates Prompt template from the LangSmith prompt hub
    Returns:
        ChatPromptTemplate -> ChatPromptTemplate instance pulled from LangSmith Hub
    """
    prompt_template = hub.pull("srishti-poem-generator/codeprompt")
    return prompt_template

