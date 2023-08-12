# YAML Parser Script

This script parses a YAML file containing team and member information, validates team members' email addresses, and prints the results.

## Prerequisites

- Python 3.x
- PyYAML library (install using `pip install pyyaml`)

## Usage

1. Make sure you have Python 3.x installed on your system.
2. Install the required PyYAML library using `pip install pyyaml`.
3. Place the YAML file named `project.yaml` in the same directory as this script.
4. Run the script using `python script.py`.

## Features

- Parses a YAML file and extracts team and member information.
- Validates email addresses of team members based on domain.
- Checks for empty teams and prints the results.

## Functions

### `validate_mail(member)`

- Validates the email address of team members.
- Args: `member` - Email address of a team member.
- Returns: `True` if the email address ends with 'bmw.de', `False` otherwise.

### `check_team_empty(team)`

- Checks if team members exist within the team definition.
- Args: `team` - Dictionary containing team details.
- Returns: `True` if the team members list is empty or the team name is missing, `False` otherwise.

### `main()`

- Main function to load and process YAML data for teams and members.

## Example

Assuming you have a `project.yaml` file containing team and member information, running the script will display the parsed data and validation results.

## Notes

- The script assumes that the `project.yaml` file is properly formatted.
- This script provides basic error handling for file not found situations.

## Contributors

- Mehdi Kachouri

## License

This project is licensed under the [MIT License](LICENSE).

