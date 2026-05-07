# Auto API Test

## 本地运行 Allure 报告

运行接口自动化并生成报告：

```bash
bash scripts/run_allure.sh
```

如果脚本没有执行权限，先执行：

```bash
chmod +x scripts/run_allure.sh
```

也可以直接执行：

```bash
./scripts/run_allure.sh
```

手动打开报告：

```bash
open allure-report/index.html
```

或：

```bash
allure open allure-report
```

`allure-results/` 和 `allure-report/` 是本地运行产物，已在 `.gitignore` 中忽略，不需要提交到 Git。

## 鉴权配置

接口 token 与 sign 优先从环境变量读取，未设置时回退到 `public/headers.py` 中的本地默认值。

可选环境变量：

- `API_TOKEN`：覆盖请求头 `authorization`
- `API_SIGN`：覆盖请求头 `sign`

本地推荐方式：把环境变量写入项目根目录的 `.env`（已在 `.gitignore` 中忽略），运行前通过 shell 加载，例如：

```bash
export $(grep -v '^#' .env | xargs)
bash scripts/run_allure.sh
```

`.env` 示例（不要提交到 Git）：

```dotenv
API_TOKEN=你最新的token
API_SIGN=你最新的sign
```

