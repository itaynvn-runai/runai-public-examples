# follow instructions in official documentation to initiate a client:
# https://pypi.org/project/runapy/
# https://github.com/runai-professional-services/runapy

from runai.client import RunaiClient
from runai.errors import RunaiHTTPError

def get_project_info(project_id):
    project = client.projects.get(int(project_id))
    return f"project '{project['name']}' (ID: {project['id']}) in department '{project['parent']['name']}' (ID: {project['parent']['id']})"

# define list of department names to delete
department_list = ["dep1", "dep2", "dep3"]

for department in department_list:
    print(f"Starting script for department '{department}'...")

    # select department by name
    all_departments = client.departments.all()['departments']
    for x in all_departments:
        if x['name'] == department:
            my_dept = client.departments.get(int(x['id']))
            print(f"found department '{my_dept['name']}', id: {my_dept['id']}")
            break
        break

    # create a list of projects in selected department
    projects_in_department = []
    projects_counter = 0
    projects = client.projects.all()['projects']
    for project in projects:
        if project['parentId'] == my_dept['id']:
            projects_in_department.append(project)
            print(f"found {get_project_info(project['id'])}")
            projects_counter += 0
    print(f"found {projects_counter} projects.")
    
    # delete all projects from list
    for project in projects_in_department:
        if project['parentId'] == my_dept['id']:
            try:
                response = client.projects.get(project['id'])
                print(f"deleting {get_project_info(response['id'])}")
                client.projects.delete(int(response['id']))
            except RunaiHTTPError as e:
                print(f"An error occurred: {e}")
    print("project deletion complete")
    
    # delete the department
    client.departments.delete(my_dept['id'])
