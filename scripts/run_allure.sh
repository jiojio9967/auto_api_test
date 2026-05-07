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
echo "报告目录：allure-report/index.html"
echo "本地服务即将启动，如果要退出服务，请在终端按 control + C"

if ! allure open ./allure-report; then
    echo ""
    echo "allure open 启动失败，可改用备用命令："
    echo "    allure serve ./allure-results"
    exit 1
fi
