🚀 项目简介
这是一个基于全栈技术开发的个人效率与数据分析仪表盘。旨在帮助用户记录日常生活中的各项活动，如待办事项、学习心得、日常杂记、饮食和睡眠情况，并通过数据分析提供个性化的洞察，助力个人成长和自我管理。
✨ 主要功能
本项目将逐步实现以下核心功能：
 * 多维度记录系统:
   * 待办事项 (To-Do List): 记录日常任务，支持标记完成。
   * 已完成事项 (Done List): 汇总已完成的任务，方便回顾。
   * 学习心得: 记录每日所学所思，支持富文本或 Markdown 格式。
   * 日常杂记: 随手记录灵感和想法。
   * 饮食记录: 记录每日饮食内容、时间和大概份量。
   * 睡眠记录: 记录入睡时间、醒来时间及睡眠时长。
 * 桌面插件模式 (计划):
   * 可作为桌面应用运行，开机自启动，无需联网即可使用。
 * 智能数据分析与可视化:
   * 任务类别比例分析: 自动统计不同类别任务（如工作、学习、生活）所占的比例，并以图表形式展示。
   * 趋势分析: 展示各项记录（如睡眠时长、任务完成量）随时间变化的趋势。
   * 初步原因分析 (逐步实现):
     * 关联分析情绪、健康状态、计划安排、突发事件等因素与任务完成情况、效率、生活习惯之间的联系。
     * 通过数据可视化，尝试揭示潜在的相互影响。
   * 自动生成数据总结: 根据记录数据自动生成当日和本周的量化总结报告。
🛠️ 技术栈
本项目采用以下主流技术栈进行开发：
 * 前端:
   * Vue.js: 渐进式 JavaScript 框架，用于构建用户界面。
   * Axios: 基于 Promise 的 HTTP 客户端，用于前后端通信。
   * ECharts / Chart.js (待定): 强大的 JavaScript 图表库，用于数据可视化。
 * 后端:
   * Python: 主要编程语言，用于后端逻辑处理和数据分析。
   * Flask: 轻量级 Python Web 框架，用于构建 RESTful API。
   * Pandas: Python 数据分析库，用于数据处理和统计。
   * Matplotlib / Seaborn: Python 数据可视化库，用于在后端生成复杂图表（或提供数据给前端图表库）。
 * 数据库:
   * MySQL: 关系型数据库，用于持久化存储所有用户数据。
 * 桌面打包 (未来计划):
   * Electron: 使用 Web 技术构建跨平台桌面应用。
⚙️ 快速开始
1. 后端设置
 * 克隆仓库:
   git clone https://github.com/YourGitHubUsername/personal-dashboard.git
cd personal-dashboard/personal-dashboard-backend

 * 创建并激活虚拟环境:
   python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

 * 安装依赖:
   pip install Flask PyMySQL Flask-CORS pandas matplotlib seaborn # 后续可能添加更多库

 * MySQL 数据库配置:
   * 确保已安装并运行 MySQL Server。
   * 登录 MySQL，创建一个新数据库（例如 personal_dashboard）和一个新用户，并授予该用户对数据库的权限。
   * 执行以下 SQL 语句创建 todos 表：
     CREATE DATABASE IF NOT EXISTS personal_dashboard;
USE personal_dashboard;
CREATE TABLE IF NOT EXISTS todos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task VARCHAR(255) NOT NULL,
    is_completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

   * 在 app.py 中更新数据库连接信息（DB_CONFIG）。
 * 运行后端:
   python app.py
# 或者
flask run

   后端服务默认运行在 http://127.0.0.1:5000。
2. 前端设置
 * 进入前端目录:
   cd ../personal-dashboard-frontend # 假设你在 backend 目录，回到项目根目录再进入 frontend

 * 安装依赖:
   npm install
# 或者
yarn install

 * 运行前端:
   npm run serve
# 或者
yarn serve

   前端应用默认运行在 http://localhost:8080。
现在，你可以在浏览器中访问前端地址，并开始测试添加和获取待办事项的功能了！
🛣️ 项目进度
 * 后端基础 API (CRUD - Create & Read for TodoList): ✅ 已完成
 * 前端与后端连接及数据显示: ✅ 已完成
 * 后端 TodoList API (Update & Delete): ⏳ 进行中
 * 其他记录类型 (饮食、睡眠等) 的数据库设计与 API: ⏳ 进行中
 * 前端多模块界面开发: ⏳ 进行中
 * 数据统计与基础可视化: ⚪ 待开始
 * 原因分析与高级可视化: ⚪ 待开始
 * 桌面应用打包 (Electron): ⚪ 待开始
🤝 贡献
本项目为个人开发项目。如果你有任何建议或发现 Bug，欢迎提出 Issue。
📄 许可证
本项目使用 MIT 许可证。详见 LICENSE 文件。
