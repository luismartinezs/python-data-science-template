# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

This project uses Python with dependencies managed via requirements.txt:

```bash
# Install dependencies
pip install -r requirements.txt

# Run specific workflows or agents
python workflows/basic-router/main.py
python agents/summarizer.py
python exercises/001-fizzbuzz.py

# For Bayesian experiments
python bayesian/coin-flip.py
python bayesian/dirichlet.py

# For reinforcement learning
python gymnasium/main.py
python marl/train.py
```

## Project Architecture

This is a Python learning and experimentation repository focused on LLM workflows, AI agents, and various computational techniques. The codebase is organized into several key areas:

### Core Structure

- **workflows/**: Structured sequences where multiple LLM agents coordinate to achieve complex goals. Examples include basic routing, conceptual blending, and story writing workflows.

- **agents/**: Autonomous entities that perform specific tasks within workflows. Each agent specializes in functions like summarization (`summarizer.py`), sentiment analysis (`sentiment_analyzer.py`), translation (`translator.py`), and routing (`router.py`).

- **prompts/**: Direct LLM instructions for single-request tasks, including SPR (Sparse Priming Representation) generators and examples.

- **config.py**: Central configuration (currently minimal - single line file)

### LLM Integration

All LLM interactions use the **ell** library with the following patterns:

- Store initialization: `ell.init(store="./logdir")`
- Complex prompts: `@ell.complex(model="gpt-4o-mini")` or `@ell.complex(model="gpt-4")`
- Structured outputs: Using Pydantic models with `response_format=ModelClass`
- Tool usage: `@ell.tool()` decorator for function calling

### Key Dependencies

The project uses several specialized libraries:
- `ell-ai`: LLM interaction framework
- `openai`: OpenAI API client
- `deap`: Evolutionary algorithms
- `gymnasium`: Reinforcement learning environments
- `networkx`: Graph algorithms
- `pulp`: Linear programming
- `scipy`, `numpy`: Scientific computing

### Specialized Areas

- **bayesian/**: Bayesian inference experiments (coin flips, Dirichlet distributions)
- **montecarlo/**: Monte Carlo simulations and tree search algorithms
- **rl-agent/**: Reinforcement learning agent implementations
- **evolutionary-strategy/**: Evolutionary computation experiments
- **course/**: Python learning materials organized by topic (basics, OOP, modules, etc.)
- **exercises/**: Practice problems from FizzBuzz to web scraping

### Template System

- **templates/agent.py**: Base agent template using ell library
- **scripts/create-agent.sh**: Agent creation script

### Development Notes

- The repository contains extensive Python learning materials in the `course/` directory
- Many experimental directories exist for different AI/ML techniques
- The codebase follows the ell library patterns for LLM interactions
- Agent architecture uses composition with routing capabilities
- Cursor rules file (`.cursorrules`) contains ell library usage examples and patterns