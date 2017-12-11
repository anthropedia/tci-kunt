git_update="git fetch origin master && git reset --hard FETCH_HEAD"

help:
	@echo "Make tasks for deployment. Checkout the makefile content."

# deploy:
# 	ssh epidaurus "cd ~/tci-fackman && " ${git_update}
# 	ssh epidaurus "cd ~/tci-compose && docker-compose restart fackman"

deploy:
	git push heroku heroku:master -f

install:
	heroku buildpacks:clear
	heroku buildpacks:add https://github.com/heroku/heroku-buildpack-apt
	heroku buildpacks:add https://github.com/heroku/heroku-buildpack-python
	heroku run cp settings.example.py settings.py
	make deploy
