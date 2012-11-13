#Recent contest

###功能：
获取最新的ACM比赛信息并生成静态页面。

###实现方法
- 从http://contests.acmicpc.info/contests.json读取信息
- 解析json，获取数据
- 整合模板，生成静态页面

###其他
设置系统任务，每个1小时执行一次，实现定期更新。
