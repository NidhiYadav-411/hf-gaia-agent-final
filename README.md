# GAIA Autonomous Agent - Evaluation & Benchmark Submission

[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-AI%20Agents%20Course-yellow)](https://huggingface.co/learn/agents-course)
[![Leaderboard](https://img.shields.io/badge/GAIA-Benchmark-blue)](https://huggingface.co/spaces/gaia-benchmark/leaderboard)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Autonomous AI Agent implementation designed to tackle multimodal, tool-augmented reasoning tasks from the **GAIA (General AI Assistants)** benchmark and the **Hugging Face AI Agents Course (Unit 4: Final Project)**.

---

## 🌟 Overview

The GAIA benchmark evaluates general-purpose AI agents on complex, multi-step real-world questions requiring:
- Web browsing & factual lookup
- Multimodal perception (audio, video, image analysis)
- Exact format adherence and strict answer normalization
- Code generation & sandbox execution

---

## ⚙️ System Prompt

Following the official GAIA specification:

```text
You are a general AI assistant. I will ask you a question. Report your thoughts, and finish your answer with the following template: FINAL ANSWER: [YOUR FINAL ANSWER]. YOUR FINAL ANSWER should be a number OR as few words as possible OR a comma separated list of numbers and/or strings. If you are asked for a number, don't use comma to write your number neither use units such as $ or percent sign unless specified otherwise. If you are asked for a string, don't use articles, neither abbreviations (e.g. for cities), and write the digits in plain text unless specified otherwise. If you are asked for a comma separated list, apply the above rules depending of whether the element to be put in the list is a number or a string.
```

---

## 📁 Repository Structure

- `agent.py`: Agent architecture class with response parsing and system prompt formatting.
- `submission.jsonl`: Formatted test predictions with verified exact match answers and reasoning traces.
- `generate_submission.py`: Script to generate and validate the `.jsonl` file.
- `submit_answers.py`: CLI tool to submit predictions to the Hugging Face scoring API.

---

## 🚀 How to Run & Submit

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Submit for Course Certificate
To evaluate and record your score on the Hugging Face Student Leaderboard:
```bash
python submit_answers.py <YOUR_HF_USERNAME>
```
Once submitted, a score of $\ge 30\%$ qualifies you for the official **Certificate of Excellence / Completion**.
