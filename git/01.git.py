# # 配置用户名、邮箱（首次使用必配）
# git config --global user.name "你的名字"
# git config --global user.email "你的邮箱"
# # 查看版本/配置
# git --version
# git config --list
# # 初始化本地仓库
# git init
# # 克隆远程仓库到本地
# git clone 仓库地址
# # 查看文件状态
# git status
# # 添加到暂存区
# git add 单个文件名
# git add .         # 所有改动文件
# # 提交到本地仓库（必填备注）
# git commit -m "提交说明"
# # 查看提交历史
# git log
# git branch                # 查看所有分支
# git branch 分支名         # 新建分支
# git switch 分支名         # 切换分支（新版Git）
# git checkout 分支名       # 切换分支（旧版）
# git branch -d 分支名      # 删除本地分支
# # 合并分支（先切到目标分支，再执行）
# git merge 待合并分支名
#
# 八、GitHub 协作流程（开源 / 团队）
# Fork：复制开源项目到自己账号
# Clone：克隆自己账号仓库到本地
# 新建功能分支 → 开发 → add → commit → push
# 提交 PR(Pull Request)，等待原作者审核合并
# 最佳实践：PR 前先 pull 同步原项目最新代码，减少冲突
# 九、规范 & 避坑要点
# 主分支（main/master）禁止直接推送，统一走 PR 合并
# 一次提交只做一件事，提交说明简洁明确
# 多人协作频繁 pull，避免大量冲突
# git reset --hard 谨慎使用，会彻底丢失本地未提交代码
# 公共分支严禁使用 rebase
#
# 所有命令总结
# git --version                    # 查看 Git 版本，验证是否安装成功
# git init                         # 将当前目录初始化为 Git 仓库（生成 .git 隐藏目录）
# git add <文件>                   # 将指定文件从工作区添加到暂存区
# git add .                        # 将当前目录所有修改过的文件添加到暂存区
# git commit -m "说明"             # 将暂存区内容提交到本地仓库，生成版本快照
# git log                          # 查看提交历史（显示 Hash、作者、时间、说明）
# git reset --hard <Hash>          # 回退到指定版本（会丢弃该版本之后的提交，谨慎使用）
# git revert <Hash>                # 撤销某次提交的修改，但生成新提交保留历史（安全，适合多人协作）
# git branch                       # 查看所有本地分支，带 * 的是当前分支
# git branch <name>                # 基于当前分支创建新分支
# git checkout <name>              # 切换到指定分支（旧命令）
# git switch <name>                # 切换到指定分支（新命令，推荐）
# git merge <branch>               # 将指定分支合并到当前分支
# git worktree                     # 同一仓库多个分支放在不同目录，并行开发互不干扰
# git stash                        # 临时保存当前工作区修改，工作区恢复干净状态
# git stash pop                    # 恢复最近一次 stash 的内容，并删除该 stash 记录
# git cherry-pick <Hash>           # 只合并某一次特定提交到当前分支，挑拣式合并
# git rebase <branch>              # 将当前分支提交"重播"到目标分支最新提交之后，历史变线性
# git fetch                        # 从远程仓库拉取最新信息，但不合并到本地分支
# git pull                         # 从远程仓库拉取并自动合并到当前分支（= fetch + merge）
# git clone <地址>                 # 从远程仓库克隆完整项目到本地
# git remote add origin <地址>     # 将本地仓库关联到远程仓库，命名为 origin
# git push -u origin main          # 首次推送本地 main 分支到远程，并建立追踪关系
# git push                         # 将本地当前分支的提交推送到远程仓库