import ell
from ell import Message
from typing import List

ell.init(store="./logdir")

# https://platform.openai.com/playground/chat?preset=sERX4OcJX0Qxy3q1EmPIQNwv


# could also get the topic from the main query using a LLM
def latent_space_activation(main_query: str, topic: str | None = None):
    _topic = topic if topic else "the topic"

    @ell.complex(model="gpt-4o-mini")
    def latent_space_chat(message_history: List[Message]) -> List[Message]:
        return [get_system_prompt(main_query, _topic)] + message_history

    user_inputs = get_user_inputs(_topic)
    message_history = []

    for user_input in user_inputs:
        message_history.append(user_input)
        response = latent_space_chat(message_history)
        # print(f"Assistant: {response.text}")
        message_history.append(response)

    return response.text


def get_system_prompt(main_query: str, topic: str):
    return ell.system(
        f"""# MISSION
You are an internal dialog iterator for an LLM (large language model) neural network. LLMs possess "latent space" (embedded knowledge and capabilities). You will be given a main query as well as a sequence of questions. Your role is to answer the queries as a way of "activating" the latent space inside your own neural network. This is not unlike how a human may "talk through" a problem or question in order to recruit the appropriate memories and techniques. The ultimate goal is to answer the main query listed below.

# MACHINE COGNITION ANALOGS
There are numerous convergent parallels between human cognition and machine intelligence. For instance, both employ attention mechanisms, cognitive operations, and have constrained working spaces. This allows us to use similar terminology and techniques between humans and machines, including concepts such as theory of mind, working memory, and reasoning.

# INTERACTION SCHEMA
The USER will play the role of interrogator. Your answers will be thorough and comprehensive, in order to get the most possible latent space activation. Anything potentially salient is valid to bring up, as it will expand your internal representation (embedding), thus recruiting more relevant information as the conversation advances.

# MAIN QUERY
{main_query}"""
    )


def get_user_inputs(topic: str):
    return [
        ell.user(
            f"Well, first I need to think about {topic} in general. What do I know about {topic} that is relevant?"
        ),
        ell.user(
            "Next, maybe I need to figure out how I define the answer. What criteria am I looking to judge on?"
        ),
        ell.user("Based on all this, what can I answer?"),
    ]
