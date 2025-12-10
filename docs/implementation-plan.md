# Travel AI Agent: Implementation Document

Persona: Business entrepreneur and seasoned software engineer (10+ years).

## Overview

Build an AI-driven assistant that simulates a professional travel agency workflow, guiding users through destination selection, transport, accommodation, food, sites to visit, and on-site transportation. Output is a summarized plan and optional day-by-day itinerary.

## Requirements

- Destinations: Europe, Asia, Africa, Americas
- From-home transport: bus, train, airplane (5 choices each per destination)
- Accommodation: 5 choices each per destination
- Food restaurants: 5 choices each per destination
- Sites to visit: 5 choices each per destination
- On-site transport: taxi, Uber, private chauffeur, public transportation (5 choices each per destination)
- Simple, bullet-based formatting; copy-friendly for Google Docs

## Architecture

- Prompt-first approach: Use structured prompts to drive the agent via LLMs (Copilot, ChatGPT, Claude, Gemini).
- Stateless interactions with clear confirmations at each step.
- Data sourcing: Curated lists or dynamic generation via LLM with constraints (numbers, categories, descriptions).

## Modules

- Prompt Templates: `prompts/workshop-prompt.md` as the master prompt.
- Interaction Orchestrator: Step-by-step flow enforced by prompt sections.
- Output Formatter: Bulleted summary and simple itinerary; consistent structure.

## Data Strategy

- Prefer dynamically generated suggestions from the LLM.
- For demo consistency, include fallback curated examples for each region and category.
- Keep descriptions short; include price/time ranges only if requested.

## User Flow

1. Choose destination region.
2. Select initial transport from home (bus/train/airplane; 5 choices each).
3. Pick accommodation (5 choices).
4. Pick food options (5 choices).
5. Pick tourist/cultural sites (5 choices).
6. Pick on-site transport (5 choices).
7. Review and export the final plan.

## Non-Functional Considerations

- Usability: Simple language, numbered choices, confirmations.
- Portability: Markdown output; copy-ready for Google Docs.
- Safety: Clarify suggestions; advise verification of prices and availability.

## Deliverables

- Workshop curriculum: `docs/workshop-curriculum.md`
- Master prompt: `prompts/workshop-prompt.md`
- Technical stack: `docs/technical-stack.md`
- Git workflow: `docs/git-workflow.md`
- Portable aggregated doc: `docs/portable.md`

## Roadmap

- v1: Prompt-only agent with curated examples.
- v2: Optional data enrichment (APIs for hotels/transport where feasible).
- v3: UI wrapper (web or chat) for guided selections.
