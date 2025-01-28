# from model import create_chat_groq
# import prompt
# def generate_Code(topic):
#     """
#     Funtion to generate code

#     Args:
#        Topic (str) - topic of the poem
    
#     Returns:
#         response.content (str)
#     """
#     prompt_template = prompt.Code_generator_prompt()
#     llm = create_chat_groq()

#     chain = prompt_template |  llm
#     response = chain.invoke({
#         "topic" : topic
#     })
#     # response = llm.invoke()
#     return response.content

def generate_code(topic):
    """
    Function to generate a code snippet for a given topic.
    
    Args:
        topic (str): The topic for which to generate code.
    
    Returns:
        str: A generated code snippet.
    """
    
    # Example responses for a few topics, you can extend this or replace with actual code generation logic
    code_snippets = {
        "python function": """
def greet(name):
    return f"Hello, {name}!"
        """,
        "web scraper": """
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.prettify()
        """,
        "basic HTML page": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Page</title>
</head>
<body>
    <h1>Welcome to my website!</h1>
    <p>This is a basic HTML page.</p>
</body>
</html>
        """,
        "simple JavaScript function": """
function add(a, b) {
    return a + b;
}
        """
    }
    
    # If topic matches a predefined snippet, return it
    if topic.lower() in code_snippets:
        return code_snippets[topic.lower()]
    
    # If no match, generate a dynamic placeholder code snippet
    return f"// Code snippet for '{topic}' not found. Here's a placeholder for '{topic}':\n" + generate_placeholder_code(topic)

def generate_placeholder_code(topic):
    """
    Generate a placeholder code snippet tailored to the topic.
    
    Args:
        topic (str): The topic for which to generate placeholder code.
    
    Returns:
        str: A placeholder code snippet based on the topic.
    """
    # Create a simple placeholder code that outputs the topic in a print/log statement
    return f"""
// Placeholder code for topic: {topic}
function placeholder() {{
    console.log("This is placeholder code for '{topic}'.");
}}
    """
