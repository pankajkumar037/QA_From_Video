import os
from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv 


load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
api_key=os.getenv("GOOGLE_API_KEY")

config_list = [{
    "model": "gemini-2.0-flash",
    "api_key": os.environ.get("GOOGLE_API_KEY"),
    "api_type": "google",
}]


def get_agent_response_from_video(trancribed_text,query):
    llm_config = { "config_list": config_list }
    assistant = AssistantAgent(
        "assistant",
        llm_config=llm_config,
        system_message="""You are an AI that answers questions based on a provided video transcript.
                        If the answer is not available in given transcript, explicitly say "I DONT KNOW" and suggest searching the web."""

                    )


    user_proxy = UserProxyAgent(
        "user_proxy", 
        code_execution_config=False,
        human_input_mode="NEVER",
        max_consecutive_auto_reply=0
    )




    agent_prompt=f"""answer the query:\n\n{trancribed_text}\n\nQuery: {query}"""

    # Start the chat
    chat_response =user_proxy.initiate_chat(
        assistant,
        message=agent_prompt,
    )

    return chat_response
