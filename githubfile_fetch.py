from github import Github

def get_file_contents(github_URL,file_extension):
    # using an access token
    g = Github("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")
    file_contents = []

    try:
        url_repo = github_URL.split("https://github.com/")[1]
        repo = g.get_repo(url_repo)
        contents = repo.get_contents("")
        while contents:
            file_content = contents.pop(0)
            if file_content.type == "dir":
                contents.extend(repo.get_contents(file_content.path))
            else:
                if file_content.path.lower().endswith(file_extension):    
                    file_contents.append(file_content)
    except: 
        print("Error: GitHub URL does not exist")

    return file_contents