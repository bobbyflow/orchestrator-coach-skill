---
name: orchestrator-coach
description: Analyzes project history to extract architectural lessons and generates a professional, single-page PDF "Masterclass" delivered via WeChat. Use when the user asks to "save a lesson," "teach me how we did this," or "summarize our orchestration strategy."
---

# Orchestrator Coach

This skill transforms messy chat history into high-signal educational assets. It identifies the "Atomic Patterns" and "Strategic Mindsets" developed during a session.

## Tools

### generate_lesson_pdf
Generates a professional PDF from a structured lesson JSON.

- **Arguments**:
  - `data_file`: Path to a JSON file containing the lesson structure (title, chapters, bodies, prompts).

- **Command**:
  `python C:\Users\choib\.gemini\skills\orchestrator-coach\scripts\coach_engine.py "<data_file>"`

## Workflow

1.  **Analyze History**: Scan the current and past sessions in `C:\Users\choib\.gemini	mp\choib\chats`.
2.  **Synthesize Lesson**: Identify one core architectural success (e.g., the WeChat Bridge) and three "Unlocking Commands" that made it possible.
3.  **Draft JSON**: Create a temporary JSON file with the following structure:
    ```json
    {
      "title": "STRATEGIC TITLE",
      "output_path": "C:\Users\choib\lesson_name.pdf",
      "sections": [
        { "type": "chapter", "content": "Concept Name" },
        { "type": "body", "content": "Theoretical explanation..." },
        { "type": "prompt", "content": "Prompt example..." }
      ]
    }
    ```
4.  **Execute**: Call `generate_lesson_pdf`.
5.  **Deliver**: Use the `wechat-messenger` skill to send the resulting PDF to the user.

## Constraints
- **Strict One-Page**: The agent must keep content concise to ensure the PDF engine fits everything on a single page.
- **No Symbols**: Headers must be plain text (no emojis or symbols in titles).
- **High Signal**: Focus on *why* a decision was made, not just *what* code was written.
