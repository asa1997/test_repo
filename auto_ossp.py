import json
from bs4 import BeautifulSoup
import sys
from urllib.request import urlopen
import requests

def write_cve_data(product_name,f):
    cve_avail = input("Enter latest cve count?(y/n)")
    cvedetails = {
        "count": 0,    
        "year": 0,                                         
        "bes_cve_details_id": "",                      
        "cvedetails_product_id": "",                      
        "cvedetails_vendor_id": ""
    }
    # TODO - Sanity check on cve url.
    # try:
    #     x = urlopen('https://www.cvedetails.com/product/'+str(product_id)+'/vendor_id='+str(vendor_id))
    #     print(x)
    # except Exception as e:
    #     print("Incorrect url https://www.cvedetails.com/product/"+ product_id +"/vendor_id="+ vendor_id)
    #     sys.exit(str(e))
    if cve_avail == "y":      
        product_id = input("Enter product id : ")
        vendor_id = input("Enter vendor id : ") 
        source = requests.get("https://www.cvedetails.com/product/"+ product_id +"/vendor_id="+ vendor_id).text
        soup = BeautifulSoup(source, features="html5lib")
        table = soup.find('table', attrs={'class':'stats'})
        # print(table)
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')
        # l = len(rows)
        # print(rows[l-3])
        cols_header = rows[len(rows)-3].find('th').text
        # print(int(cols_header))
        cols_data = rows[len(rows)-3].find('td').text
        # print(int(cols_data))
        cvedetails["count"] = int(cols_data)
        cvedetails["year"] = int(cols_header)
        cvedetails["cvedetails_product_id"] = str(product_id)
        cvedetails["cvedetails_vendor_id"] = str(vendor_id)
    f.write('"cvedetails": '+ json.dumps(cvedetails, indent=4)+ ",\n")
    # print(l)
        

            
        
def check_issue_exists(id):
    try:
        x = urlopen('https://github.com/Be-Secure/BeSLighthouse/issues/'+id)
    except Exception as e:
        print("Could not find issue with id : "+id)
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
    print("Could not find "+ project_name +" under Be-Secure")
    sys.exit(str(e))
project_data = json.loads(json_data.read())
f = open("ossp_data.json", "w")
f.write("{\n")
# f.seek(0, 2)
# f.seek(-3, 2)
for i in repo_keys:
    if i == "cve_details" :
        write_cve_data(project_name, f)
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
f.write("},\n")
f.close()

    
    