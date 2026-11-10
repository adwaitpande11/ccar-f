from utils import get_current_datetime
from helper import add_tool_message
from helper import add_assistant_message
from utils import get_current_datetime_schema
from helper import add_user_message
from pprint import pprint
from helper import chat_with_tool

TOOL_MAP = {
    "get_current_datetime": get_current_datetime,
}

messages = []
add_user_message(messages, "What is the exact time, formatted as HH:MM:SS and also separately as MM/DD/YYYY HH:MM:SS?")

tools_to_invoke = chat_with_tool(messages, tools=[get_current_datetime_schema])
add_assistant_message(messages, tools_to_invoke)

for tool_to_invoke in tools_to_invoke:
    tool_result = TOOL_MAP[tool_to_invoke.name](**tool_to_invoke.input)
    add_tool_message(messages, tool_use_id=tool_to_invoke.id, text=tool_result)

final_tool_result = chat_with_tool(messages, tools=[get_current_datetime_schema])

pprint(final_tool_result)