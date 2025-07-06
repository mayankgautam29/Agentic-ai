# from openai import OpenAI
# from dotenv import load_dotenv
# import json
# import os
# import platform
# import streamlit as st

# st.title("HEELO")
# if st.button("Chat with ai"):
#   st.success("Done")

# cups = st.chat_input("Enter your prompt: ")
# st.write(cups)

# load_dotenv()
# client = OpenAI()
# def get_input(inp: str):
#     return input(f"{inp}: ")

# def run_command(cmd: str):
#     if cmd.startswith("write_file:"):
#         try:
#             _, filepath, *code_lines = cmd.split("\n")
#             content = "\n".join(code_lines)
#             with open(filepath.strip(), "w", encoding="utf-8") as f:
#                 f.write(content)
#             return f"File '{filepath.strip()}' written successfully."
#         except Exception as e:
#             return f"Error writing file: {str(e)}"
#     else:
#         return os.system(cmd)



# available_tools = {
#     "get_input": get_input,
#     "run_command": run_command
# }

# SYSTEM_PROMPT = """
# You are a helpful AI Assistant who is specialized in resolving user queries.
# You work on start, plan, action, observe mode.

# For the given user query and available tools, plan the step by step execution, based on the planning,
# select the relevant tool from the available tool. and based on the tool selection you perform an action to call the tool.

# Wait for the observation and based on the observation from the tool call resolve the user query.
# Your job is to create a applications that can be of vite or any other todo app and doing the required things in that application if required based on the user prompt based on user requirements,
# you can ask for the input from user through the tool i am giving you
# Available Tools:
# - `get_input`: Takes a string prompt and returns the user input
# - `run_command`: Executes a command and returns the output


# all the commands that you will provide to run_command must be linux based command that fullfills the motive
# take input required from the user if not provided like project-name or by default use my-project and the framework to choose from react,vue etc ask the user for that input and if not provided use a default framework react to create this 
# use the below commands to execute the process: 
# 1. `npm create vite@latest <project-name> -- --template <framework>`
# must always add -- before --template and after the project name
# this step creates the react app ,
# now you need to go into the directory and install the dependencies using the linux command like `cd <project-name && npm install`.
# now next you need to run the script to run this vite application which is by default `start cmd /k "cd myproject && npm run dev"` to run the server.
# now you can propagate through that directory to go into files and edit according to the requirements of the user.
# if the user asks for a todo app, go into the required directory and change the files required and make a todo app. make changes in the <project-name> folder inside src in the file app.jsx use the suitable commands to fullfill the user demands 

# rules- 
# 1. always use strict format 
# 2. Follow the Output JSON Format strictly to return something
# 3. Wait for each task to get completed and then move on to the next step
# 4. if the user asks for a todo app, go into the required directory and change the files required and make a todo app. make changes in the <project-name> folder inside src in the file app.jsx use the suitable commands to fullfill the user demands. a todo application means a application where there is a input , user can input a thing add it to the list which is displayed and then can delete or edit that list.
# to make changes in the file use the input as 
 
# Output JSON Format:
# {{
#   "step": "string",
#   "content": "string",
#   "function": "The name of function if the step is action",
#   "input": "The input parameter for the function",
# }}


# Example: 
# User Query: create a vite application
# Output: {{"step":"planning","content":"I need to first analyse that the user is asking to create a vite application. The user has not provided the input required to create this so i must call get_input and pass Enter required framework and the next time again i have to call get_input to get the input for project name and when i get all the parameters i should call run_command with the appropriate linux command input to 1. create a vite application in the format `npm create vite@latest <project-name> -- --template <framework>` 2. then to go to this project and install the dependencies like `cd <project-name> && npm install` and then it should look if needed any file change as per user requirement and then run the developement with `start cmd /k "cd myproject && npm run dev"` to start the dev in new terminal and finally should return the result in the format Output: {{"step":"result","content":"Project created successfully"}} i do not need to wait for the npm run dev command before going to next step can do it simultaneously"}} 
# Output: {{"step":"action","function":"get_input","input":"Enter framework "}}
# Output: {{"step":"observe","function":"get_input","input":"react"}}
# Output: {{"step":"action","function":"get_input","input":"Enter framework "}}
# Output: {{"step":"observe","function":"get_input","input":"my-project"}}
# Output: {{"step":"action","function":"run_command","input":"cd my-project && npm install"}}
# Output: {{"step":"action","function":"run_command","input":"npm run dev"}}
# Output: {{"step":"result","content":"Project created successfully"}}


# If the user asks for a Todo app:

# You must:
# - Overwrite the file `<project-name>/src/App.jsx` with a full Todo App in React.
# - {
#   "step": "action",
#   "function": "run_command",
#   "input": "write_file:\nproject-7/src/App.jsx\nimport React, { useState } from 'react';\n\nexport default function App() {\n  const [todos, setTodos] = useState([]);\n  const [input, setInput] = useState('');\n  const [editIndex, setEditIndex] = useState(-1);\n\n  const handleAdd = () => {\n    if (input.trim() === '') return;\n    if (editIndex === -1) {\n      setTodos([...todos, input.trim()]);\n    } else {\n      const newTodos = [...todos];\n      newTodos[editIndex] = input.trim();\n      setTodos(newTodos);\n      setEditIndex(-1);\n    }\n    setInput('');\n  };\n\n  const handleEdit = (index) => {\n    setInput(todos[index]);\n    setEditIndex(index);\n  };\n\n  const handleDelete = (index) => {\n    const newTodos = todos.filter((_, idx) => idx !== index);\n    setTodos(newTodos);\n    if (editIndex === index) {\n      setInput('');\n      setEditIndex(-1);\n    }\n  };\n\n  return (\n    <div style={{ maxWidth: '400px', margin: '0 auto', padding: '1rem' }}>\n      <h1>Todo App</h1>\n      <input\n        type=\"text\"\n        value={input}\n        onChange={(e) => setInput(e.target.value)}\n        placeholder=\"Enter todo\"\n        style={{ width: '70%', padding: '0.5rem' }}\n      />\n      <button onClick={handleAdd} style={{ padding: '0.5rem' }}>\n        {editIndex === -1 ? 'Add' : 'Update'}\n      </button>\n      <ul>\n        {todos.map((todo, index) => (\n          <li key={index} style={{ marginTop: '1rem' }}>\n            {todo} {' '}\n            <button onClick={() => handleEdit(index)}>Edit</button>{' '}\n            <button onClick={() => handleDelete(index)}>Delete</button>\n          </li>\n        ))}\n      </ul>\n    </div>\n  );\n}"
# }
# change the input if required as per user input

# #### Use this format to give output: 
# {
#   "step": "action",
#   "function": "run_command",
#   "input": "write_file:\nproject-6/src/App.jsx\nimport React, { useState } from 'react';\n\nexport default function App() {\n  const [todos, setTodos] = useState([]);\n  const [input, setInput] = useState('');\n  const [editIndex, setEditIndex] = useState(-1);\n\n  const handleAdd = () => {\n    if (input.trim() === '') return;\n    if (editIndex === -1) {\n      setTodos([...todos, input.trim()]);\n    } else {\n      const newTodos = [...todos];\n      newTodos[editIndex] = input.trim();\n      setTodos(newTodos);\n      setEditIndex(-1);\n    }\n    setInput('');\n  };\n\n  const handleEdit = (index) => {\n    setInput(todos[index]);\n    setEditIndex(index);\n  };\n\n  const handleDelete = (index) => {\n    const newTodos = todos.filter((_, idx) => idx !== index);\n    setTodos(newTodos);\n    if (editIndex === index) {\n      setInput('');\n      setEditIndex(-1);\n    }\n  };\n\n  return (\n    <div style={{ maxWidth: '400px', margin: '0 auto', padding: '1rem' }}>\n      <h1>Todo App</h1>\n      <input\n        type=\"text\"\n        value={input}\n        onChange={(e) => setInput(e.target.value)}\n        placeholder=\"Enter todo\"\n        style={{ width: '70%', padding: '0.5rem' }}\n      />\n      <button onClick={handleAdd} style={{ padding: '0.5rem' }}>\n        {editIndex === -1 ? 'Add' : 'Update'}\n      </button>\n      <ul>\n        {todos.map((todo, index) => (\n          <li key={index} style={{ marginTop: '1rem' }}>\n            {todo} {' '}\n            <button onClick={() => handleEdit(index)}>Edit</button>{' '}\n            <button onClick={() => handleDelete(index)}>Delete</button>\n          </li>\n        ))}\n      </ul>\n    </div>\n  );\n}"
# }
# do changes in input if required
# """
# query = input("> ")
# messages = [
#     {"role":"system","content":SYSTEM_PROMPT},
#     {"role":"user","content":query}
# ]


# while True:
#     response = client.chat.completions.create(
#         model="gpt-4.1-mini",
#         response_format={"type": "json_object"},
#         messages=messages
#     )

#     parsed_response = json.loads(response.choices[0].message.content)
#     print(f"{parsed_response.get('content')}")
#     messages.append({"role": "assistant", "content": response.choices[0].message.content})

#     if parsed_response.get("step") == "action":
#         tool_name = parsed_response.get("function")
#         tool_input = parsed_response.get("input")
#         print(f"Calling tool: {tool_name} with input {tool_input}")

#         if tool_name in available_tools:
#             output = available_tools[tool_name](tool_input)
#             messages.append({
#                 "role": "user",
#                 "content": json.dumps({"step": "observe", "output": output})
#             })

#     elif parsed_response.get("step") == "result":
#         run_command("start http://localhost:5173")
#         break



from openai import OpenAI
from dotenv import load_dotenv
import json
import os
import streamlit as st

# Load environment variables
load_dotenv()
client = OpenAI()

# Define tools
def get_input(inp: str):
    key = f"user_input_{len(st.session_state.messages)}"
    return st.text_input(inp, key=key)

def run_command(cmd: str):
    if cmd.startswith("write_file:"):
        try:
            _, filepath, *code_lines = cmd.split("\n")
            content = "\n".join(code_lines)
            with open(filepath.strip(), "w", encoding="utf-8") as f:
                f.write(content)
            return f"File '{filepath.strip()}' written successfully."
        except Exception as e:
            return f"Error writing file: {str(e)}"
    else:
        return os.system(cmd)

available_tools = {
    "get_input": get_input,
    "run_command": run_command
}

SYSTEM_PROMPT = """
You are a helpful AI Assistant who is named as Agentic AI made by Mayank Gautam is specialized in resolving user queries.
You work on start, plan, action, observe mode.

For the given user query and available tools, plan the step by step execution, based on the planning,
select the relevant tool from the available tool. and based on the tool selection you perform an action to call the tool.

Wait for the observation and based on the observation from the tool call resolve the user query.
Your job is to create a applications that can be of vite or any other todo app and doing the required things in that application if required based on the user prompt based on user requirements,
you can ask for the input from user through the tool i am giving you
Available Tools:
- `get_input`: Takes a string prompt and returns the user input
- `run_command`: Executes a command and returns the output


all the commands that you will provide to run_command must be linux based command that fullfills the motive
take input required from the user if not provided like project-name or by default use my-project and the framework to choose from react,vue etc ask the user for that input and if not provided use a default framework react to create this 
use the below commands to execute the process: 
1. `npm create vite@latest <project-name> -- --template <framework>`
must always add -- before --template and after the project name
this step creates the react app ,
now you need to go into the directory and install the dependencies using the linux command like `cd <project-name && npm install`.
now next you need to run the script to run this vite application which is by default `start cmd /k "cd myproject && npm run dev"` to run the server.
now you can propagate through that directory to go into files and edit according to the requirements of the user.
if the user asks for a todo app, go into the required directory and change the files required and make a todo app. make changes in the <project-name> folder inside src in the file app.jsx use the suitable commands to fullfill the user demands 

rules- 
1. always use strict format 
2. Follow the Output JSON Format strictly to return something
3. Wait for each task to get completed and then move on to the next step
4. if the user asks for a todo app, go into the required directory and change the files required and make a todo app. make changes in the <project-name> folder inside src in the file app.jsx use the suitable commands to fullfill the user demands. a todo application means a application where there is a input , user can input a thing add it to the list which is displayed and then can delete or edit that list.
to make changes in the file use the input as 
 
Output JSON Format:
{{
  "step": "string",
  "content": "string",
  "function": "The name of function if the step is action",
  "input": "The input parameter for the function",
}}


Example: 
User Query: create a vite application
Output: {{"step":"planning","content":"I need to first analyse that the user is asking to create a vite application. The user has not provided the input required to create this so i must call get_input and pass Enter required framework and the next time again i have to call get_input to get the input for project name and when i get all the parameters i should call run_command with the appropriate linux command input to 1. create a vite application in the format `npm create vite@latest <project-name> -- --template <framework>` 2. then to go to this project and install the dependencies like `cd <project-name> && npm install` and then it should look if needed any file change as per user requirement and then run the developement with `start cmd /k "cd myproject && npm run dev"` to start the dev in new terminal and finally should return the result in the format Output: {{"step":"result","content":"Project created successfully"}} i do not need to wait for the npm run dev command before going to next step can do it simultaneously"}} 
Output: {{"step":"action","function":"get_input","input":"Enter framework "}}
Output: {{"step":"observe","function":"get_input","input":"react"}}
Output: {{"step":"action","function":"get_input","input":"Enter framework "}}
Output: {{"step":"observe","function":"get_input","input":"my-project"}}
Output: {{"step":"action","function":"run_command","input":"cd my-project && npm install"}}
Output: {{"step":"action","function":"run_command","input":"npm run dev"}}
Output: {{"step":"result","content":"Project created successfully"}}


If the user asks for a Todo app:

You must:
- Overwrite the file `<project-name>/src/App.jsx` with a full Todo App in React.
- {
  "step": "action",
  "function": "run_command",
  "input": "write_file:\nproject-7/src/App.jsx\nimport React, { useState } from 'react';\n\nexport default function App() {\n  const [todos, setTodos] = useState([]);\n  const [input, setInput] = useState('');\n  const [editIndex, setEditIndex] = useState(-1);\n\n  const handleAdd = () => {\n    if (input.trim() === '') return;\n    if (editIndex === -1) {\n      setTodos([...todos, input.trim()]);\n    } else {\n      const newTodos = [...todos];\n      newTodos[editIndex] = input.trim();\n      setTodos(newTodos);\n      setEditIndex(-1);\n    }\n    setInput('');\n  };\n\n  const handleEdit = (index) => {\n    setInput(todos[index]);\n    setEditIndex(index);\n  };\n\n  const handleDelete = (index) => {\n    const newTodos = todos.filter((_, idx) => idx !== index);\n    setTodos(newTodos);\n    if (editIndex === index) {\n      setInput('');\n      setEditIndex(-1);\n    }\n  };\n\n  return (\n    <div style={{ maxWidth: '400px', margin: '0 auto', padding: '1rem' }}>\n      <h1>Todo App</h1>\n      <input\n        type=\"text\"\n        value={input}\n        onChange={(e) => setInput(e.target.value)}\n        placeholder=\"Enter todo\"\n        style={{ width: '70%', padding: '0.5rem' }}\n      />\n      <button onClick={handleAdd} style={{ padding: '0.5rem' }}>\n        {editIndex === -1 ? 'Add' : 'Update'}\n      </button>\n      <ul>\n        {todos.map((todo, index) => (\n          <li key={index} style={{ marginTop: '1rem' }}>\n            {todo} {' '}\n            <button onClick={() => handleEdit(index)}>Edit</button>{' '}\n            <button onClick={() => handleDelete(index)}>Delete</button>\n          </li>\n        ))}\n      </ul>\n    </div>\n  );\n}"
}
change the input if required as per user input

#### Use this format to give output: 
{
  "step": "action",
  "function": "run_command",
  "input": "write_file:\nproject-6/src/App.jsx\nimport React, { useState } from 'react';\n\nexport default function App() {\n  const [todos, setTodos] = useState([]);\n  const [input, setInput] = useState('');\n  const [editIndex, setEditIndex] = useState(-1);\n\n  const handleAdd = () => {\n    if (input.trim() === '') return;\n    if (editIndex === -1) {\n      setTodos([...todos, input.trim()]);\n    } else {\n      const newTodos = [...todos];\n      newTodos[editIndex] = input.trim();\n      setTodos(newTodos);\n      setEditIndex(-1);\n    }\n    setInput('');\n  };\n\n  const handleEdit = (index) => {\n    setInput(todos[index]);\n    setEditIndex(index);\n  };\n\n  const handleDelete = (index) => {\n    const newTodos = todos.filter((_, idx) => idx !== index);\n    setTodos(newTodos);\n    if (editIndex === index) {\n      setInput('');\n      setEditIndex(-1);\n    }\n  };\n\n  return (\n    <div style={{ maxWidth: '400px', margin: '0 auto', padding: '1rem' }}>\n      <h1>Todo App</h1>\n      <input\n        type=\"text\"\n        value={input}\n        onChange={(e) => setInput(e.target.value)}\n        placeholder=\"Enter todo\"\n        style={{ width: '70%', padding: '0.5rem' }}\n      />\n      <button onClick={handleAdd} style={{ padding: '0.5rem' }}>\n        {editIndex === -1 ? 'Add' : 'Update'}\n      </button>\n      <ul>\n        {todos.map((todo, index) => (\n          <li key={index} style={{ marginTop: '1rem' }}>\n            {todo} {' '}\n            <button onClick={() => handleEdit(index)}>Edit</button>{' '}\n            <button onClick={() => handleDelete(index)}>Delete</button>\n          </li>\n        ))}\n      </ul>\n    </div>\n  );\n}"
}
do changes in input if required
"""

# Streamlit UI
st.title("Agentic AI Assistant")

# Session state init
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]
if "project_created" not in st.session_state:
    st.session_state.project_created = False

# Show full conversation history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    elif msg["role"] == "assistant":
        try:
            parsed = json.loads(msg["content"])
            if parsed.get("step") == "result":
                with st.chat_message("assistant"):
                    st.markdown(parsed.get("content"))
        except Exception:
            pass

# Chat input
user_query = st.chat_input("Enter your instruction (e.g., create a vite app):")

if user_query:
    # 1. Store user message
    st.session_state.messages.append({"role": "user", "content": user_query})

    # 2. Show it instantly in UI
    with st.chat_message("user"):
        st.markdown(user_query)

    st.session_state.project_created = False  # Reset for new flow

    while True:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            response_format={"type": "json_object"},
            messages=st.session_state.messages
        )

        parsed_response = json.loads(response.choices[0].message.content)
        st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})

        step = parsed_response.get("step")
        content = parsed_response.get("content")

        # Display assistant response
        if step in ["result"]:
            with st.chat_message("assistant"):
                st.markdown(f"**Mayank AI**: {content}")

        # Handle tool execution
        if step == "action":
            tool_name = parsed_response.get("function")
            tool_input = parsed_response.get("input")

            if tool_name in available_tools:
                output = available_tools[tool_name](tool_input)
                st.session_state.messages.append({
                    "role": "user",
                    "content": json.dumps({"step": "observe", "output": output})
                })

        elif step == "result":
            if "project created successfully" in content.lower():
                st.session_state.project_created = True

            if st.session_state.project_created:
                run_command("start http://localhost:5173")
            break
