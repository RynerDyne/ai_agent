import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key =  os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

if len(sys.argv) == 1:
    print("Provide prompt in quotations")
    sys.exit(1)

user_prompt = sys.argv[1]

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists file content in text, limited to 10000 characters (will truncate if necessary), constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to read the contents from.",
            ),
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file in the given path within the working directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file and location of the python file to run",
            ),
        }
    )
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write to a file; if one doesn't exist then the file you write too shall be created, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file location and file you wish to write too."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content you wish to write into the file specified in file_path"
            )
        }
    )
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)])
]

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read the contents of files
- Run python files
- Create and write to files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

model_name = 'gemini-2.0-flash-001'
response = client.models.generate_content(
    model = model_name,
    contents = messages,
    config=types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt,
    ),
)

function_call_part = response.function_calls[0]

if len(sys.argv) == 3 and sys.argv[2] == '--verbose':
                print(f"User prompt: {user_prompt}\nPrompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")

print(f"Calling function: {function_call_part.name}({function_call_part.args})")
