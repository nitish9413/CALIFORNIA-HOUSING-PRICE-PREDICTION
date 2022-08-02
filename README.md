# Machine_Learning_Project

### Software and Account Requirements.
1. Github Account
2. Heroku Account
3. VS code IDE
4. GIT CLI
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)

### Create a conda environment
```
conda create -p venv python==3.7 -y
```

```
conda activate venv/
```

```
pip install -r requirements.txt
```

To Add files to git
```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status
```
git status
```

To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version chnages to github
```
git push origin main
```

To check remote url
```
git remote -v
```

To setup CI/CD pipeline in heroku we need 5 information

1. HEROKU_EMAIL= <>
2. HEROKU_API_KEY= <>
3. HEROKU_APP_NAME = mlproject1st-reg


BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase

To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 <img id>
```

To check running container in docker
```
docker ps
```

To stop dokcker container
```
docker stop <container_id>
```

