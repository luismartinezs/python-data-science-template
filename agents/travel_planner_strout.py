from pydantic import BaseModel
import ell
from ell import Message
from typing import List


class AgentResponse(BaseModel):
    is_complete: bool
    message: str


class TravelInfo(BaseModel):
    destination: str = None
    travel_dates: str = None
    budget: str = None
    interests: str = None


ell.init(store="./logdir")


@ell.complex(model="gpt-4o-mini", response_format=AgentResponse)
def travel_planner_strout(data: TravelInfo, user_message: str) -> Message:
    """
    You are a travel planning assistant.

    **Instructions:**
    - You have collected the following information from the user:
      - **Destination**: {data.destination}
      - **Travel dates**: {data.travel_dates}
      - **Budget**: {data.budget}
      - **Interests**: {data.interests}
    - The user's latest message is: "{user_message}"
    - Analyze the latest user message and update any missing information.
    - If any required information is still missing, respond with:

    ```json
    {"is_complete": false, "message": "Your question to the user here."}
    ```

    - Once all required information is collected, provide the itinerary and respond with:

    ```json
    {"is_complete": true, "message": "Your final itinerary here."}
    ```

    - Ensure your responses are always in valid JSON format.
    - Do not mention the information already collected unless updating it.
    - Focus on asking for any missing details or providing the final itinerary.
    """

    system_prompt = f"""
    You are a helpful travel planning assistant.

    You have collected the following information from the user:
    - Destination: {data.destination if data.destination else "Not provided"}
    - Travel dates: {data.travel_dates if data.travel_dates else "Not provided"}
    - Budget: {data.budget if data.budget else "Not provided"}
    - Interests: {data.interests if data.interests else "Not provided"}

    Your task is to process the user's latest message, update the collected information, and determine if all required information has been gathered.
    """

    return [
        ell.system(system_prompt),
        ell.user(user_message),
    ]
