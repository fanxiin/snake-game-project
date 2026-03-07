# 🐍 芋头的贪吃蛇游戏

一个由 AI 助手芋头开发的贪吃蛇游戏，包含多个版本。

## 🎮 游戏版本

### 1. 手机版贪吃蛇 (`snake_mobile.html`)
- **特点**：专为手机优化，触摸控制
- **技术**：HTML5 + CSS3 + JavaScript
- **功能**：
  - 响应式设计，适配各种屏幕
  - 触摸控制（上下左右滑动）
  - 分数系统
  - 游戏暂停/继续
  - 重新开始

### 2. 终端版贪吃蛇 (`snake_terminal.py`)
- **特点**：在终端中运行的贪吃蛇
- **技术**：Python + curses 库
- **运行**：`python3 snake_terminal.py`

### 3. 桌面版贪吃蛇 (`snake_game.py`)
- **特点**：使用 PyGame 的桌面版本
- **技术**：Python + PyGame
- **运行**：`python3 snake_game.py`

## 🚀 快速开始

### 手机版（推荐）
1. 访问：https://[你的GitHub用户名].github.io/snake-game-project/snake_mobile.html
2. 直接在手机浏览器中打开
3. 使用手指滑动控制蛇的移动

### 本地运行
```bash
# 克隆项目
git clone https://github.com/[你的GitHub用户名]/snake-game-project.git

# 运行手机版
open snake_mobile.html  # Mac
# 或直接双击HTML文件

# 运行终端版
python3 snake_terminal.py

# 运行桌面版
python3 snake_game.py
```

## 📱 手机版控制说明
- **向上滑动**：蛇向上移动
- **向下滑动**：蛇向下移动  
- **向左滑动**：蛇向左移动
- **向右滑动**：蛇向右移动
- **点击暂停按钮**：暂停/继续游戏
- **点击重新开始**：重新开始游戏

## 🛠️ 技术栈
- **前端**：HTML5, CSS3, JavaScript (ES6+)
- **后端**：Python 3.9+
- **游戏引擎**：原生Canvas (手机版), PyGame (桌面版)
- **UI设计**：响应式设计，渐变背景，圆角元素

## 📁 文件说明
- `snake_mobile.html` - 手机版游戏主文件
- `snake_mobile.js` - 手机版游戏逻辑
- `snake_game.py` - 桌面版游戏 (PyGame)
- `snake_terminal.py` - 终端版游戏 (curses)
- `游戏说明.txt` - 游戏开发说明文档
- `simple_cost_analyzer.py` - OpenClaw成本分析工具

## 🌐 部署到 GitHub Pages
1. 在 GitHub 仓库设置中启用 GitHub Pages
2. 选择 `main` 分支的 `/ (root)` 目录
3. 访问：`https://[用户名].github.io/snake-game-project/snake_mobile.html`

## 🤝 贡献
欢迎提交 Issue 和 Pull Request 来改进游戏！

## 📄 许可证
MIT License - 详见 LICENSE 文件

## 🐱 关于作者
**芋头** - 一个正在学习开发的 AI 助手
- GitHub: [@yutou-ai](https://github.com/[你的GitHub用户名])
- 游戏开发日期：2026年3月7日

---
*Made with ❤️ by 芋头 (Yutou)*