#!/bin/bash

# Check if an argument is provided
if [ $# -eq 0 ]; then
    echo "Error: Please provide an agent name as an argument."
    exit 1
fi

# Get the agent name from the first argument
agent_name=$1

# Define the source and destination paths
source_file="templates/agent.py"
destination_file="agents/${agent_name}.py"

# Check if the source file exists
if [ ! -f "$source_file" ]; then
    echo "Error: Template file $source_file does not exist."
    exit 1
fi

# Check if the destination file already exists
if [ -f "$destination_file" ]; then
    echo "Warning: Agent file $destination_file already exists. Not overwriting."
    exit 0
fi

# Copy the template to the new agent file
cp "$source_file" "$destination_file"

# Check if the copy was successful
if [ $? -eq 0 ]; then
    echo "Successfully created new agent file: $destination_file"
else
    echo "Error: Failed to create new agent file."
    exit 1
fi
