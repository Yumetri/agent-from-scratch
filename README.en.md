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
One click moves several steps of work forward in moments.

The faster the results arrive, the more curious I become. What is actually happening behind that click?

Rather than stopping at how to use the tool, I decided to build a small agent and follow the process myself.

## Goal

Understand what happens behind each click, explain how an agent works, and rebuild its core structure in a small amount of code.

## Roadmap

1. [Lecture 1: Build Claude Code in 500 Lines](notebooks/001_500_lines_claudecode.ipynb)

## Lecture 01 — Build Claude Code in 500 Lines

Start with a memoryless LLM call and develop it into a code-editing agent that can read files, make changes, and verify execution results.

Core concepts covered in this lecture:

- Conversation history as the agent's memory
- The difference between imitating function calls in a prompt and actual Tool Calling
- A Tool Feedback Loop that returns execution results to the model
- Tools for exploring, creating, and editing files
- Verifying work through JavaScript execution results
- A Workspace Guard that blocks access outside the working directory

| Step | Capability added | Core concept |
| --- | --- | --- |
| 0 | Send only the current input to the LLM | An LLM API does not remember conversations automatically |
| 1 | Accumulate previous messages | Conversation history creates the agent's memory |
| 2 | Call `read_file` | The model creates structured Tool Calls |
| 3 | Return tool results to the model | The Tool Feedback Loop lets the task continue |
| 4 | Explore, create, and edit files | Multiple tools work together to complete real tasks |
| 5 | Run code and protect paths | Execution is verified while the workspace stays constrained |
