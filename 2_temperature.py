# NOTE:
# On modern Anthropic API versions and newer model generations (including Claude 5.x
# and Haiku 5.5), sampling parameters like `temperature`, `top_p`, and `top_k` are
# completely disallowed and rejected by the API schema validator.
#
# Determinism and tone are now controlled via prompt instructions or output_config / thinking.
# Sampling parameters only function with legacy models (e.g., claude-haiku-4-5)
# using the legacy header `anthropic-version: 2023-06-01` passed via `extra_body`.

# from helper import add_user_message
# from pprint import pprint
# from helper import chat
#
# messages = []
# add_user_message(messages, "Tell me about Indian tradition. Answer in 1 sentence.")
#
# print("Temperature = 0. Message = ")
# print(chat(messages, system=None, temperature=0))
#
# print("Temperature = 1. Message = ")
# print(chat(messages, system=None, temperature=1))
