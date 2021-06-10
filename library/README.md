## 河南理工大学图书馆预约系统API文档

> 为了方便替换，以下的网址均已用[URL]代替<http://seatlib.hpu.edu.cn>

##### 登录

| 地址     | [URL]/rest/auth                                          |
| -------- | -------------------------------------------------------- |
| 请求方式 | GET                                                      |
| 样例     | `[URL]/rest/auth?username=311709030330&password=1454767` |
| 返回类型 | application/json                                         |

| 请求参数名 | 含义 | 必要性 |
| ---------- | ---- | ------ |
| username   | 学号 | True   |
| password   | 密码 | True   |

| 返回参数名 | 含义     | 备注               |
| ---------- | -------- | ------------------ |
| status     | 状态     | `success`和`fail`  |
| data       | 返回数据 | 错误时无此参数     |
| code       | 状态码   | 正确时返回`0`      |
| message    | 错误信息 | 正确时返回空字符串 |
| data.token | Token    |                    |

##### 用户信息

| 地址     | [URL]/rest/v2/user                            |
| -------- | --------------------------------------------- |
| 请求方式 | GET                                           |
| 样例     | `[URL]/rest/v2/user?token=7U3M27V4PL06485448` |
| 返回类型 | application/json                              |

| 请求参数名 | 含义  | 必要性 |
| ---------- | ----- | ------ |
| token      | Token | True   |

| 返回参数名          | 含义         | 备注               |
| ------------------- | ------------ | ------------------ |
| status              | 状态         | `success`和`fail`  |
| data                | 数据         |                    |
| message             | 错误信息     | 正确时返回空字符串 |
| code                | 状态码       | 正确时返回`0`      |
| data.name           | 名字         | 学生姓名           |
| data.username       | 账号         | 学号               |
| data.lastIn         | 最后进馆时间 |                    |
| data.lastOut        | 最后出馆时间 |                    |
| data.violationCount | 违约信息     | 近60天违约信息     |
| data.checkedIn      | 是否签到     | 没有在馆即`false`  |

##### 历史预约记录

| 地址     | [URL]/rest/v2/history/{pages}/{count}                 |
| -------- | ----------------------------------------------------- |
| 请求方式 | GET                                                   |
| 样例     | `[URL]/rest/v2/history/1/10?token=7U3M27V4PL06485448` |
| 返回类型 | application/json                                      |


