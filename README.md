## JStar自定义的OUC实验报告LaTeX模板

[![made-with-latex](https://img.shields.io/badge/Made%20with-LaTeX-1f425f.svg?color=green)](https://www.latex-project.org/)
[![GitHub license](https://img.shields.io/badge/License-LaTeX%20v1.3c-green.svg)](https://www.latex-project.org/lppl/lppl-1-3c)
[![Release](https://img.shields.io/badge/Release-v1.0.0.report-green.svg)](https://github.com/jstar0/LaTeXTemplate/releases)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-Maybe-yellow.svg)](https://github.com/jstar0/LaTeXTemplate/graphs/commit-activity)

### 介绍

本分支`report`专为实验报告设计，精简了不必要的页面，轻易上手。至于论文格式，请移步到分支`essay`使用。

---

本项目是基于 IPLeiria Thesis 项目进行的二次开发，主要用于中国海洋大学本科生实验报告或论文的撰写。本项目的目的是为中国海洋大学的学生提供一个简洁、易用、符合学校要求的 LaTeX 模板，使学生能够更加专注于论文的内容，而不是格式的调整。

源项目基于 LPPL v1.3c 协议，因此本项目在遵循此协议的前提上，合规地进行二改分发。您也可以在本项目的基础上进行二次开发。

### 相较于原项目的更改

- 修改了封面的内容，使其符合中国海洋大学的要求
- 更改多语言支持为中文和英文，去掉了葡萄牙语支持
- 去掉了一些不必要的页面（主要是留白），如需，可以通过指令`\plainblankpage`打印出来

---

以下是原项目的 README 内容：

## Polytechnic University of Leiria: LaTeX Thesis Template

### Description
Optimize your academic document creation with this LaTeX template tailored for theses and dissertations at the [Polytechnic University of Leiria](https://www.ipleiria.pt/). Tailored specifically for students within the School of Management and Technology (ESTG), this template guarantees a refined, timeless, and professionally formatted document. With its clean and classic aesthetic, navigating through the template is exceptionally straightforward, making document creation a seamless and efficient endeavor. Curious? Explore the [demo](https://www.overleaf.com/latex/templates/unofficial-polytechnic-university-of-leiria-estg-thesis-slash-report-template/tqgbrncfhwgt.pdf) to see more!

<p float="left">
  <img src="https://github.com/joseareia/ipleiria-thesis/blob/master/Assets/01_B.png" width="400"/>
  <img src="https://github.com/joseareia/ipleiria-thesis/blob/master/Assets/02_B.png" width="400"/>
</p>

### Getting Started
To utilise this template, please follow the steps below.

1. Download LaTeX:
    - Linux: Install [TeX-Live](https://www.tug.org/texlive/) or [MikTeX](https://miktex.org/).
    - Windows: Install [TeX-Live](https://www.tug.org/texlive/) or [MikTeX](https://miktex.org/).
    - macOS: Install [MacTeX](https://www.tug.org/mactex/) (a macOS version of TeX-Live) or [MikTeX](https://miktex.org/).
2. Download `IPLeiria Thesis` by either:
    - Cloning this GitHub repository (<kbd>git clone https://github.com/joseareia/ipleiria-thesis.git</kbd>).
    - Download the latest version as [ZIP file](https://github.com/joseareia/ipleiria-thesis/archive/refs/heads/master.zip).
3. Compile the document with you favorite LaTeX processor (pdfLaTeX, XeLaTeX or LuaLaTeX)!

> [!TIP]
> To make the most of this template and for real-time collaboration, I highly recommend using [Overleaf](https://www.overleaf.com/home-2). You can access the ready-to-use template by clicking [here](https://www.overleaf.com/latex/templates/unofficial-polytechnic-university-of-leiria-estg-thesis-slash-report-template/tqgbrncfhwgt).

### Content Overview
This repository has the following structure.

- **Bibliography**: Contains the bibliography file used for references.
- **Chapters**: Includes individual chapters of the thesis.
- **Code**: Includes any code examples related to the thesis.
- **Figures**: Contains figures and images used in the thesis.
- **Matter**: Contains additional matter (e.g. acronyms, glossary, etc.) and front/back pages for the thesis.
- **Variables**: Includes the `Variables.tex` document, where you can change the all the document variables.
- **IPLeiriaMain.tex**: Main LaTeX file for compiling the thesis content.
- **ThesisTemplate.cls**: LaTeX class file containing the formatting and styling specifications.

### Multilanguage Support
This template offers multilanguage support in two languages: English and Portuguese. **If you wish to add support for more languages, please contact me**. To change the language, simply modify the first line (*document class definition*) of the `ThesisTemplate.tex` file to the desired language: `pt` for Portuguese and `en` for English. Here is an example: `\documentclass[en]{ThesisTemplate}`. Easy, right?

### Getting Help
If you have any questions regarding the template, its usage, or encounter any errors you're struggling with, please feel free to open an issue in this repository, or contact me via email at <a href="mailto:jose.apareia@gmail.com">jose.apareia@gmail.com</a>.

### Contributing
Contributions to this template are welcome! If you encounter any issues, have suggestions for improvements, or would like to add new features, please submit a pull request. We appreciate your feedback and contributions to make this template even better.

### License
This project is under the [LPPL 1.3c](https://www.latex-project.org/lppl/lppl-1-3c/) license.
