<div align="center">

<img src="https://raw.githubusercontent.com/Mymiyu-tool/gray-intel/main/assets/icon.png" width="96" alt="gray-intel">
<img src="https://raw.githubusercontent.com/Mymiyu-tool/luckin-coffee/main/assets/icon.png" width="96" alt="luckin-coffee">

# Mymiyu Tool

Miyu 的自制软件包：脚本工具、检索器、生活服务。

**一个包一个仓库，Release 里直接下 `.miyu`。**

</div>

---

## 有什么

<img src="https://raw.githubusercontent.com/Mymiyu-tool/gray-intel/main/assets/icon.png" width="28" align="left" alt="">

### [gray-intel](https://github.com/Mymiyu-tool/gray-intel) — 灰产情报检索


给 Miyu 用的黑话搜索引擎。`中转站` 会自动扩展成 `API中转 / relay / 2api / 号池 / 倍率`，Bing + 360 双引擎，自动对 linux.do、v2ex、GitHub 做站内检索，并且**把「怎么选 / 排行 / 推荐」的带货文压下去，把「跑路 / 判刑 / 曝光」的实锤顶上来**。

```bash
curl -LO https://github.com/Mymiyu-tool/gray-intel/releases/download/v0.1.0/gray-intel-0.1.0.miyu
miyu pkg install gray-intel-0.1.0.miyu
```

<img src="https://raw.githubusercontent.com/Mymiyu-tool/luckin-coffee/main/assets/icon.png" width="28" align="left" alt="">

### [luckin-coffee](https://github.com/Mymiyu-tool/luckin-coffee) — 瑞幸咖啡


查附近门店、看菜单、预览价格、下单、查单、取消。走本机 `luckin` CLI 的登录态，不碰你的账号密码。

```bash
curl -LO https://github.com/Mymiyu-tool/luckin-coffee/releases/download/v0.1.0/luckin-coffee-0.1.0.miyu
miyu pkg install luckin-coffee-0.1.0.miyu
```

---

## 全部包

这份表格由仓库里的 workflow 自动从组织拉取，只收录带 `miyu-package` topic 的公开仓库。

<!-- packages:start -->
| 包 | 说明 | 仓库 |
|---|---|---|
| **gray-intel** | Gray-market OSINT search for Miyu: slang expansion, dual engines, forum dorks, SEO-farm downranking | [Mymiyu-tool/gray-intel](https://github.com/Mymiyu-tool/gray-intel) |
| **luckin-coffee** | Luckin Coffee ordering for Miyu: stores, menus, preview, create, detail and cancel orders through the local luckin CLI | [Mymiyu-tool/luckin-coffee](https://github.com/Mymiyu-tool/luckin-coffee) |
<!-- packages:end -->

---

## 装法

```bash
# Release 里的包文件
curl -LO https://github.com/Mymiyu-tool/<repo>/releases/latest/download/<name>-<version>.miyu
miyu pkg install <name>-<version>.miyu

# 或者从源码目录
git clone https://github.com/Mymiyu-tool/<repo>.git
miyu pkg install ./<repo>
```

装完直接对 Miyu 说「用 xxx 工具帮我…」就行。

> Miyu 官方源后续会收录社区包，收录后直接 `miyu pkg install <id>` 即可，不用再手动下载。在那之前走 Release 里的 `.miyu`。

## 写一个自己的

Miyu 包 = 一个目录 + `package.toml` + `scripts/*.py`。脚本顶部的注释就是参数 Schema。

详见 [gray-intel 的源码](https://github.com/Mymiyu-tool/gray-intel)，它只有 6 个文件。
