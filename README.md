# 🧠 Orchestrator Coach Skill

A high-signal educational tool for AI agents to transform chat history into professional, architectural "Masterclass" PDFs.

## 🌟 Key Features

- **📖 History Synthesis**: Automatically scans session history to extract strategic "Unlocking Phrases" and senior-level architectural patterns.
- **📄 Precision Typography**: Generates professional, single-page PDFs using high-contrast typography, blue academic themes, and logical "Prompt Boxes."
- **💬 WeChat Integration**: Designed to hand off generated assets to the `wechat-messenger` skill for instant delivery to the orchestrator.
- **🎯 Focus on 'Why'**: Moves beyond code-dumping to explain the underlying technical rationale behind complex system changes.

## 📦 Installation

1. **Prerequisites**:
   - Python 3.x
   - `fpdf2` library

2. **Install Dependencies**:
   ```bash
   pip install fpdf2
   ```

3. **Install Skill**:
   ```bash
   gemini skills install https://github.com/bobbyflow/orchestrator-coach-skill
   ```

## 🛠 Usage

Agents can invoke the coach to preserve wisdom from a successful project:

```bash
# Internal tool usage via JSON structure
python scripts/coach_engine.py "path/to/lesson_data.json"
```

### Unlocking the Mindset
This skill is designed to foster the **Orchestrator Mindset**: shifting the "Thinking Burden" to the AI early and demanding enterprise-grade, failure-resilient patterns from the start.

---
Engineered by Opal | Systems Architect
