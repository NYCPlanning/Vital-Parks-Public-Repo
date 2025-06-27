#!/bin/bash
#
# Script to compile python packages from a requirements.in file to a requirements.txt file
#
set -e
PATH_TO_REQUIREMENTS="setup"
RELATIVE_SCRIPTPATH="$(dirname -- "${BASH_SOURCE[0]}")"
SCRIPT_NAME=$(basename "$0")
OUTPUT_FILE="requirements.txt"

# Update and install packages used to compile requirements
echo -e "🛠 upgrading python package management tools"
python -m pip install --upgrade pip
python -m pip install --upgrade pip-tools wheel

# Delete existing requirements file to ensure full dependency resolution
echo -e "🛠 deleting ${PATH_TO_REQUIREMENTS}/requirements.txt"
rm -f ${PATH_TO_REQUIREMENTS}/requirements.txt

# Compile requirements
echo -e "🛠 compiling from ${PATH_TO_REQUIREMENTS}/requirements.in"
CUSTOM_COMPILE_COMMAND="${RELATIVE_SCRIPTPATH}/${SCRIPT_NAME} ${PATH_TO_REQUIREMENTS}" python -m piptools compile --output-file=${PATH_TO_REQUIREMENTS}/${OUTPUT_FILE} ${PATH_TO_REQUIREMENTS}/requirements.in
echo -e "✅ done compiling ${path_to_requirements}/${OUTPUT_FILE}"
