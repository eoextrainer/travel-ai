# End-to-End Artificial Intelligence Course: Build a Travel AI Agent (2 Hours)

Audience: Non-technical participants with limited computer knowledge.
Instructor Persona: Business entrepreneur and seasoned software engineer (10+ years).
Language: Simple, friendly, and actionable.
Optimization: Usable with Microsoft Copilot, ChatGPT, Claude, Gemini.

---

## Course Objectives
- Understand what an AI agent is and how prompts guide it.
- Build a Travel AI Agent using a clear, structured prompt.
- Practice interactive planning: destination, transport, accommodation, food, sites, local transport.
- Produce a final travel plan and simple itinerary ready to copy into Google Docs.
- Learn a lightweight project workflow and version control basics (Git).

## Time & Agenda (2 Hours)
- Part 1 (20 min): Introduction to AI Agents (Plain English)
- Part 2 (30 min): Designing the Prompt & Flow
- Part 3 (40 min): Interactive Agent Session (Hands-on)
- Part 4 (20 min): Personalization & Export
- Part 5 (10 min): Next Steps & Resources

---

## Materials Checklist
- A device with internet access and a browser
- Access to any LLM assistant (Microsoft Copilot, ChatGPT, Claude, Gemini)
- The master prompt (see section below)
- Optional: Google Docs to copy final plan

---

## Part 1 (20 min): Introduction to AI Agents
Plain-English overview. No coding.

1. What is an AI agent?
   - A smart assistant that follows instructions (a “prompt”) to do tasks.
   - We will guide it step by step to behave like a travel agent.
2. What will our agent do?
   - Offer structured choices for destination, transport, accommodation, food, sites, and local transport.
   - Present 5 curated choices per category for each destination.
3. How do we control it?
   - With a clear, structured prompt. Prompts are like recipes.
4. Tools we’ll use (no deep dive):
   - Any AI assistant (Copilot, ChatGPT, Claude, Gemini) + a text prompt.
5. Outcome of the workshop:
   - A ready-to-use prompt and a simple workflow to generate a travel plan.

Reference: See `docs/workshop-curriculum.md`.

---

## Part 2 (30 min): Designing the Prompt & Travel Flow
Hands-on prompt design. No coding.

1. Start friendly and clear.
   - “Help me plan a trip with destination, transport, accommodation, food, sites, and local transport.”
2. Add structure for each step:
   - Destination: Offer 4 regions and let the user pick.
   - Transport from home: Provide bus, train, airplane options (5 each).
   - Accommodation: 5 choices by price/comfort.
   - Food: 5 restaurants per destination (local cuisine, budget → upscale).
   - Sites: 5 tourist/cultural places with short descriptions.
   - On-site transport: 5 choices including taxi, Uber, private chauffeur, public transit.
3. Make it interactive:
   - Show options step by step; confirm after each selection.
4. Keep language simple:
   - Short sentences, bullets, numbers.
5. Practice:
   - Participants copy the base prompt and try it with an AI assistant.

Tips:
- Ask the AI: “Use bullets and keep it concise.”
- Ask: “Rephrase this in simpler words,” when needed.

Reference: See `prompts/workshop-prompt.md`.

---

## Master Prompt (Copy/Paste)
Use the following starter prompt with your AI assistant. It’s optimized for Copilot, ChatGPT, Claude, and Gemini.

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

Reference: Full prompt guide in `prompts/workshop-prompt.md`.

---

## Part 3 (40 min): Interactive Agent Session
Hands-on guided practice.

1. Choose a destination region.
   - AI lists Europe, Asia, Africa, Americas; you pick one.
2. Transportation from home.
   - AI offers 5 bus, 5 train, 5 airplane choices; you pick one.
3. Accommodation.
   - AI suggests 5 options from budget → luxury; you pick one.
4. Food options.
   - AI lists 5 restaurants; pick one or more.
5. Tourist & cultural sites.
   - AI provides 5 places with short descriptions; you pick.
6. On-site transport.
   - AI offers 5 choices including taxi, Uber, private chauffeur, public transit.
7. Review your plan.
   - AI summarizes selections and proposes a simple daily itinerary.

Facilitator guidance:
- Encourage alternatives on request.
- Suggest asking for price ranges and travel times.
- Remind participants to copy the plan to Google Docs.

Reference: See `docs/workshop-curriculum.md`.

---

## Part 4 (20 min): Personalization & Export
1. Personalize.
   - Ask AI to adjust for budget, dates, family needs, accessibility.
2. Export.
   - Ask AI for final plan in clean bullets; copy to Google Docs.
   - Optional: Ask for a day-by-day itinerary.
3. Safety & expectations.
   - These are suggestions; verify prices and availability.

Reference: See `docs/workshop-curriculum.md`.

---

## Part 5 (10 min): Next Steps & Resources
- Try different regions and compare plans.
- Include travel insurance or visa tips if needed.
- Save your prompts for future trips.
- Use `docs/portable.md` to copy the essentials quickly.

---

## Implementation Overview (For Instructor Reference)
- Prompt-first: Drive flow via structured LLM prompt.
- Data: Dynamic generation with optional curated examples for consistency.
- Output: Bulleted summary + simple itinerary; copy-friendly.
- Deliverables: Curriculum, prompt, tech stack, Git workflow, portable doc.

Reference: See `docs/implementation-plan.md`.

---

## Technical Stack (For Instructor Reference)
- LLMs: Microsoft Copilot, ChatGPT, Claude, Gemini
- Documents: Markdown; optional JSON/YAML for structure
- Tools: VS Code (optional), Git, GitHub repo `git@github.com:eoextrainer/travel-ai.git`
- Optional runtime: Python 3.10+ or Node.js 18+ if wrapping in a CLI/UI later

Reference: See `docs/technical-stack.md`.

---

## Version Control & Workflow (Optional Module)
Repository: `git@github.com:eoextrainer/travel-ai.git`

Quick start commands (run in project root):

```bash
git init
git remote add origin git@github.com:eoextrainer/travel-ai.git

git checkout -b docs/workshop
git add .
git commit -m "docs: scaffold workshop and prompt"
git push -u origin docs/workshop
```

Branching and commits:
- `main` protected; PRs required
- Branches: `feature/<name>`, `docs/<name>`, `fix/<name>`
- Messages: concise and focused (e.g., `docs: add workshop curriculum`)

Reference: See `docs/git-workflow.md`.

---

## Exercises & Handouts
- Exercise A: Run the master prompt and choose Europe; complete all selections.
- Exercise B: Personalize for a family with kids; add two kid-friendly activities.
- Exercise C: Ask for budget ranges; refine accommodation and food picks.
- Handout: Copy the “Master Prompt” and keep the “Flow Steps” summary.

---

## Assessment (Lightweight)
- Participant can produce a complete plan with all choices.
- Participant can request alternatives and confirm steps.
- Participant can copy the final plan into Google Docs.

---

## Facilitation Notes
- Pace the interaction; ensure everyone completes each step.
- Reiterate simple language and confirmations after each choice.
- Encourage participants to save their final prompts and outputs.

---

## Appendix: Flow Steps (Quick Reference)
1. Destination region (Europe, Asia, Africa, Americas)
2. From-home transport (bus/train/airplane, 5 choices each)
3. Accommodation (5 choices, budget → luxury)
4. Food (5 restaurants)
5. Tourist/cultural sites (5 places with short descriptions)
6. On-site transport (5 choices including taxi, Uber, private chauffeur, public transit)
7. Summary + simple daily itinerary

---

## Copy-Friendly Export Tips
- Ask the AI for clean bullets and numbered lists.
- Keep option descriptions to one line.
- Paste into Google Docs and adjust headings as needed.
