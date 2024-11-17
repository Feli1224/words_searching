# 定义变量
REPO_URL = git@github.com:Feli1224/words_searching.git
BRANCH = main

.PHONY: init add commit push status

# 默认目标
all: init add commit push

# 初始化本地git仓库
init:
	@git init

# 添加远程仓库
remote:
	@git remote add origin $(REPO_URL)

# 添加文件到git暂存区
add:
	@git add .

# 提交更改
commit:
	@git commit -m "Update code"

# 推送到GitHub
push:
	@git push -u origin $(BRANCH)

# 检查git状态
status:
	@git status