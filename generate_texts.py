import openai
import config

# Replace YOUR_API_KEY with your OpenAI API key
openai.api_key = config.CHAT_GPT_API_KEY

def generate_youtube_title(content):
    # Set the model and prompt
    model_engine = "gpt-3.5-turbo"

    # Set the maximum number of tokens to generate in the response
    max_tokens = 250

    message_log = [
        {"role": "system", "content": content.get("prompt")},
    ]

    # Generate a response
    response = openai.ChatCompletion.create(
        model=model_engine,  # The name of the OpenAI chatbot model to use
        messages=message_log,   # The conversation history up to this point, as a list of dictionaries
        max_tokens=max_tokens,        # The maximum number of tokens (words or subwords) in the generated response
        stop=None,              # The stopping sequence for the generated response, if any (not used here)
        temperature=0.7,        # The "creativity" of the generated response (higher temperature = more creative)
    )

    print(response)

    # Find the first response from the chatbot that has text in it (some responses may not have text)
    for choice in response.choices:
        if "text" in choice:
            return choice.text.upper().rstrip('"').lstrip('"')

    # If no response with text is found, return the first response's content (which may be empty)
    return response.choices[0].message.content.upper().rstrip('"').lstrip('"')

if __name__ == "__main__":
    print(generate_youtube_title(config.CONTENT_TABLE[0]))
