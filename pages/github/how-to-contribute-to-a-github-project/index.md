title: How to contribute to a Github project
description: Simple steps to collaborate with the open source proyects
tags: Github, Git, Contribute
position: 1
date: 2016-03-10 18:20:00
content:

Here are the steps to contribute your code to existing Github project.

- Go to the repository via web.
```https://github.com/{friend_username}/{friend_project_name}```
- Click the **"Fork"** button at the top. This create a copy of the repository on your Github account.
- Clone the repository from your Github account on your local PC.
- Open a Shell / Terminal.

```
$ git clone git@github.com:{my_username}/{friend_project_name}.git

# Output example
Cloning into '{friend_project_name}'...
remote: Counting objects: 211, done.
remote: Total 211 (delta 0), reused 0 (delta 0), pack-reused 211
Receiving objects: 100% (211/211), 56.62 KiB | 0 bytes/s, done.
Resolving deltas: 100% (62/62), done.
Checking connectivity... done.
```

<!-- pagebreak -->

- Go into the new directory created.

```
$ cd {friend_project_name}
```

- Connect your local repository with the original repository.

```
$ git remote add {friend_username} git@github.com:{friend_username}/{friend_project_name}.git
```

- Now you can make changes on your local repository.
- After the changes, make a push to sync your local repo and Github repo.

```
$ git add -A
$ git commit -m "New changes"
$ git push
```

- Go to your repository on Github.
```https://github.com/{my_username}/{friend_project_name}```
- Click on the button **"New pull request"**.
- Click on the button **"Create a pull request"**.
- Complete the title and description about the changes you made.
- Click on the button **"Create pull request"**.
- Now wait your friend accept this changes.

## Notes
- Change *{my_username}* for your username, remember remove the { }.
- Change *{friend_username}* for the username of the repository to contribute, remember remove the { }.
- Change *{friend_project_name}* for the project name of the repository to contribute, remember remove the { }.

This post is based on: http://kbroman.org/github_tutorial/pages/fork.html
