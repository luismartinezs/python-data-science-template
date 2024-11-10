# PYTHON INTENSIVE

- day 1
  - https://docs.python.org/3/tutorial/introduction.html
  - basic syntax diff js / py
  - comments, variables, data types int, float, str, bool
  - basic operations and expressions
  - project: script that takes user input and performs arithmetic operations
- day 2
  - https://docs.python.org/3/tutorial/controlflow.html
  - https://docs.python.org/3/tutorial/datastructures.html
  - control flow: if, elif, else, for, while, break, continue, pass
  - data structures: lists, tuples, sets, dictionaries
  - list comprehension
  - project: script that processes a list of numbers and outputs statistical calculations
- day 3
  - https://docs.python.org/3/tutorial/functions.htmlhttps://docs.python.org/3/tutorial/controlflow.html#defining-functions
  - https://docs.python.org/3/tutorial/modules.html
  - functions: def, call, args, return values
  - lambda functions
  - modules and packages: import standard modules, creating and using modules
  - project: module containing mathematical functions that you can import into other scripts
- day 4
  - https://docs.python.org/3/tutorial/classes.html
  - classes: def, constructor, instance methods
  - inheritance, method override
  - special methods: __init__, __str__, __repr__...
  - project: A Product class for an inventory system with methods to adjust stock levels
- day 5
  - https://docs.python.org/3/tutorial/errors.html
  - https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
  - Exception Handling: try, except, else, finally, custom exceptions
  - file i/o: open, read, write, close
  - file paths
  - project: script that logs data to a file and handles potential I/O errors
- day 6
  - https://docs.python.org/3/library/
  - https://requests.readthedocs.io/en/latest/
  - standard libs: datetime, math, random, os, sys, json
  - 3rd party: pip install
    - Use the requests library to interact with web APIs
  - project: Fetch GitHub user data and display selected information
- day 7
  - generators and yield
  - decorators
  - final project (pick one)
    - Web Scraper: Use requests and BeautifulSoup for scraping data from websites
    - Command-Line Application: Build a todo list manager or a notes app
    - Automated Script: Develop a script to automate a routine task you perform frequently
- Extra
  - Build command-line utilities using argparse for argument parsing
  - Web Development: flask
  - Data Manipulation: pandas
  - Automation Scripts: Automate file management, data entry, or interaction with web services
- Advanced topics:
  - Multithreading and multiprocessing
  - Advanced OOP concepts like metaclasses
  - Networking and sockets programming


# Project structure

- workflows: Structured sequences of tasks where multiple LLM agents and tools interact to achieve a goal, often involving complex processing and decision-making. These workflows coordinate various agents, data sources, and actions

- agents: Autonomous or semi-autonomous entities that perform specific tasks within an LLM workflow. Each agent is designed for a particular function, like summarizing text, making decisions, or calling APIs

- prompts: Concise instructions given directly to an LLM to generate a response. These are typically single requests without complex task coordination or multiple agents involved, focusing on clarity and brevity

- config.py: Configuration for the whole project

- scripts: Scripts for running workflows, agents, prompts, etc

NOTE: there are lots of files and folders just floating around that should be cleaned up