# 工作流录制通 WorkflowLearner 

## 项目概述 Summary

本项目旨在通过使用PSR.exe录制的MHT文件，让大语言模型（LLM）学习工作流。PSR.exe是Windows操作系统中的问题步骤记录器，可以记录用户操作并生成MHT文件。通过解析这些MHT文件，LLM可以学习和理解用户的工作流程。

To teach LLM Agents how to work with PSR.exe's MHT files, this project aims to use MHT files recorded by PSR.exe to enable large language models (LLMs) to learn workflows. PSR.exe is the Problem Steps Recorder in the Windows operating system, which can record user operations and generate MHT files. By parsing these MHT files, LLMs can learn and understand user workflows.

## 功能 Functions

- 使用PSR.exe录制用户操作并生成MHT文件。
- 解析MHT文件并提取工作流信息。
- 使用LLM学习和理解工作流。

- Record user operations using PSR.exe and generate MHT files.
- Parse MHT files and extract workflow information.
- Use LLMs to learn and understand workflows.

## 安装 installment

### 前提条件 Requirements

- Windows操作系统 Windows operating system
- Python 3.x
- PSR.exe（问题步骤记录器，Windows自带;Problem Steps Recorder, included with Windows）

### 安装步骤 Install Steps

克隆仓库/Clone the repository:

```bash
git clone https://github.com/u3588064/WorkflowLearner
cd llm-workflow-learning
```

安装依赖/Install dependencies:

```bash
pip install -r requirements.txt
```

## 使用方法 Methods

### 使用PSR.exe录制用户操作 Recording actions with PSR.exe

1. 打开PSR.exe（问题步骤记录器），可通过Win7/Win8/Win10的搜索栏搜索找到。
2. 点击“开始记录”按钮，然后开始你的工作。PSR.exe会自动记录鼠标动作（如点击、拖动、滚动等）以及键盘动作（仅是动作，不会记录键入的内容）。
3. 完成操作后，点击“停止记录”按钮。软件会自动弹出保存窗口。
4. 结果会以一个Zip压缩包存在，压缩包内是MHT格式的网页，内含分步步骤以及屏幕截图。

1. Open PSR.exe (Problem Steps Recorder), which can be found via the search bar in Win7/Win8/Win10.
2. Click the "Start Record" button and begin your work. PSR.exe will automatically record mouse actions (such as clicks, drags, scrolls) and keyboard actions (only actions, not the content typed).
3. Once done, click the "Stop Record" button. The software will automatically prompt a save window.
4. The result will be saved as a Zip file containing an MHT file, which includes step-by-step actions and screenshots.

### 解析MHT文件 Parse MHT files:

```bash
python parse_mht.py path/to/your/file.mht
```

### 使用LLM学习工作流 Use LLM to learn workflows:

```bash
python learn_workflow.py path/to/parsed/data.json
```

## 文件结构 File Structure:

```
llm-workflow-learning/
│
├── parse_mht.py          # 解析MHT文件的脚本
├── learn_workflow.py     # 使用LLM学习工作流的脚本
├── requirements.txt      # 项目依赖
├── README.md             # 项目说明文档
└── data/                 # 存放解析后的数据文件
```

```
llm-workflow-learning/
│
├── parse_mht.py          # Script to parse MHT files
├── learn_workflow.py     # Script to use LLM to learn workflows
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
└── data/                 # Directory to store parsed data files
```

## 贡献 Contributing

欢迎贡献！请提交Issue或Pull Request。

Contributions are welcome! Please submit an Issue or Pull Request.

## 许可证 License

本项目采用MIT许可证，详见LICENSE文件。

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## 联系方式 Contact

如果您有任何问题或需要进一步的信息，请联系项目维护者：[u3588064@connect.hku.hk](mailto:u3588064@connect.hku.hk)。

![qrcode_for_gh_643efb7db5bc_344(1)](https://github.com/u3588064/LLMemory/assets/53069671/8bb26c0f-4cab-438b-9f8c-16b1c26b3587)

