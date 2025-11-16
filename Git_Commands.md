GIT

•	Download and install git.
•	After installation, open your working folder. Right click – Select git Bash here, then CMD open

Basic commands
•	Touch (filename.txt) – to create a file in any type current directory
•	Rm –rf (filename.txt) – to Remove the file in current directory
•	Mkdir (Folder name) – to create a directory
•	Rmdir (Folder name) - to remove a directory
•	Cd (Folder name) – move one folder to another
•	Ls – List all files In current folder
•	Clear – clear the screen
•	Nano (filename.txt) -  create file and input text or anything
•	Cat (filename.txt) -  to see the what content in that file




Git commands

WORKING DIRECTORY
	•	Git - -version -> to check the current version of git.
	•	Git init -> To install Git in the working Directory (Local folder) if not exist. its is helps to track everything in that particular folder, any changes, etc.
	
	•	Git config --global user.name “username” -> Add/Change username in global.
	•	Git config --global user.name -> To Check Global Username. 	
	
	•	Git config user.name “username” -> Add/Change username.
	•	Git config user.name -> To Check Local Username. 	
	
	•	Git config --global user.email “test@gmail.com” -> Add/Change user email in global
	•	Git config --global user.email -> To Check Global Email. 
	
	•	Git config user.email “test@gmail.com” -> Add/Change user name
	•	Git config user.email -> To Check Local Email.
	
	•	Git config --global alias.(What name do you want) (Which command do you want a shortcut) -> alias use to change the command to a simple way, Ex: Git config - - global alias.st status – now status call as st
	•	Git config --global core.editor “code --wait” -> only for visual studio
	•	Git config --global –e -> open the visual code editor
              


STAGING AREA
	•	Git status -> It is used to display the Files & folders status. It shows the tracked details. Once a file is added to the staging area, it tracks all the file changes. If a file is added to staging it show the status in green if file is not added it show in red color to git add
	•	Git branch -> it shows list of branches
	
	•	Git add (filename.txt)-> This is use to add the created file to staging process. If file is added + symbol shows on file icon
	•	Git add . -> Its add the all the file in current folder
	•	Git add *. -> If you want to add many file in particular format do like this Ex: git add *.js

	•	Git restore --staged (path/file.txt) -> Restore the particular file in staging area

	•	Git rm –cached (filename.txt) -> you want to remove file in staging using this comment to remove that file. If file is removed + symbol not shows on file icon

	•	Git diff -> it shows the what changes made in file working directory and repository,  added(+(text or filename.txt)) or deleted(-(text or filename.txt))
	•	Git diff –cached ->its show the what changes made in file staging area and last commited repository

    COMMIT & HISTORY
	
	•	Git commit (filename.txt) –m ‘ give some message what use made changes in the file’ -> it commits the file added and modified file staging to git local repository. If file is commit tick symbol shows on file icon
	•	Git commit –a –m ‘some messages’ -> second time commit the file using this message and -a means add you no need to git add it do automatically
	•	Git commit --amend -> This commit merged last commit like If you forget to commit one file to last commit this command use to commit with last commit 
	
	•	Git log -> Its use to Show all the staging changes history 
	•	Git log - - oneline -> Its use to Show all staging history changes in single line
	•	Git log - - oneline (filename.txt)-> Its use to Show particular file staging history changes in single line
	•	Git log (commit id start) (commit id end) -> It use to show the history in between these commit id
	•	Git log - -stat -> it show the all commit history and detail about affected or changes file 
	•	git tag –a (version id) –m ‘(message)’ ->Its just tag the commit to version using every update or bug fixing or changes Ex: Git tag –a v1.0.0 –m ‘fixing bugs, stable’
	•	git tag -> It show the current version
	Q – Quit

	•	Git checkout . ->  get back to last commit
	•	Git checkout . (a2d941dbb97f5552066c49b7a507f4c1eb4593c2) -> get back to particular commit and you can see the file content (this code you will get in git log)
	•	Git checkout (master or that branch name) -> come  back original content
	•	Git reset HEAD - -hard -> it undo all the content permanently back to one step or last staging area and code also change back to working directory
	•	Git reset - -hard (a2d941dbb97f5552066c49b7a507f4c1eb4593c2) -> it undo all the content permanently back to this particular commit  and code also change back to working directory
	•	Git reset HEAD~1 -> It delete history and come to last commit from committed history. 1 mean last commit you can delete how many commit you want to delete
	•	Git revert (commit id) -> It not delete in history and come to last commit
	•	Git clean –fd -> it remove the file and directory reset the staging unwanted file and directory still in working directory  (f mean file, d mean directory you can use like only –f or –d )

	•	Touch .gitignore - > Create this file is used to ignore to commit particular files. Add the which file you want to not commit  (filename.txt) in that .gitignore file  

	
	•	Git branch -> it shows list of branches
	•	Git branch (branch name) -> add new branches
	•	Git checkout (branch name) -> Switch to branch
	•	Git checkout –g (or) -b (branch name) -> add new branch and Switch to branch 
	•	Git branch –d (branch name) -> delete the branch You can see all the master branch file in any branch but if you in master branch you can’t see the other branch file.
	•	Git merge (branch name) -> this command used to merge the branch (ex: you in master branch use git merge (branch name) which branch you want to merge with master branch that name you will give)

	•	Git remote add orgin (git hub link) -> this command use to connect the git to git hub (first create account in git hub then create new project then push it)
	•	git push –u origin master -> to push the code to git hub or do you want push any other branch first move to that branch in git then git push –u origin (branch name)
	•	git clone (git hub link) -> is use to download the project in github to our system
	•	git pull -> once you clone the project then any changes made in your github project this command update the new code.
	•	Git - - bare init -> if initialized in folder only you can push and pull only it stores data git status,git log not for in bare git
	•	Git push ~/Desktop/git/home master(this is path of folder)- > push the code one folder to another 
	•	Git pull ~/Desktop/git/home master(this is path of folder)- > pull the code one folder to another 





