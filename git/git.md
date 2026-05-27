# Git 知识点全面总结

---

## 一、Git 本质

Git 是开源**分布式版本控制工具**，核心能力：

- 记录文件变化历史，随时回溯任意版本
- 支持多人并行协作开发
- 本地完整保存仓库历史，不依赖网络

**核心概念：**

| 概念 | 说明 |
|------|------|
| 仓库（Repo） | 被 Git 管理的文件夹，包含隐藏目录 `.git` |
| Commit（提交） | 版本快照，每次提交生成唯一哈希 ID（Hash） |
| 本地仓库 | 自己电脑上的仓库 |
| 远程仓库 | GitHub / GitLab 等托管的仓库，用于备份与协作 |
| HEAD 指针 | 指向当前分支最新提交；detached HEAD 状态容易丢提交 |

**AI 时代为什么更要学 Git：**
- 几乎所有 AI 编程工具（Claude Code、Codex 等）底层都在调用 Git
- 不用死记命令，但概念必须懂（提交、分支、合并、冲突、四分区）

---

## 二、核心模型：四分区

```
工作区(Working)  ──git add──→  暂存区(Staging)  ──git commit──→  本地仓库(Local)
                                                                      │
                                                                   git push
                                                                      ↓
                                                              远程仓库(Remote)
                                                                      │
                                                                   git pull / git fetch
                                                                      ↓
                                                              本地仓库(Local)
```

| 分区 | 说明 |
|------|------|
| **工作区** | 你看到的文件目录，实际编辑代码的地方 |
| **暂存区** | 临时存放待提交的文件（`git add`） |
| **本地仓库** | `.git` 目录，保存所有版本历史 |
| **远程仓库** | GitHub 等服务器上的仓库 |

**数据流转：**
- 向前推：`add` → `commit` → `push`
- 向后拉：`pull`（拉取+合并）或 `fetch`（只拉取不合并）

---

## 三、环境准备

```bash
# 安装 Git
# Windows：官网下载安装包
# Mac：xcode-select --install

# 验证安装
git --version

# 首次使用必配（全局配置用户名、邮箱）
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"

# 查看配置
git config --list
```

配套工具：VSCode（推荐编辑器）、GitHub 账号

---

## 四、仓库初始化

```bash
# 将当前目录初始化为 Git 仓库（生成 .git 隐藏目录）
git init

# 克隆远程仓库到本地
git clone 仓库地址
```

`.gitignore` 文件 — 配置不跟踪的文件/文件夹：
```
node_modules/
.env
*.log
__pycache__/
```

---

## 五、文件提交与状态查看

```bash
# 查看当前工作区状态（哪些文件修改/暂存/未追踪）
git status

# 添加到暂存区
git add 单个文件名        # 指定文件
git add .                # 当前目录所有修改

# 提交到本地仓库（必填备注说明）
git commit -m "提交说明"

# 查看提交历史（Hash、作者、时间、说明）
git log
```

---

## 六、版本回退（后悔药）

### 按阶段选择操作

| 阶段 | 操作 | 命令 |
|------|------|------|
| 仅工作区修改，未 add | 直接丢弃 | `git checkout -- 文件名` |
| 已 add 未 commit | 撤出暂存区 | `git reset HEAD 文件名` |
| 已 commit 未推送 | 硬回退（会丢代码） | `git reset --hard <Hash>` |
| 已推送 / 多人协作 | 安全回退（生成新提交） | `git revert <Hash>` |

```bash
# 1. 未add：撤销工作区改动
git checkout -- 文件名

# 2. 已add未commit：撤出暂存区
git reset HEAD 文件名

# 3. 已commit未推送：硬回退到指定版本（丢失该版本之后的提交，谨慎使用）
git reset --hard <Hash>

# 4. 已推送到远程/多人协作：安全回退（撤销某次提交，但生成新提交保留历史）
git revert <Hash>
```

**注意：** `git reset --hard` 谨慎使用，会彻底丢失本地未提交代码；公共分支严禁使用 `rebase`。

---

## 七、分支管理

### 基础操作

```bash
git branch                   # 查看所有本地分支，带 * 的是当前分支
git branch <name>            # 基于当前分支创建新分支
git switch <name>            # 切换到指定分支（新版 Git，推荐）
git checkout <name>          # 切换到指定分支（旧命令）
git branch -d <name>         # 删除本地分支

# 合并分支（先切换到目标分支，再执行合并）
git merge <branch>           # 将指定分支合并到当前分支
```

### 分支策略

- 主分支 `main/master` 永远可用
- 新功能走**特性分支**（feature/xxx）
- 开发完成后合并回主分支

### 合并冲突（Merge Conflict）

- **原因：** 两个分支修改了同一文件的同一行
- **解决：** VSCode 可视化工具 或 AI 辅助解决，手动编辑冲突内容后重新 `add` + `commit`

---

## 八、并行开发：git worktree

```bash
# 同一仓库多个分支放在不同目录，并行开发互不干扰
git worktree
```

---

## 九、远程仓库关联与推拉

### 两种起步方式

**方式一：先有远程 → 克隆**
```
GitHub 新建仓库 → git clone 地址 → 本地修改 → git push
```

**方式二：先有本地 → 关联远程**
```
git init → 提交 → GitHub 新建空仓库 → 关联远程 → push
```

```bash
# 将本地仓库关联到远程仓库，命名为 origin
git remote add origin 远程地址

# 首次推送（绑定上下游追踪关系）
git push -u origin 分支名

# 日常推送到远程
git push

# 拉取远程代码（拉取 + 自动合并）
git pull

# 仅拉取远程更新信息，不自动合并
git fetch
```

### fetch vs pull

| 命令 | 行为 |
|------|------|
| `git fetch` | 只拉取远程信息到本地，不合并 |
| `git pull` | 拉取 + 自动合并（= fetch + merge） |

---

## 十、进阶实用命令

```bash
# 临时储藏工作区改动（切换分支应急时使用）
git stash                   # 保存当前工作区修改，工作区恢复干净状态
git stash pop               # 恢复最近一次 stash 内容，并删除该 stash 记录

# 挑拣单个提交合并到当前分支
git cherry-pick <Hash>      # 只合并某一次特定提交，适合"挑拣"代码

# 变基（整理线性提交历史，个人分支使用）
git rebase <branch>         # 将当前分支提交"重播"到目标分支最新之后，历史变线性
```

### rebase 注意事项
- 历史呈线性，更干净
- **多人主分支慎用**，容易引发冲突
- 公共分支严禁使用

---

## 十一、GitHub 协作流程

### 内部协作（有权限）

```
管理员添加协作者 → 直接 push → 提 PR 合并到主分支
```

### 外部贡献（开源项目，无权限）— 标准五步

```
1. Fork：把项目复制到自己账号
2. Clone：克隆自己账号的仓库到本地
3. 新建分支：git branch feature/xxx
4. 修改并推送：git push 到自己仓库
5. Pull Request（PR）：向原项目提交合并请求，等待审核
```

**PR 前必须做：** 同步原项目最新代码（先 pull），否则容易冲突

### GitHub 常用功能

| 功能 | 说明 |
|------|------|
| Star | 点赞收藏 |
| Fork | 复制别人项目到自己账号 |
| Issues | 讨论问题 |
| Releases | 发布版本 |
| Codespace | 浏览器在线开发环境 |

---

## 十二、最佳实践 & 避坑要点

1. **提交规范：** 一次提交只做一件事，提交说明简洁明确
2. **分支策略：** 主分支 `main` 永远可用，功能走特性分支
3. **保护主分支：** 禁止直接 push，统一走 PR 审核
4. **频繁同步：** 多人协作经常 pull，避免大量冲突
5. **`git reset --hard` 谨慎使用：** 会彻底丢失本地未提交代码
6. **公共分支严禁 rebase：** 会改写公共历史，影响协作者

---

## 十三、AI 时代 Git 学习法

| 传统学习 | AI 时代学习 |
|----------|------------|
| 背命令、敲命令、查文档 | 理解核心概念即可 |
| 手动排错 | AI 分析错误并给出方案 |
| 死记参数 | 自然语言指挥 AI 执行 |

**重点懂：** 提交、分支、合并、冲突、四分区模型

---

## 十四、命令速查总表

```bash
# === 环境配置 ===
git --version                    # 查看 Git 版本，验证是否安装成功
git config --global user.name "你的名字"   # 配置全局用户名
git config --global user.email "你的邮箱"  # 配置全局邮箱
git config --list                # 查看所有配置

# === 仓库操作 ===
git init                         # 将当前目录初始化为 Git 仓库
git clone <地址>                 # 从远程仓库克隆完整项目到本地

# === 文件提交 ===
git status                       # 查看工作区文件状态
git add <文件>                   # 将指定文件从工作区添加到暂存区
git add .                        # 将当前目录所有修改过的文件添加到暂存区
git commit -m "说明"             # 将暂存区内容提交到本地仓库，生成版本快照
git log                          # 查看提交历史（显示 Hash、作者、时间、说明）

# === 版本回退 ===
git checkout -- <文件>           # 丢弃工作区对指定文件的修改
git reset HEAD <文件>            # 将指定文件从暂存区撤回到工作区
git reset --hard <Hash>          # 回退到指定版本（会丢失该版本之后的提交，谨慎使用）
git revert <Hash>                # 撤销某次提交的修改，但生成新提交保留历史（安全，适合多人协作）

# === 分支管理 ===
git branch                       # 查看所有本地分支，带 * 的是当前分支
git branch <name>                # 基于当前分支创建新分支
git switch <name>                # 切换到指定分支（新命令，推荐）
git checkout <name>              # 切换到指定分支（旧命令）
git branch -d <name>             # 删除本地分支
git merge <branch>               # 将指定分支合并到当前分支

# === 并行开发 ===
git worktree                     # 同一仓库多个分支放在不同目录，并行开发互不干扰

# === 进阶命令 ===
git stash                        # 临时保存当前工作区修改，工作区恢复干净状态
git stash pop                    # 恢复最近一次 stash 的内容，并删除该 stash 记录
git cherry-pick <Hash>           # 只合并某一次特定提交到当前分支，挑拣式合并
git rebase <branch>              # 将当前分支提交"重播"到目标分支最新提交之后，历史变线性

# === 远程操作 ===
git remote add origin <地址>     # 将本地仓库关联到远程仓库，命名为 origin
git push -u origin main          # 首次推送本地 main 分支到远程，并建立追踪关系
git push                         # 将本地当前分支的提交推送到远程仓库
git fetch                        # 从远程仓库拉取最新信息，但不合并到本地分支
git pull                         # 从远程仓库拉取并自动合并到当前分支（= fetch + merge）
```
