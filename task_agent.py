import os
from dotenv import load_dotenv
import cohere
load_dotenv()

cohereAi = cohere.Client(os.getenv("COHERE_API_KEY"))
def read_task(fileName):
    with open(fileName, 'r') as file:
        return file.read()

def summarize_task(task):
    prompt= f"""
You are a smart task planning agent. Your job is to summarize the task provided to you.
Give task in 3 priority levels: High, Medium, Low.
Here is the task description:
{task}
Return response in this format:
High Priority : 
    -task 1
    -task 2
Medium Priority :
    -task 1
    -task 2
Low Priority : 
    -task 1
    -task 2
Make sure to provide a clear and concise summary of the task, breaking it down into actionable items 
"""

    response = cohereAi.chat(
        model="command-r",
       message=prompt
    )
    return response.text

if __name__ == "__main__":
    task_text = read_task("task.txt")
    summary = summarize_task(task_text)
    print("Task Summary:")
    print(summary)