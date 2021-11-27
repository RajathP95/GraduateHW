from github import Github

def get_file_contents(github_url,file_extension):
    # using an access token
    g = Github("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")
    file_content_list = []

    try:
        url = github_url.split("https://github.com/")[1]
        repo = g.get_repo(url)
        contents = repo.get_contents("")
        while contents:
            file_content = contents.pop(0)
            if file_content.type == "dir":
                contents.extend(repo.get_contents(file_content.path))
            else:
                if file_content.path.lower().endswith(file_extension):    
                    file_content_list.append(file_content)
    except: 
        print("Error: GitHub URL does not exist")

    return file_content_list