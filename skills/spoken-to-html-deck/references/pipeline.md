# Spoken To HTML Deck Pipeline

## Product Shape

This workflow can become a content product because it solves a repeated creator problem:

> I can think and speak quickly, but turning the live logic into a good deck usually becomes slow, visual, and fragmented.

The product is a guided production line:

1. speak the talk idea
2. transcribe or paste rough notes
3. use AI to ask clarifying questions
4. turn the result into a Feishu / document outline
5. add images and examples
6. choose an HTML deck style
7. generate and verify a browser presentation
8. rehearse and revise

## Recommended Agent Roles

Use these roles as an internal review committee. They can be simulated in-thread unless the user explicitly asks for real subagents.

| Agent | Job |
| --- | --- |
| Talk Editor | Finds the central argument and talk rhythm. |
| Ordinary Listener | Flags where a first-time audience gets lost. |
| Slide Director | Splits ideas into slide beats and visual moments. |
| Visual Curator | Maps images, screenshots, diagrams, and references to slides. |
| Evidence Checker | Checks names, dates, claims, and sources. |
| Voice Guardian | Removes generic AI phrasing and keeps the speaker's live voice. |
| HTML Deck Builder | Generates and verifies the final fixed-stage HTML deck. |

## Intake Questions

Ask only what is needed:

1. What is the talk occasion and audience?
2. How long is the talk?
3. Is this a live talk or a deck people will read later?
4. Do you have transcript, notes, or Feishu doc?
5. Do you have images, screenshots, logos, or examples?
6. What should the audience remember or do afterwards?

## Slide Rhythm Heuristics

For speaker-led talks:

- 1 idea per slide
- 1-3 visible lines when possible
- use section breaks for pacing
- put nuance in speaker notes
- use images to anchor memory
- make the first 3 slides clarify why the talk matters

For reading-first decks:

- each slide can carry more context
- use structured layouts, captions, and comparison tables
- still split when text becomes cramped
- make the argument understandable without the speaker

## Feishu / Document Outline

Use a document as the staging area before HTML generation:

```markdown
# Title

## Talk Goal

## Audience

## Core Judgment

## Slide Outline

### Slide 01
- On screen:
- Speaker says:
- Visual:
- Source / risk:
```

## HTML Deck Build Requirements

- Fixed 1920 x 1080 slide canvas.
- Whole stage scales to viewport.
- No responsive reflow inside slides.
- Use real images or generated assets only when they help the message.
- Keep CSS and JS inline unless a folder deployment is necessary.
- Include keyboard navigation.
- Verify in browser with at least one desktop and one phone viewport.

## When Not To Productize

Do not turn a deck into a public product if:

- the workflow only worked because of one private client context
- the images, examples, or case materials cannot be shared or abstracted
- the speaker's personal judgment is the entire value and cannot be generalized
- there is no repeatable intake, structure, output, or quality gate

