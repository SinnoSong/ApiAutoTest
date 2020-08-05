# ApiAutoTest
A simple api auto test frame,modify on https://github.com/yingoja/DemoAPI .
## How to use
Modify "APITestCase.xlsx","config.ini" in the "data" folder according to your needs,then run "run_all.py".
## 测试框架处理流程
- 调用被测试系统提供的接口，先数据驱动读取excel用例一行数据

- 发送请求数据，根据传参数据，向数据库查询得到对应的数据；

- 将查询的结果组装成JSON格式的数据，同时根据返回的数据值与Excel的值对比判断，并写入结果至指定Excel测试用例表格；

- 通过单元测试框架断言接口返回的数据，并生成测试报告，最后把生成最新的测试报告HTML文件发送指定的邮箱。

## todo:

- [x] 测试脚本excel中host使用配置文件配置，读取
- [ ] 预期结果简化，测试脚本excel测试结果3合1.
- [ ] 优化log功能
- [ ] 提供测试前初始化数据功能
- [ ] 修复执行测试后测试结果文件写入错误的问题



