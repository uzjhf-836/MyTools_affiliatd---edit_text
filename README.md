# edit_text

[![Python](https://img.shields.io/badge/Python-3.6+-yellow?logo=python)](https://python.org)
[![Version](https://img.shields.io/badge/Version-v1.0.0-blue)](https://github.com/uzjhf-836/MyTools_affiliatd---edit_text)
[![License](https://img.shields.io/badge/License-Apache_2.0-green)](https://apache.org/licenses/LICENSE-2.0)
[![Platform](https://img.shields.io/badge/Platform-Windows/macOS/Linux-white)](https://www.bing.com/search?q=all+platforms)
[![Commit](https://img.shields.io/github/last-commit/uzjhf-836/MyTools_affiliatd---edit_text?logo=github)](https://github.com/uzjhf-836/MyTools_affiliatd---edit_text/commits/main)
[![Co-Author](https://img.shields.io/badge/Co--Author-Claude-8A2BE2?logo=claude)](https://claude.ai)

> MyTools「Text」类的加强版 —— 纯 Python 命令行文本工具集，~~零依赖~~<Python是个依赖qwq！

---

# 警告
由于本程序使用了f-string，使用本程序Python版本最低为3.6

## 📋 目录

- [概述](#-概述)
- [功能一览](#-功能一览)
- [安装](#-安装)
- [使用指南](#-使用指南)
  - [文本工具](#文本工具)
  - [哈希计算](#哈希计算)
  - [编解码](#编解码)
  - [密码学](#密码学)
  - [文件工具](#文件工具)
  - [其他工具](#其他工具)
- [示例](#-示例)
- [项目结构](#-项目结构)
- [许可证](#-许可证)

---

## 📖 概述

**edit_text** 是一个功能丰富的命令行文本处理工具，从简单的文本替换到 RSA 非对称加密一应俱全。

### 特点

~~零依赖~~ —— 纯 Python 标准~~库~~实现，**无需 pip install**
- **覆盖全面** —— 文本、哈希、编解码、密码学、文件处理
- **简单易用** —— 命令行参数直截了当，--help 即学即用
- **纯 Python 实现** —— RSA、SHA 系列哈希等算法均从零手写

---

## 🚀 功能一览

### 文本工具

| 功能 | 命令 | 说明 |
|------|------|------|
| 反转字符串 | `--text reverse` | 从右到左反转文本 |
| 文本替换 | `--text replace` | all / place / precise_place 三种模式 |
| 大小写转换 | `--text case` | upper / lower / title |
| 字数统计 | `--text count` | 字符数、行数统计 |
| 排序去重 | `--text sort` | 按行排序，可选 uniq 去重 |
| 按分隔符拆分 | `--text split` | 按指定分隔符拆分文本 |
| 重复文本 | `--text repeat` | 将文本重复 N 遍 |
| 截取子串 | `--text slice` | 取文本第 X 到 Y 位 |
| 取分段 | `--text at` | 以分隔符取第 N 段（支持负数索引） |

### 哈希计算

| 算法 | 命令 |
|------|------|
| MD5 | `--hash md5` |
| SHA-1 | `--hash sha1` |
| SHA-256 | `--hash sha256` |
| SHA-384 | `--hash sha384` |
| SHA-512 | `--hash sha512` |
| RIPEMD-160 | `--hash ripemd160` |
| CRC32 | `--hash crc32` |

### 编解码

| 功能 | 命令 |
|------|------|
| Base64 | `--base64 encode/decode` |
| URL 编解码 | `--url encode/decode` |
| 十六进制 | `--hex encode/decode` |
| 二进制 | `--bin encode/decode` |
| 摩斯电码 | `--morse encode/decode` |

### 密码学

| 功能 | 命令 | 说明 |
|------|------|------|
| ROT 移位密码 | `--rot` | ASCII / Unicode 模式 |
| Atbash 密码 | `--atbash` | 字母表反转 |
| XOR 加解密 | `--xor` | 异或加密/解密 |
| **RSA 非对称加密** | `--rsa` | 密钥生成 / 加密 / 解密 / 提取公钥 |

### 文件工具

| 功能 | 命令 |
|------|------|
| 读取文件 | `--file read` |
| 写入文件 | `--file write` |
| 文件哈希 | `--file hash` |
| 文件编解码 | `--file encode` |

### 其他工具

| 功能 | 命令 | 说明 |
|------|------|------|
| 阅读时间统计 | `--stats` | 估算文本阅读时间 |
| 随机十六进制 | `--tools randhex` | 生成随机十六进制数 |
| 随机密码 | `--tools randpass` | 生成随机密码 |
| 进制转换 | `--tools base` | 任意进制互转 |
| 彩红字 | `--rainbow` | 彩色渐变输出 |

---

## 📦 安装

```bash
# 克隆仓库
git clone https://github.com/uzjhf-836/MyTools_affiliatd---edit_text.git

# 直接使用（无需安装）
cd MyTools_affiliatd---edit_text
python edit_text_v1_0_0.py --help
```

> 要求 Python 3.6+
---

## 🔧 使用指南

## 调用方法:
### 1.命令行参数
### 文本工具

```bash
# 反转字符串
python edit_text_v1_0_0.py --text reverse "Hello World"

# 替换文本（普通替换）
python edit_text_v1_0_0.py --text replace "old" "new" "some old text"

# 大小写转换
python edit_text_v1_0_0.py --text case upper "hello world"

# 重复文本 3 遍
python edit_text_v1_0_0.py --text repeat 3 "Ha! "

# 取第 0 到 5 位
python edit_text_v1_0_0.py --text slice 0 5 "Hello World"

# 以空格分割取第 1 段
python edit_text_v1_0_0.py --text at " " 1 "Hello World"
```

### 哈希计算

```bash
python edit_text_v1_0_0.py --hash md5 "hello"
python edit_text_v1_0_0.py --hash sha256 "hello"
python edit_text_v1_0_0.py --hash crc32 "hello"
```

### 编解码

```bash
python edit_text_v1_0_0.py --base64 encode "Hello World"
python edit_text_v1_0_0.py --url encode "https://example.com?a=1&b=2"
python edit_text_v1_0_0.py --morse encode "SOS"
```

### RSA 非对称加密

```bash
# 生成 2048 位密钥对
python edit_text_v1_0_0.py --rsa generate 2048

# 用公钥加密
python edit_text_v1_0_0.py --rsa encrypt public.pem "秘密消息"

# 用私钥解密
python edit_text_v1_0_0.py --rsa decrypt private.pem "<密文>"

# 从私钥提取公钥
python edit_text_v1_0_0.py --rsa pubkey private.pem
```

### 文件工具

```bash
python edit_text_v1_0_0.py --file read input.txt
python edit_text_v1_0_0.py --file hash sha256 input.txt
```

---

### 2.导入模块
```python
import edit_text_v1_0_0
使用任何函数！
```
## 💡 示例

```bash
# 摩斯电码 + 反转 + 统计一条龙
$ python edit_text_v1_0_0.py --morse encode "HELLO"
.... . .-.. .-.. ---

$ python edit_text_v1_0_0.py --text reverse ".... . .-.. .-.. ---"
--- ..-. .-.. .- ....

$ python edit_text_v1_0_0.py --stats "文章内容..."
阅读时间: 约 2 分钟 (340 字)
```

---

## 📁 项目结构

```
edit_text_v1_0_0.py    # 主程序（单文件，全部功能）
version.txt            # 版本信息
.gitignore             # 忽略 __pycache__
README.md              # 本文件
```

---

## 📄 许可证

[Apache License 2.0](https://apache.org/licenses/LICENSE-2.0)

---

*由 uzjhf-836 和 Claude 共同开发*
