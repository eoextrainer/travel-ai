# Travel AI Workshop Portable Document

This single Markdown aggregates the curriculum, prompt, implementation overview, and Git workflow for quick copying into Google Docs.

---

## Curriculum (2 Hours, Non-Technical)

See `docs/workshop-curriculum.md` for detailed steps. Highlights:

- Clear, friendly intro to AI agents
- Step-by-step interactive travel planning
- Choices for destination, transport, accommodation, food, sites, local transport
- Final summary and itinerary; copy-friendly output

---

## Master Prompt (Copy/Paste)

See `prompts/workshop-prompt.md`. Starter:

"""
Hello! Help me plan a trip using a step-by-step flow.

Please follow this structure:

1) Offer regions (Europe, Asia, Africa, Americas). I’ll pick one.
2) Offer 5 bus, 5 train, and 5 airplane choices from my home to that destination. I’ll pick one.
3) Offer 5 accommodation choices (budget to luxury). I’ll pick one.
4) Offer 5 food/restaurant options. I’ll pick one or more.
5) Offer 5 tourist/cultural sites with short descriptions. I’ll pick.
6) Offer 5 on-site transport options. I’ll pick one.
7) Summarize my selections and propose a simple daily itinerary.

Use bullets, keep text short, and confirm after each choice.
"""

---

## Implementation Overview

- Prompt-first: Drive flow via structured LLM prompt
- Data: Dynamically generated options; optional curated examples
- Output: Bulleted summary + simple itinerary, copy-friendly
- Deliverables: Curriculum, prompt, tech stack, Git workflow, portable doc

---

## Git Workflow (Quick Start)

Repository: `git@github.com:eoextrainer/travel-ai.git`

```bash
git init
git remote add origin git@github.com:eoextrainer/travel-ai.git

git checkout -b docs/workshop
git add .
git commit -m "docs: scaffold workshop and prompt"
git push -u origin docs/workshop
```

Branching: `main` protected; feature/docs/fix branches; PRs required.
