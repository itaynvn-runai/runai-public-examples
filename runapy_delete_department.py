from runai.client import RunaiClient
from runai.errors import RunaiHTTPError

# set cluster / app details
realm="" # keycloak realm name
client_id="" # application id
client_secret="" # application secret
runai_base_url="" # for saas use https://<TENANT>.run.ai
cluster_id="" # ???

def get_project_info(project_id):
    project = client.projects.get(int(project_id))
    return f"project '{project['name']}' (ID: {project['id']}) in department '{project['parent']['name']}' (ID: {project['parent']['id']})"

# select department by name
departments = client.departments.all()['departments']
for department in departments:
    if department['name'] == dept_name:
        my_dept = client.departments.get(int(department['id']))
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
