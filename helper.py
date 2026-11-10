from anthropic import Anthropic

client = Anthropic()
model = "claude-haiku-5-5"

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def add_tool_message(messages, tool_use_id, text=None, is_error=False):
    tool_message = {"role": "user", "content": [{
        "type": "tool_result",
        "tool_use_id": tool_use_id,
        "content": text,
        "is_error": True if not text else is_error
    }]}
    messages.append(tool_message)

def chat(messages, system=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages
    }
    
    if system:
        params["system"] = system
    
    message = client.messages.create(**params)
    return message.content[0].text


def chat_with_tool(messages, system=None, tools=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages
    }
    
    if system:
        params["system"] = system

    if tools:
        params["tools"] = tools
    
    message = client.messages.create(**params)
    return message.content