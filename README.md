<div align="center">

# Mymiyu Tool

**自制的 Miyu 软件包，一个仓库一个包。**

装法都一样：下载 Release 里的 `.miyu`，或者 clone 下来 `miyu pkg install ./目录`。

</div>

---

## 包列表

| 包 | 做什么 | 依赖 | 安装 |
|---|---|---|---|
| [**gray-intel**](https://github.com/Mymiyu-tool/gray-intel) · 灰产情报检索 | 黑话扩展、Bing + 360 双引擎、论坛站内 dork、软文降权 | Python 标准库 | `curl -LO https://github.com/Mymiyu-tool/gray-intel/releases/download/v0.1.0/gray-intel-0.1.0.miyu` 后 `miyu pkg install` |
| [**luckin-coffee**](https://github.com/Mymiyu-tool/luckin-coffee) · 瑞幸咖啡 | 查门店、看菜单、预览、下单、查单、取消 | 本机 `luckin` CLI 已登录 | `curl -LO https://github.com/Mymiyu-tool/luckin-coffee/releases/download/v0.1.0/luckin-coffee-0.1.0.miyu` 后 `miyu pkg install` |

## 安装一个包

```bash
# 方式一：直接装 Release 里的包文件
curl -LO https://github.com/Mymiyu-tool/gray-intel/releases/download/v0.1.0/gray-intel-0.1.0.miyu
miyu pkg install gray-intel-0.1.0.miyu

# 方式二：clone 后从目录装（方便改）
git clone https://github.com/Mymiyu-tool/gray-intel.git
miyu pkg install ./gray-intel
```

装完在 Miyu 里会多出对应的工具，下一轮对话就能用。

## 自己做一个包

Miyu 的包就是一个带 `package.toml` 的目录，`scripts/` 下每个文件是一个工具：

```text
my-package/
├── package.toml
├── README.md
├── LICENSE
└── scripts/
    └── hello.py
```

```toml
[package]
version = "0.1.0"
name = { en = "Hello", zh = "你好" }
summary = { en = "Say hello", zh = "打个招呼" }
author = "your-name"
icon = "sparkles"
```

脚本顶部的注释就是工具的参数 Schema，写好后 `miyu pkg install ./my-package` 即可。

## 许可

每个包各自采用 MIT，见各仓库的 `LICENSE`。
