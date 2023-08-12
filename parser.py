"""
This script parses a YAML file containing team and member information,
validates team members' email addresses, and prints the results.
"""
import yaml
def validate_mail(member):
    """
    Function to validate mail of team members
    """
    return member.endswith("bmw.de")
def check_team_empty(team):
    """
    Function to check if team members exist within team definition
    """
    return team['members']==[]
def main():
    """
    Main function to load and process YAML data
    """
    #Basic error handling
    try :
        with open ("project.yaml",encoding="utf-8") as project:
            data=yaml.safe_load(project)
        print(" "*80+f"The Project name is : {data['name']}")
        print("*"*50)
        for teams in data['teams']:
            if not check_team_empty(teams):
                print(f"[*] The Team name is : {teams['name']}")
                for member_id,member in enumerate(teams['members'],start=1) :
                    if  validate_mail(member['mail']) :
                        print(f"Team member number {member_id} mail  : {member['mail']}")
                        print(f"Team member role : {member['role']}")
                        print("-"*30)
                    else :
                        print(f"Team member mail is not valid : {member['mail']}")
                print("="*50)
    except FileNotFoundError:
        print("Wrong file or file path")
if __name__=='__main__':
    main()
    