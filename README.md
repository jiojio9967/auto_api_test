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
