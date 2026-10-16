"""
GAIA Agent Implementation
Evaluated on General AI Assistants (GAIA) Benchmark & Hugging Face Agents Course Unit 4.
"""

import os
import re
from typing import Dict, Any, Optional

SYSTEM_PROMPT = """You are a general AI assistant. I will ask you a question. Report your thoughts, and finish your answer with the following template: FINAL ANSWER: [YOUR FINAL ANSWER]. YOUR FINAL ANSWER should be a number OR as few words as possible OR a comma separated list of numbers and/or strings. If you are asked for a number, don't use comma to write your number neither use units such as $ or percent sign unless specified otherwise. If you are asked for a string, don't use articles, neither abbreviations (e.g. for cities), and write the digits in plain text unless specified otherwise. If you are asked for a comma separated list, apply the above rules depending of whether the element to be put in the list is a number or a string."""


class GaiaAgent:
    """Autonomous agent configured for solving GAIA benchmark multi-modal and reasoning tasks."""

    def __init__(self, model_name: str = "gpt-4o", system_prompt: str = SYSTEM_PROMPT):
        self.model_name = model_name
        self.system_prompt = system_prompt

    def parse_final_answer(self, response_text: str) -> str:
        """Extract final answer formatted according to GAIA specification."""
        match = re.search(r"FINAL ANSWER:\s*\[?(.*?)\]?$", response_text.strip(), re.MULTILINE)
        if match:
            return match.group(1).strip()
        # Fallback to last line if template not explicitly found
        lines = [line.strip() for line in response_text.strip().split("\n") if line.strip()]
        return lines[-1] if lines else ""

    def solve(self, question: str, file_path: Optional[str] = None) -> Dict[str, Any]:
        """Process a task and generate the final answer with reasoning trace."""
        # Custom reasoning and tool invocation logic goes here
        # E.g., web search, code sandbox, audio transcription, image inspection
        return {
            "model_answer": "",
            "reasoning_trace": ""
        }


if __name__ == "__main__":
    agent = GaiaAgent()
    print("GAIA Agent initialized with system prompt:")
    print(agent.system_prompt)
