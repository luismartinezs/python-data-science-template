import ell

ell.init(store="./logdir")

def zero_shot_cot_user_message(user_prompt: str):
    return ell.user(user_prompt + "\n\nfirst generate your reasoning and then the outputs\n\n[REASONING]\n\nmy_reasoning: <Your careful and step-by-step reasoning before you return the desired outputs>\n\n[OUTPUT]\n\nmy_response: <your final response here>")

__all__ = ["zero_shot_cot_user_message"]
