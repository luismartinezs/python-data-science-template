from typing import List
from ell import ell
from pydantic import BaseModel

ell.init(store="./logdir")


class StoryIdeasResponse(BaseModel):
    ideas: List[str]


@ell.complex(model="gpt-4o-mini", response_format=StoryIdeasResponse)
def generate_story_ideas(n: int = 3, theme: str = ""):
    theme_prompt = f" based on the provided theme\n\n[THEME]\n{theme}" if theme else ""
    return [
        ell.system(
            "You are a creative assistant. Generate unique story ideas based on the user's request."
        ),
        ell.user(f"Please generate {n} unique story ideas{theme_prompt}."),
    ]


@ell.complex(model="gpt-4o-mini", max_tokens=150)
def write_a_draft_of_a_story(idea: str):
    return [
        ell.system(
            "Write a short and concise draft of a story based on the given idea."
        ),
        ell.user(idea),
    ]


@ell.complex(model="gpt-4o-mini")
def choose_the_best_draft(drafts: List[str]):
    formatted_drafts = "\n\n".join(
        f"Draft {i+1}:\n{draft}" for i, draft in enumerate(drafts)
    )
    return [
        ell.system("Choose the best draft from the given drafts."),
        ell.user(f"Drafts:\n\n{formatted_drafts}"),
    ]


@ell.complex(model="gpt-4o-mini")
def write_a_really_good_story(theme: str = "", style: str = "") -> str:
    ideas_response = generate_story_ideas(theme=theme)

    drafts = []
    for idea in ideas_response.parsed.ideas:
        draft_response = write_a_draft_of_a_story(idea)
        drafts.append(draft_response.text)

    best_draft_response = choose_the_best_draft(drafts)

    style_prompt = f"[STYLE]\n{style}" if style else ""
    system_prompt = f"You are a story writer. You are given a draft of a story and you need to write a really good story in the given style\n\n{style_prompt}."
    return [ell.system(system_prompt), ell.user(best_draft_response)]


story = write_a_really_good_story(
    theme="realistic hyperfuturistic slice of life",
    style="in the writing style of Isaac Asimov",
)
print(story.text)
