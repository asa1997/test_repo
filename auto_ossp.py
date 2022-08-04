import json
import sys
from urllib.request import urlopen
import requests

# def get_and_write_cve_data(f, project_data):

def check_issue_exists(id):
    try:
        x = urlopen('https://github.com/Be-Secure/BeSLighthouse/issues/'+id)
    except Exception as e:
        sys.exit(str(e))

def write_project_repos_data(file_pointer, project_data):
    project_repos = {
        "main_github_url": "",
        "main_bes_url": "",
        "all_projects": [                                                                        
            {
                "id": 0,
                "name": "",
                "url": ""
            }
        ],
        "all_bes_repos": [                                                                  
            {
                "id": 0,
                "name": "",
                "url": ""
            }
                    
        ]
    }
    project_repos.update({"main_github_url": project_data["parent"]["html_url"]}) 
    project_repos.update({"main_bes_url": project_data["html_url"]})
    project_repos["all_projects"][0]["id"] = project_data["parent"]["id"]     
    project_repos["all_projects"][0]["name"] = project_data["parent"]["full_name"]
    project_repos["all_projects"][0]["url"] = project_data["parent"]["html_url"]
    project_repos["all_bes_repos"][0]["id"] = project_data["id"]
    project_repos["all_bes_repos"][0]["name"] = project_data["full_name"]
    project_repos["all_bes_repos"][0]["url"] = project_data["html_url"]         
    file_pointer.write('"project_repos": '+ json.dumps(project_repos, indent=4) + ","+"\n")


def write_tags(f, bes_id):
    url = 'https://api.github.com/repos/Be-Secure/BeSLighthouse/issues/'+str(bes_id)+'/labels'
    tags_json_data = urlopen(url)
    tags_dict = json.loads(tags_json_data.read())
    tags = []
    for i in range(len(tags_dict)):
        tags.append(tags_dict[i]["name"])
    f.write('"tags": ' + json.dumps(tags, indent=4) + "\n")
    


bes_id, project_name = input("Enter id and name as <id> <name>:").split()
check_issue_exists(bes_id)
repo_keys = [ "bes_id", "bes_tracking_id", "name", "full_name", "description", "watchers_count", "forks_count", "stargazers_count", "size", "open_issues", "created_at", "updated_at", "pushed_at", "git_url", "clone_url", "html_url", "homepage", "owner", "cve_details", "project_repos", "license", "language", "tags" ]
try:
    json_data = urlopen('https://api.github.com/repos/Be-Secure/'+project_name)
except Exception as e:
    print(str(e))
project_data = json.loads(json_data.read())
f = open("ossp_data.json", "w")
for i in repo_keys:
    if i == "cve_details" :
        continue
    elif i == "project_repos":
        write_project_repos_data(f, project_data)
    elif i == "tags":
        write_tags(f, bes_id)
    elif i == "owner" or i == "license":
        f.write('"' + i + '": '+ json.dumps(project_data[i], indent=4) + ","+"\n")
    elif i == "bes_id":
        f.write('"id": '+ str(bes_id) + ","+"\n")      
    elif i == "bes_tracking_id":
        f.write('"' + i + '": '+ str(bes_id) + ","+"\n")
    else:
        f.write('"' + i + '": '+ json.dumps(project_data[i]) + ","+"\n")

f.close()

    
    