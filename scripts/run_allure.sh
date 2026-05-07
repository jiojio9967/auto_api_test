#!/usr/bin/env bash
set -e

echo "清理旧的 Allure 运行产物..."
rm -rf allure-results allure-report

echo "执行 pytest 并生成 allure-results..."
python3 -m pytest testcases --alluredir=./allure-results

echo "生成 Allure 报告..."
allure generate ./allure-results -o ./allure-report --clean

echo "测试执行完成"
echo "Allure 报告已生成"
echo "报告路径：allure-report/index.html"

echo "打开本地 Allure 报告..."
if command -v allure >/dev/null 2>&1; then
    allure open ./allure-report
elif [[ "$(uname)" == "Darwin" ]]; then
    open ./allure-report/index.html
else
    echo "当前系统未检测到可用的自动打开命令，请手动打开 allure-report/index.html"
fi
