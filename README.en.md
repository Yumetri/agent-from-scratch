# Agent From Scratch

<p align="center">
  <img src="assets/agent-from-scratch-cover.png" alt="Agent From Scratch parody cover" width="360">
</p>

<p align="center">
  <sub>An unofficial parody cover generated with AI. This is not a real book and is not affiliated with any publisher.</sub>
</p>

[한국어](README.md) | **English**

Today, I click again.

The test code has been written, the tests have passed, and the commit message has been generated.  
While the click is running, I am already planning what to ask for next.

It is convenient.  
But it feels a little uncomfortable.

Shouldn't professionals try to understand how the tools they use actually work?

## Goal

Understand what happens behind each click, and become able to explain it instead of just pretending to know.

## Roadmap

1. [Build a ClaudeCode-like agent in 500 lines](notebooks/001_500_lines_claudecode.ipynb)

## Quick Start

```bash
uv sync
cp .env.example .env
uv run --group dev pytest
```

Add your OpenRouter or Gemini API key to `.env`. The lecture examples try OpenRouter first and fall back to Gemini when authentication fails or the OpenRouter key is missing.

Run the final lecture 1 example:

```bash
uv run python -m lecture_001_500_lines_claudecode.steps.step_05_code_agent
```

## Project Structure

```text
assets/                         Cover image
docs/                           Long-lived documentation
examples/001_500_lines_claudecode/                     Lecture 1 practice fixtures
notebooks/001_500_lines_claudecode.ipynb
src/lecture_001_500_lines_claudecode/      Lecture 1 agent implementation
tests/                          Step behavior and LLM provider tests
```

## Repository Policy

- Put real API keys in `.env`, and do not commit them.
- Keep lecture narrative in notebooks and runnable code in `src`.
- Put practice input files in `examples`, not `docs`.

## License

This project is licensed under the MIT License.
