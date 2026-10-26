# 第一周 AI协作与Windows项目入门

本周从零准备一个属于自己的晶圆调度学习项目。你将理解 AI 如何使用信息，在 Windows 上配置 VS Code、Conda 和 Git，从GitHub 模板建立个人作业仓库，并通过提问与小作业认识半导体制造和调度。

本周必做是环境检查、学习记录和一次真实的 commit 与 push；暂不要求编写或修改调度程序。建议安排 4—6 小时，下载、账号审核和权限等待另行记录。基础不熟时先解决当前步骤，再继续下一项。

## 怎样用这份材料

每一步都按“先自己想 → 向 AI 提问 → 继续追问 → 亲手操作 → 用证据核对”进行。引号内的问题可直接复制，但请把方括号内的信息换成自己的实际情况。讲义提供目标和检查点，AI 帮你解释具体操作；自己的回答由自己写。

### 可以反复使用的提问开头

“我第一次接触这些工具，使用 Windows 系统。请一次只指导一个小步骤，解释目的、将改变什么和如何检查。先问我现状，再给建议。如果我不理解，请换一个例子，并留一个小问题让我复述。”

### 可以反复使用的追问

“这个词是什么意思？”“我应该在哪里点击或输入？”“为什么需要这一步？”“如果跳过会怎样？”“怎样判断真的成功？”“请用我刚才的输出解释，而不是给通用结论。”

## 学习顺序和时间

1. AI 的基础概念与新会话练习。

2. 注册 GitHub 并取得模板权限。

3. 安装工具、建立空目录、获取模板、配置环境，不含下载。

4. VS Code 文件与终端练习。

5. 半导体与调度提问作业。

6. commit、push 与最终自查。

卡住 20 分钟以上时，可以向师兄寻求帮助。

### 本周使用的文件

最终作业模板位于项目根目录下的 docs/notes/W01_作业模板.docx（Word，推荐）和 docs/notes/W01_作业模板.md（Markdown，可选）。项目根目录是 README.md 与 environment.yml 所在文件夹。复制所选模板到同一目录，分别命名为 docs/notes/W01_我的作业.docx 或 docs/notes/W01_我的作业.md；只需填写并提交一种格式。附件按需放在 docs/notes/W01_附件/。无需上交整段聊天，保留关键问题、自己的理解和核验结果即可。

## 01 理解AI为什么需要上下文

### 先有一个基本认识

AI 是一类技术的统称，大语言模型是其中擅长处理语言和代码的一类。许多语言模型把文本拆成 token，用训练得到的参数，根据当前可见信息逐步生成后续 token。训练与当前对话中的推理不同；你补充一个事实，通常只是改变本次输入，并非重新训练模型。

token 是处理片段，不固定等于一个汉字或一个单词。上下文是模型这一次可使用的信息，包括指令、对话片段、已提供的文件内容和工具结果。窗口容量有限；文件在电脑里或曾经聊过，不代表它此刻一定可见。

注意力机制通过计算 token 表示之间的关联，对可见位置的信息加权组合。可把它理解为“根据当前任务利用相关线索”，但它没有人的注意力，也不保证总能找到真正重要的内容。

无关材料与重复粘贴会增加输入长度；后续轮次若继续携带这些历史，累计处理的 token 也会增加。冗长、冲突或被压缩的上下文可能使模型遗漏约束、混淆任务，表现甚至显著下降。效果取决于模型、任务和信息组织，并非越长必然越差；缓存、截断、摘要及产品计量会影响实际费用与延迟，不能按聊天字数直接计算账单。

### 向AI提问

“请用我学习晶圆调度的例子，解释训练、推理、token、上下文、上下文窗口和注意力机制。为什么把旅行闲聊、过期报错和多个不相干任务放进同一会话，可能增加 token 消耗并影响回答？请区分已知机制、教学比喻和不能保证的现象，最后问我两个理解题。”

继续追问：“长上下文是否必然更差？有用信息很长时怎么办？你现在实际能看到哪些项目内容？哪些只是你根据我描述推测的？”

### A1 自己完成

用自己的话写 5—8 句话：模型怎样生成文字；什么是 token 和上下文；注意力机制大致做什么；为什么应保留相关信息、整理长会话。举一个你会删掉的无关内容和一个必须保留的条件。

### A2 做一次新会话交接

在同一会话追问当前问题；换到不同目标，或旧会话已经混乱时，先整理“目标、当前系统环境、项目路径、相关文件、已验证结果、未解决问题”六项摘要，再开新会话提供摘要。让 AI 复述当前目标并指出还缺什么，你核对后再继续。

新会话不保证继承旧对话；某些产品可能带有记忆或自动注入项目资料。新会话通常不改变已经保存的本地文件。记录一条摘要和一次核对结果即可，不需故意制造很长的聊天。

## 02 分清AI回答和工具执行

### 向AI提问

“你给出一条命令、你调用工具执行命令、我在终端执行命令，这三件事有什么区别？请说明当前会话能用哪些工具、运行在哪里、能访问什么文件。没有实际执行时请明确标注。‘命令返回成功’与‘答案正确’还差哪些核验？”

继续追问：“如果你说安装好了，我应该看什么证据？如果你读不到我的磁盘，我需要提供什么？执行结果和预期不一样时，我怎样继续问？”

### 在 B2 环境检查中核验一次真实操作

在后面的 B2 环境检查中，选一个实际命令记录“谁执行、在哪个目录、命令、返回输出、自己的判断”。这份证据写入作业模板的 B2 即可。AI 只有网页聊天能力时，由你在 VS Code 终端执行，再把必要输出发给它；具备工具时，也要区分 AI 的运行环境和你的 Windows 电脑。

AI 的解释可能出错。查文件、看输出和对照小例子，比“AI 说成功了”更可靠。安装、修改文件或推送前，先知道影响哪些对象；账号密码、验证码和访问令牌由自己在官方界面输入，不发到聊天里。

## 03 注册GitHub并取得模板

### 向AI提问

“我还没有 GitHub 账号。Git 和 GitHub 分别解决什么问题？请依据官方注册页指导我注册并验证邮箱。什么是仓库、本地副本和远程地址？请在我完成每一步后再继续。”

操作入口：https://github.com/signup 。注册并验证邮箱后，把 GitHub 用户名发送给师兄，接受师兄对私有模板的访问邀请。

模板：https://github.com/HawkW1027/wafer-scheduling-learning 。登录后确认能看到 README.md 与 environment.yml。若显示 404，先检查登录账号、邀请是否接受和地址。

### 从模板建立个人作业仓库

在模板页面选择 Use this template → Create a new repository。Owner 选择自己的账号，名称建议 wafer-scheduling-homework，可见性选 Public，仅使用默认分支即可。创建后检查网页地址中的账号是你自己，并在仓库 Settings → Collaborators 中邀请账号 HawkW1027。

这是先从项目生成个人模板副本，再将自己的副本克隆到电脑。仓库用于发布模板，学生的作业提交到个人仓库。

### 继续追问并核对

“Use this template、Fork、Download ZIP 和 clone 有什么区别？为什么本周先生成自己的仓库？请根据我实际网页上的账号与仓库名，帮我判断接下来应该复制哪个 HTTPS 地址。”

没有模板按钮或没有权限时，记录页面状态请我处理。可临时用包内模板学习，但账号、clone 和 push 仍属于待补项，不能把临时方案记成全部完成。

## 04 安装VS Code Git和Conda

### 先问清楚三种工具的分工

“我使用Windows操作系统，请解释 VS Code、Git、Conda、Python 各负责什么，它们如何配合。先帮我检查已有安装，再按缺项安装。请只给 Windows 对应步骤和官方链接。”

### VS Code

官方入口：https://code.visualstudio.com/docs/setup/windows 。选择与系统架构匹配的 Windows 安装包，通常使用 User Installer。安装后打开 VS Code；已有可用版本可直接沿用。界面不熟时让 AI 逐个解释菜单。

### Git for Windows

官方入口：https://git-scm.com/install/windows 。安装与系统架构匹配的版本；请 AI 解释安装选项中 Git 的命令行可用范围与凭据管理，确认普通终端可以使用 Git。安装完成后关闭并重开 VS Code，稍后在终端检查 git --version。

### Conda

已有可用 Miniforge、Miniconda 或 Anaconda 时先核对，不重复安装。本课程新安装优先使用 Miniforge：https://github.com/conda-forge/miniforge 。Windows x64 使用官方列出的 Miniforge3-Windows-x86_64.exe。如果系统是ARM64 （可以在codex中请AI帮忙查看），请先向 AI 核对官方支持情况，不要照搬 x64 步骤。

安装时记下真实路径，选择本人账户可写、尽量无空格和特殊字符的目录，保留开始菜单快捷方式；沿用不将 Miniforge 加入全局 PATH 的默认选项。安装后从开始菜单打开 Miniforge Prompt，运行 conda --version。已有其他发行版则用其 Anaconda Prompt。

### 让VS Code的PowerShell认识Conda

向 AI 提问：“Miniforge Prompt 里能找到 conda，但 PowerShell 中找不到，是为什么？conda init powershell 会改动哪里？请先解释，再指导我初始化并重开终端验证。”

理解后在 Miniforge Prompt 中运行 conda init powershell，再关闭并重开 VS Code 和 PowerShell 终端。若出现脚本执行策略报错，保留完整报错请 AI 判断是否为组织策略；不要盲目放宽全局策略。也可在完成项目目录创建后，完全退出所有 VS Code 窗口，从 Miniforge Prompt 进入项目并运行 code .；在新开的 VS Code 中新建 Command Prompt 终端并验证 conda。若 code 不可用，先请 AI 检查 VS Code 的命令行配置；CMD 使用自己的命令语法。

### 需要自己留下的证据

记录 Windows 版本与架构、VS Code 版本、Git 版本、Conda 发行版与版本，以及实际使用的 Shell。继续追问：“安装 Conda 是否等于创建好了本项目的 Python 环境？代码文件夹与环境安装目录是同一个东西吗？”

## 05 亲手创建空项目文件夹并获取模板

### 先用Windows文件资源管理器创建

打开文件资源管理器，进入自己的用户目录，在其中新建 Projects 文件夹；再在 Projects 内新建 wafer-scheduling-homework 文件夹。示例路径是 C:\Users\你的Windows用户名\Projects\wafer-scheduling-homework，用户名必须换成真实值。大家可以放在自己想放的位置，推荐所有项目放在一个文件夹下，以文件夹区分不同项目。

此时打开 wafer-scheduling-homework，应看到它是空的。下一步要把模板克隆进这个空目录。

### 以文件夹为项目打开VS Code

启动 VS Code，选择 File → Open Folder（文件 → 打开文件夹），选刚才的 wafer-scheduling-homework，点击选择文件夹。检查左侧文件树根目录是它，而不是 Projects、下载目录或整个课程资料目录。工作区信任提示出现时，确认信任即可。

选择 Terminal → New Terminal（终端 → 新建终端）。本教程默认 PowerShell；终端标签应显示 PowerShell。Ctrl+` 可显示或隐藏终端，Ctrl+Shift+P 打开命令面板。

### 向AI提问后再克隆

“我已在 VS Code 打开空目录[真实路径]，终端是 PowerShell，个人模板副本的 HTTPS 地址是[从 GitHub 的 Code → HTTPS 复制]。请先指导我验证当前目录确实为空，再把这个仓库 clone 到当前目录。解释命令末尾的点号和不写点号的区别，一次只给一条命令。不要让我对已克隆的仓库再次 git init。”

可先运行以下两条只读检查命令，自己核对路径和内容：

```powershell

Get-Location

Get-ChildItem -Force

```

AI 给出的 clone 命令应使用你的个人仓库地址，并把目标设为当前空目录“.”。不要把示例用户名、尖括号或聊天提示符一并复制。认证时按官方登录提示操作；若命令失败，先读报错再决定下一步。

### B1 获取成功的检查点

文件树中出现 README.md、environment.yml、docs 和 scripts；README.md 直接位于项目根目录，没有多套一层同名文件夹。运行 git status 能识别仓库，git remote -v 的 origin 指向自己的仓库。追问 AI：“这里的首次获取为什么用 clone，不是 git pull？远程账号错了会造成什么问题？”

## 06 配置项目环境并认识VS Code

### B2 向AI提问并分步配置

“请读项目根目录的 environment.yml，解释环境名、Python 版本和渠道。指导我检查已有环境；不存在时再创建 wafer-scheduling，存在时核对后激活。然后在 VS Code 安装 Microsoft 的 Python 扩展并选择相同解释器。请解释每条命令，让我操作并反馈输出。”

创建与激活命令由 AI 根据文件和现状逐条指导。创建成功后，在 Extensions（扩展，Ctrl+Shift+X）搜索 Python，核对发布者为 Microsoft；中文界面扩展可选，AI 使用现有可用入口即可，不要求购买新服务。

用 Ctrl+Shift+P 搜索 Python: Select Interpreter，选择 wafer-scheduling。重新新建终端、核对环境并在项目根目录运行检查脚本；以下是可用于核验的命令：

```powershell

conda env list

python --version

python -c "import sys; print(sys.executable)"

python scripts/check_env.py

```

environment.yml 要求 Python 3.11。检查实际解释器路径属于 wafer-scheduling，工作目录为自己的项目根目录；base 的版本不代表项目环境的版本。再用 VS Code 的 Run Python File in Terminal 运行 scripts/check_env.py，比较路径与版本。这个脚本只报告现状，是否选对仍需你判断。

### B3 做一次文件操作

在 VS Code 文件树中展开 docs → notes，找到 W01_作业模板.docx。右键文件并选择在文件资源管理器中显示，复制为 W01_我的作业.docx，再用 Word 或 WPS 打开，填写姓名和自己的学习目标，保存到原来的 docs/notes/ 目录。关闭后重新打开，确认内容仍在；可使用 Word 或 WPS 的打印预览查看版面。不要求本周会渲染 Markdown；选用 .md 时再向 AI 学习 Ctrl+Shift+V 预览。

### 用实际界面解释这些词

向 AI 提问：“请结合我打开的项目说明：文件树、编辑区、终端、工作区、扩展和 Python 解释器各是什么？打开一个文件与打开项目文件夹有什么区别？选择解释器与激活终端环境是否总会同步？”

自己在记录中分别写一句话，并指出对应位置。本项目先用单文件夹工作区；VS Code 也支持多个文件夹组成工作区。扩展为编辑器增加能力，Python 扩展本身不等于 Python 解释器，Conda 环境也不等于项目文件夹。

若出现 >>>，你正在 Python 交互模式中，先输入 exit() 回到 Shell 再运行命令。若改用 CMD，当前目录用 cd、列目录用 dir，不直接照抄 PowerShell 的 Get-Location。每次遇到报错，提供 Shell、目录、原命令、必要完整报错和已尝试步骤。

## 07 通过提问认识半导体制造和调度

以下三个问题按“先写猜想、再问 AI、追问、对照讲义、自己作答”完成。每题保留一处你确认或修正的理解。

### C1 一批晶圆是什么

先问 AI：“请用一个虚构的半导体工厂例子，带我区分 Wafer、Die、Lot、Product、Carrier。”

追问：“同一个 Lot 换了载具，哪些身份和记录需要保留？一片晶圆和一个晶粒是否是同一个对象？载具是否定义产品类型？”

作业：画一张包含这五个对象的关系图；简单说明换载具后哪些信息要保持关联；回答：在半导体加工中，被实际送入机器的是以上中的哪一个？最小被加工单元又是什么？核对《半导体晶圆制造基础知识》1.1、1.2。

### C2 一批晶圆经历哪些加工

先问 AI：“请用不涉及化学推导的语言解释沉积、光刻、刻蚀、清洗和 CMP 各改变什么，再向我提问检查理解。哪些比喻可能误导？”

追问：“同类工艺为何会在路线中反复出现？两次光刻是否一定是同一步？”

作业：描述上述五种工艺的作用；用一个材料层的例子解释为什么会出现重复加工。核对晶圆讲义2.1。

### C3 为什么需要调度

只有设备 M1，时刻 0 可用；Lot A 和 Lot B 都已就绪且有资格加工。A 需连续加工 4 分钟，B 需 1 分钟；加工不能中断，不考虑准备与运输时间。

自己画出 A→B 和 B→A 两种时间安排，写出每个 Lot 的开始、完工和等待时间。比较“让全部任务尽快结束”与“让平均等待更短”时，你会如何评价两种安排。再追问 AI：“如果关心交期，我还缺哪些信息？为什么仅凭加工时间不能断言某个顺序在所有目标下最好？”

写出这个例子的输入、决策、两条约束和一个评价目标。核对《生产调度基础知识》1.1、1.3。

## 08 向AI学习commit和push并完成提交

### 把真实状态提供给AI

“我用 Windows，在自己的作业仓库[真实路径]完成了 docs/notes/W01_我的作业.docx 和附件（选 Markdown 时把路径改为 .md）。请先指导我查看当前分支、远程地址与改动，再解释保存、暂存、commit、push 分别发生了什么。请一步一步带我把自己的答案 commit 并 push 到个人仓库。每步先让我预测它会改变本地还是远程，再给一条命令和检查方法；不要直接代写或替我盲目提交所有文件。”

请 AI 根据实际文件、分支和远程配置指导操作。首次提交需要 Git 姓名和邮箱时，让 AI 解释配置范围，使用自己愿意用于提交记录的署名与邮箱。这里是已克隆仓库，不需要再次初始化。

### 在三个节点继续追问

提交前：“哪些文件应该进本次提交？我保存了文件，为什么网页还没变？git status、git diff 和暂存差异分别能看到什么？新文件为什么可能不出现在普通 git diff 中？”

提交后：“commit 已成功但还没 push，另一个人能从 GitHub 看到修改吗？提交编号表示什么？请让我用自己的话解释。”

推送后：“怎样确认这次提交真的到了正确的仓库和分支？Everything up-to-date 是否说明我没保存的修改也上传了？推送失败时应该先检查认证、权限、分支还是远程地址？”

### B4 必须由自己完成的检查

检查待提交文件：Markdown 可查看文字差异；Word 的正文通常不会在 git diff 中逐行显示，应先用 Word 或 WPS 打开检查，保存并关闭后再提交。只选自己的作业与附件，保留模板代码。完成 commit 后再 push，在浏览器打开自己的仓库和实际分支，核对作业文件与提交编号。Word 若不能在线预览，下载本次提交中的文件并打开核对答案；确认师兄可以访问。

若认证或网络失败，保留真实状态与报错，不用“已上传”代替未完成的步骤。避免为通过推送而强制覆盖远程。请 AI 解释原因，也可以向我提问。

### 最终交什么

提交个人仓库链接、分支、包含作业的完整 commit 编号，以及作业文件相对路径：docs/notes/W01_我的作业.docx（推荐），或 docs/notes/W01_我的作业.md。把这些信息和推送、网页核对结果发到提交入口或消息中，不必写回被该提交包含的作业文件。

作业包含 A1—A2 的 AI 学习记录、B1—B4 的目录与工具记录、C1—C3 的场景回答，以及一个仍不确定的问题。真实操作核验证据合并记录在 B2。环境目录、凭据和整段聊天不属于作业内容。

### 口头自查

我能找到项目目录和终端；解释实际 Python 来自哪里；说明新会话需要什么信息；区分 AI 文字与工具证据；说明个人仓库与模板的关系；解释一次 commit 和 push；用自己的例子说清 Lot、工艺与调度。

## 查阅来源

操作流程以实际软件界面和官方文档为准。以下内容核对于 2026年10月25日，安装和账号页面未来可能调整；遇到差异先记录页面信息再询问 AI。

1. VS Code Windows 安装：https://code.visualstudio.com/docs/setup/windows

2. VS Code 终端：https://code.visualstudio.com/docs/terminal/getting-started

3. Conda Windows 安装：https://docs.conda.io/projects/conda/en/stable/user-guide/install/windows.html

4. Miniforge Windows 安装与支持范围：https://github.com/conda-forge/miniforge

5. Git Windows 安装：https://git-scm.com/install/windows

6. GitHub 注册：https://docs.github.com/en/account-and-profile/how-tos/account-management/creating-an-account-on-github

7. GitHub 从模板创建仓库：https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template

8. Git 记录修改：https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository

9. Git 远程仓库：https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes

10. 本项目《半导体晶圆制造基础知识》1.1、1.2、2.1与《生产调度基础知识》1.1、1.3。两份讲义随课程资料发放。
