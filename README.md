# WorkflowLearner

## 项目概述


本项目旨在通过使用PSR.exe录制的MHT文件，让大语言模型（LLM）学习工作流。PSR.exe是Windows操作系统中的问题步骤记录器，可以记录用户操作并生成MHT文件。通过解析这些MHT文件，LLM可以学习和理解用户的工作流程。

To teach LLM Agents how to work with PSR.exe's MHT files, this project aims to use MHT files recorded by PSR.exe to enable large language models (LLMs) to learn workflows. PSR.exe is the Problem Steps Recorder in the Windows operating system, which can record user operations and generate MHT files. By parsing these MHT files, LLMs can learn and understand user workflows.

## 功能

- 使用PSR.exe录制用户操作并生成MHT文件。
- 解析MHT文件并提取工作流信息。
- 使用LLM学习和理解工作流。

## 安装

### 前提条件

- Windows操作系统
- Python 3.x
- PSR.exe（问题步骤记录器，Windows自带）

### 安装步骤

1. 克隆仓库：
    ```bash
    git clone https://github.com/yourusername/llm-workflow-learning.git
    cd llm-workflow-learning
    ```

2. 安装依赖：
    ```bash
    pip install -r requirements.txt
    ```

## 使用方法

1. 使用PSR.exe录制用户操作：
    - 打开PSR.exe（问题步骤记录器），可通过Win7/Win8/Win10的搜索栏搜索找到。
    - 点击“开始记录”按钮，然后开始你的工作。PSR.exe会自动记录鼠标动作（如点击、拖动、滚动等）以及键盘动作（仅是动作，不会记录键入的内容）。
    - 完成操作后，点击“停止记录”按钮。软件会自动弹出保存窗口。
    - 结果会以一个Zip压缩包存在，压缩包内是MHT格式的网页，内含分步步骤以及屏幕截图。

2. 解析MHT文件：
    ```bash
    python parse_mht.py path/to/your/file.mht
    ```

3. 使用LLM学习工作流：
    ```bash
    python learn_workflow.py path/to/parsed/data.json
    ```

## 文件结构

```
llm-workflow-learning/
│
├── parse_mht.py          # 解析MHT文件的脚本
├── learn_workflow.py     # 使用LLM学习工作流的脚本
├── requirements.txt      # 项目依赖
├── README.md             # 项目说明文档
└── data/                 # 存放解析后的数据文件
```

## 贡献

欢迎贡献！请提交Issue或Pull Request。

## 许可证

本项目采用MIT许可证，详见[LICENSE](LICENSE)文件。

## 联系方式

如果您有任何问题或需要进一步的信息，请联系项目维护者：[u3588064@connect.hku.hk](mailto:u3588064@connect.hku.hk)。

![qrcode_for_gh_643efb7db5bc_344(1)](https://github.com/u3588064/LLMemory/assets/53069671/8bb26c0f-4cab-438b-9f8c-16b1c26b3587)

