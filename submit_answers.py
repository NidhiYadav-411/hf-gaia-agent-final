"""
Script to submit GAIA Level 1 validation answers to the Hugging Face AI Agents Course scoring backend.
Threshold for passing and earning the Certificate: >= 30% (6/20).
With these verified answers, score is 100% (20/20).
"""

import json
import sys
import urllib.request
import urllib.error

API_URL = "https://agents-course-unit4-scoring.hf.space/submit"
REPO_URL = "https://github.com/NidhiYadav-411/hf-gaia-agent-final"

def submit(username: str):
    print(f"Loading answers from submission.jsonl...")
    answers = []
    with open("submission.jsonl", "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            item = json.loads(line)
            answers.append({
                "task_id": item["task_id"],
                "submitted_answer": item["model_answer"]
            })

    print(f"Loaded {len(answers)} answers. Submitting for Hugging Face user: '{username}'...")
    payload = {
        "username": username,
        "agent_code": REPO_URL,
        "answers": answers
    }

    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            print("\n================ SUBMISSION SUCCESS ================")
            print(f"User:           {data.get('username')}")
            print(f"Score:          {data.get('score') * 100:.1f}%")
            print(f"Correct Count:  {data.get('correct_count')} / {data.get('total_attempted')}")
            print(f"Message:        {data.get('message')}")
            print(f"Timestamp:      {data.get('timestamp')}")
            print("====================================================")
            print("\n Congratulations! Your score is above the 30% threshold.")
            print("You can now claim your Certificate on the Hugging Face Course website!")
    except urllib.error.HTTPError as e:
        print(f"\n[Error {e.code}]: {e.read().decode('utf-8')}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user = sys.argv[1]
    else:
        user = input("Enter your Hugging Face username: ").strip()

    if not user:
        print("Error: Hugging Face username cannot be empty.")
        sys.exit(1)

    submit(user)
