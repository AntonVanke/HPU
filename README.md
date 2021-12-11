[TOC]

## /图书馆座位管理接口

```text
暂无描述
```
#### 公共Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 公共Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 公共Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 预执行脚本
```javascript
apt.globals.set("URL", "http://seatlib.hpu.edu.cn");
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /图书馆座位管理接口/获取公告
```text
暂无描述
```
#### 接口状态
> 开发中

#### 接口URL
> http://seatlib.hpu.edu.cn/rest/v2/announce

#### 请求方式
> GET

#### Content-Type
> form-data

#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /图书馆座位管理接口/获取系统信息
```text
暂无描述
```
#### 接口状态
> 开发中

#### 接口URL
> http://seatlib.hpu.edu.cn/rest/v2/settings

#### 请求方式
> GET

#### Content-Type
> form-data

#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"data": {
		"expressCompleteMins": 0,
		"buildingExpressCheckoutStatuses": [
			[
				1,
				false
			],
			[
				2,
				false
			],
			[
				3,
				false
			]
		],
		"buildingOpenClose": [
			[
				1,
				"07:30",
				"22:00"
			],
			[
				2,
				"07:00",
				"22:00"
			],
			[
				3,
				"07:30",
				"22:00"
			]
		],
		"wifiAwayDisabled": false,
		"wifiStopDisabled": false,
		"checkInAheadMins": 30,
		"lateAllowedMins": 15
	},
	"message": null,
	"status": true
}
```
参数名 | 示例值 | 参数类型 | 参数描述
--- | --- | --- | ---
data | - | Text | 返回数据
data.expressCompleteMins | 0 | Text | 
data.buildingExpressCheckoutStatuses | - | Text | 自动签到设置
data.buildingExpressCheckoutStatuses.0 | 1 | Text | 图书馆ID
data.buildingExpressCheckoutStatuses.1 | false | Text | 是否自动签到
data.buildingOpenClose | - | Text | 图书馆开馆闭馆设置
data.buildingOpenClose.0 | 1 | Text | 图书馆ID
data.buildingOpenClose.1 | 07:30 | Text | 开馆时间
data.buildingOpenClose.2 | 22:00 | Text | 闭馆时间
data.wifiAwayDisabled | false | Text | 是否允许在非内网暂离
data.wifiStopDisabled | false | Text | 是否允许在非内网
data.checkInAheadMins | 30 | Text | 提前允许签到时间
data.lateAllowedMins | 15 | Text | 迟后允许签到时间
message | - | Text | 返回信息
status | true | Text | 返回状态
## /图书馆座位管理接口/获取Token
```text
暂无描述
```
#### 接口状态
> 开发中

#### 接口URL
> http://seatlib.hpu.edu.cn/rest/auth?username=311809030326&password=123456

#### 请求方式
> GET

#### Content-Type
> form-data

#### 请求Query参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
username | 311809030326 | Text | 是 | -
password | 123456 | Text | 是 | -
#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
captcha | 111 | Text | 是 | -
username | 311809030326 | Text | 是 | -
password | 123456 | Text | 是 | -
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"status": "success",
	"data": {
		"token": "V46UFSWIBL11065152"
	},
	"code": "0",
	"message": ""
}
```
参数名 | 示例值 | 参数类型 | 参数描述
--- | --- | --- | ---
status | success | Text | 返回状态
data | - | Text | 返回数据
data.token | V46UFSWIBL11065152 | Text | 用户Token
code | 0 | Text | 错误码
message | - | Text | 错误信息
#### 错误响应示例
```javascript
{
	"status": "fail",
	"code": "13",
	"message": "登录失败: 用户名或密码不正确",
	"data": null
}
```
## /图书馆座位管理接口/获取用户信息
```text
暂无描述
```
#### 接口状态
> 开发中

#### 接口URL
> http://seatlib.hpu.edu.cn/rest/v2/user?token=2M2Q4OI62T12012621

#### 请求方式
> GET

#### Content-Type
> form-data

#### 请求Query参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
token | 2M2Q4OI62T12012621 | Text | 是 | -
#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
token | GBZU8G587G11282250 | Text | 是 | -
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"status": "success",
	"data": {
		"id": 24254,
		"enabled": true,
		"name": "冯君奭",
		"username": "311809030326",
		"username2": null,
		"status": "NORMAL",
		"lastLogin": null,
		"checkedIn": false,
		"reservationStatus": null,
		"lastIn": null,
		"lastOut": null,
		"lastInBuildingId": null,
		"lastInBuildingName": null,
		"violationCount": 0
	},
	"message": "",
	"code": "0"
}
```
参数名 | 示例值 | 参数类型 | 参数描述
--- | --- | --- | ---
status | success | Text | 返回状态
data | - | Text | 返回数据
data.id | 24254 | Text | 用户iD
data.enabled | true | Text | 是否启用账户
data.name | 冯君奭 | Text | 用户姓名
data.username | 311809030326 | Text | 用户账号(学号)
data.username2 | - | Text | 用户账号2
data.status | NORMAL | Text | 账户状态
data.lastLogin | - | Text | 最后登录时间
data.checkedIn | false | Text | 是否签到
data.reservationStatus | - | Text | 
data.lastIn | - | Text | 
data.lastOut | - | Text | 
data.lastInBuildingId | - | Text | 
data.lastInBuildingName | - | Text | 
data.violationCount | 0 | Text | 
message | - | Text | 错误信息
code | 0 | Text | 错误码
#### 错误响应示例
```javascript
{
	"status": "fail",
	"code": "12",
	"message": "登录失败: 用户名或密码不正确"
}
```
参数名 | 示例值 | 参数类型 | 参数描述
--- | --- | --- | ---
status | fail | Text | 返回状态
code | 12 | Text | 错误码
message | 登录失败: 用户名或密码不正确 | Text | 错误信息
## /图书馆座位管理接口/签到
```text
暂无描述
```
#### 接口状态
> 开发中

#### 接口URL
> http://seatlib.hpu.edu.cn/rest/v2/checkIn?token=JGJVNZC3HM11243643

#### 请求方式
> GET

#### Content-Type
> form-data

#### 请求Query参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
token | JGJVNZC3HM11243643 | Text | 是 | -
#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
token | GBZU8G587G11282250 | Text | 是 | -
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 错误响应示例
```javascript
{
	"status": "fail",
	"data": null,
	"message": "请连接此场馆无线网或在触屏机上操作",
	"code": "1"
}
```
## /图书馆座位管理接口/取消暂未履约的预约
```text
暂无描述
```
#### 接口状态
> 开发中

#### 接口URL
> http://seatlib.hpu.edu.cn/rest/v2/cancel/:reserve_id?token=*

#### 请求方式
> GET

#### Content-Type
> form-data

#### 请求Query参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
token | * | Text | 是 | -
#### 路径变量
参数名 | 示例值 | 参数描述
--- | --- | ---
reserve_id | 4589305 | 预约ID
#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
token | GBZU8G587G11282250 | Text | 是 | -
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"status": "success",
	"data": {
		"totalCancelled": 1,
		"allowedCancel": 15
	},
	"message": "",
	"code": "0"
}
```
参数名 | 示例值 | 参数类型 | 参数描述
--- | --- | --- | ---
status | success | Text | 返回状态
data | - | Text | 返回数据
data.totalCancelled | 1 | Text | 近60天取消情况
data.allowedCancel | 15 | Text | 允许的取消次数
message | - | Text | 返回信息
code | 0 | Text | 错误码
#### 错误响应示例
```javascript
{
	"status": "fail",
	"data": null,
	"message": "预约状态错误，无法取消",
	"code": "1"
}
```
参数名 | 示例值 | 参数类型 | 参数描述
--- | --- | --- | ---
status | fail | Text | 返回状态
data | - | Text | 返回数据
message | 预约状态错误，无法取消 | Text | 错误信息
code | 1 | Text | 错误码
## /图书馆座位管理接口/历史记录
```text
暂无描述
```
#### 接口状态
> 开发中

#### 接口URL
> http://seatlib.hpu.edu.cn/rest/v2/history/:page/:batch?token=*

#### 请求方式
> GET

#### Content-Type
> form-data

#### 请求Query参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
token | * | Text | 是 | -
#### 路径变量
参数名 | 示例值 | 参数描述
--- | --- | ---
page | 1 | 页码
batch | 9999 | 单页数量
#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
token | GBZU8G587G11282250 | Text | 是 | -
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"status": "success",
	"data": {
		"reservations": [
			{
				"id": 4508704,
				"date": "2021-11-17",
				"begin": "17:00",
				"end": "21:00",
				"awayBegin": null,
				"awayEnd": null,
				"loc": "南校区第二图书馆7层7层自主学习空间（Ⅳ）322号",
				"stat": "RESERVE"
			},
			{
				"id": 4477346,
				"date": "2021-11-14",
				"begin": "14:30",
				"end": "18:30",
				"awayBegin": null,
				"awayEnd": null,
				"loc": "南校区第二图书馆7层7层自主学习空间（Ⅳ）330号",
				"stat": "COMPLETE"
			}
		]
	},
	"message": "",
	"code": "0"
}
```
参数名 | 示例值 | 参数类型 | 参数描述
--- | --- | --- | ---
status | success | Text | 返回状态
data | - | Text | 返回数据
data.reservations | - | Text | 预约列表
data.reservations.id | 4508704 | Text | 预约ID
data.reservations.date | 2021-11-17 | Text | 预约日期
data.reservations.begin | 17:00 | Text | 预约开始时间
data.reservations.end | 21:00 | Text | 预约结束时间
data.reservations.awayBegin | - | Text | 暂离开始时间
data.reservations.awayEnd | - | Text | 暂离结束时间
data.reservations.loc | 南校区第二图书馆7层7层自主学习空间（Ⅳ）322号 | Text | 预约地址
data.reservations.stat | RESERVE | Text | 预约状态
message | - | Text | 错误信息
code | 0 | Text | 错误码
#### 错误响应示例
```javascript
{
	"status": "fail",
	"code": "12",
	"message": "登录失败: 用户名或密码不正确"
}
```
参数名 | 示例值 | 参数类型 | 参数描述
--- | --- | --- | ---
status | fail | Text | 返回状态
code | 12 | Text | 错误码
message | 登录失败: 用户名或密码不正确 | Text | 错误信息
## /图书馆座位管理接口/释放履约中座位
```text
暂无描述
```
#### 接口状态
> 开发中

#### 接口URL
> http://seatlib.hpu.edu.cn/rest/v2/stop?token=*

#### 请求方式
> GET

#### Content-Type
> form-data

#### 请求Query参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
token | * | Text | 是 | -
#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
token | GBZU8G587G11282250 | Text | 是 | -
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 错误响应示例
```javascript
{
	"status": "fail",
	"data": null,
	"message": "当前没有可用预约",
	"code": "1"
}
```
参数名 | 示例值 | 参数类型 | 参数描述
--- | --- | --- | ---
status | fail | Text | 返回状态
data | - | Text | 返回数据
message | 当前没有可用预约 | Text | 错误信息
code | 1 | Text | 错误码
## /图书馆座位管理接口/获取当前预约信息
```text
暂无描述
```
#### 接口状态
> 开发中

#### 接口URL
> http://seatlib.hpu.edu.cn/rest/v2/user/reservations?token=8VVFS3G2B712013244

#### 请求方式
> GET

#### Content-Type
> form-data

#### 请求Query参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
token | 8VVFS3G2B712013244 | Text | 是 | -
#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
token | GBZU8G587G11282250 | Text | 是 | -
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"status": "success",
	"data": [
		{
			"id": 4508704,
			"receipt": "0330-704-3",
			"onDate": "2021-11-17",
			"seatId": 18397,
			"status": "RESERVE",
			"location": "南校区第二图书馆7层7层自主学习空间（Ⅳ），座位号322",
			"begin": "17:00",
			"end": "21:00",
			"actualBegin": null,
			"awayBegin": null,
			"awayEnd": null,
			"userEnded": false,
			"message": "请在 11月17日16点30分 至 17点15分 之间前往场馆签到"
		}
	],
	"message": "",
	"code": "0"
}
```
参数名 | 示例值 | 参数类型 | 参数描述
--- | --- | --- | ---
status | success | Text | 返回状态
data | - | Text | 返回数据
data.id | 4508704 | Text | 预约ID
data.receipt | 0330-704-3 | Text | 预约凭证号
data.onDate | 2021-11-17 | Text | 任务时间
data.seatId | 18397 | Text | 座位ID
data.status | RESERVE | Text | 预约状态
data.location | 南校区第二图书馆7层7层自主学习空间（Ⅳ），座位号322 | Text | 预约地址
data.begin | 17:00 | Text | 预约开始时间
data.end | 21:00 | Text | 预约结束时间
data.actualBegin | - | Text | 
data.awayBegin | - | Text | 
data.awayEnd | - | Text | 
data.userEnded | false | Text | 
data.message | 请在 11月17日16点30分 至 17点15分 之间前往场馆签到 | Text | 预约信息
message | - | Text | 错误信息
code | 0 | Text | 错误码
## /图书馆座位管理接口/获取60天内的违约信息
```text
暂无描述
```
#### 接口状态
> 开发中

#### 接口URL
> http://seatlib.hpu.edu.cn/rest/v2/violations?token=*

#### 请求方式
> GET

#### Content-Type
> form-data

#### 请求Query参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
token | * | Text | 是 | -
#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
token | GBZU8G587G11282250 | Text | 是 | -
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"data": [],
	"message": null,
	"status": true
}
```
参数名 | 示例值 | 参数类型 | 参数描述
--- | --- | --- | ---
data | {} | Text | 返回数据
message | - | Text | 错误信息
status | true | Text | 返回状态
## /图书馆座位管理接口/可用座位查询
```text
暂无描述
```
#### 接口状态
> 开发中

#### 接口URL
> http://seatlib.hpu.edu.cn/rest/v2/searchSeats/:date/:start_time/:end_time?token=JGJVNZC3HM11243643&roomId=29&batch=9999&page=1

#### 请求方式
> GET

#### Content-Type
> form-data

#### 请求Header参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
Accept | */* | Text | 是 | -
User-Agent | doSingle/11 CFNetwork/1312 Darwin/21.0.0 | Text | 是 | -
#### 请求Query参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
token | JGJVNZC3HM11243643 | Text | 是 | -
roomId | 29 | Text | 是 | -
batch | 9999 | Text | 是 | -
page | 1 | Text | 是 | -
#### 路径变量
参数名 | 示例值 | 参数描述
--- | --- | ---
date | 2021-11-28 | 预约日期
start_time | 750 | 
end_time | 850 | 
#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
token | GBZU8G587G11282250 | Text | 是 | -
roomId | 29 | Text | 是 | -
batch | 9999 | Text | 是 | -
page | 1 | Text | 是 | -
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"data": {
		"seats": {
			"3006": {
				"id": 14160,
				"name": "078",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"3008": {
				"id": 14162,
				"name": "082",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"3013": {
				"id": 14167,
				"name": "146",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"3014": {
				"id": 14168,
				"name": "145",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"3017": {
				"id": 14171,
				"name": "154",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"5006": {
				"id": 14202,
				"name": "075",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"5015": {
				"id": 19618,
				"name": "147",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"5016": {
				"id": 19619,
				"name": "148",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"5017": {
				"id": 19620,
				"name": "151",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"5018": {
				"id": 19621,
				"name": "152",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"7007": {
				"id": 14245,
				"name": "065",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"7008": {
				"id": 14246,
				"name": "070",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"7014": {
				"id": 14252,
				"name": "133",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"7015": {
				"id": 14253,
				"name": "138",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"7016": {
				"id": 14254,
				"name": "137",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"9004": {
				"id": 14284,
				"name": "059",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"9005": {
				"id": 14285,
				"name": "060",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"9013": {
				"id": 14293,
				"name": "131",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"9018": {
				"id": 14298,
				"name": "140",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"11005": {
				"id": 14327,
				"name": "049",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"11006": {
				"id": 14328,
				"name": "054",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"11013": {
				"id": 14335,
				"name": "122",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"11018": {
				"id": 14340,
				"name": "129",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"13007": {
				"id": 14371,
				"name": "052",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"13013": {
				"id": 14377,
				"name": "119",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"13015": {
				"id": 14379,
				"name": "123",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"13016": {
				"id": 14380,
				"name": "124",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"13017": {
				"id": 14381,
				"name": "127",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"19006": {
				"id": 14496,
				"name": "042",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"19014": {
				"id": 14504,
				"name": "109",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"19015": {
				"id": 14505,
				"name": "114",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"19016": {
				"id": 14506,
				"name": "113",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"19017": {
				"id": 14507,
				"name": "118",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"21006": {
				"id": 14538,
				"name": "039",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"21007": {
				"id": 14539,
				"name": "040",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"21017": {
				"id": 14549,
				"name": "115",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"23005": {
				"id": 14579,
				"name": "025",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"23007": {
				"id": 14581,
				"name": "029",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"23017": {
				"id": 14591,
				"name": "106",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"23018": {
				"id": 14592,
				"name": "105",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"25006": {
				"id": 14622,
				"name": "027",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"25008": {
				"id": 14624,
				"name": "031",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"25013": {
				"id": 14629,
				"name": "095",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"25016": {
				"id": 14632,
				"name": "100",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"26021": {
				"id": 14771,
				"name": "157",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"27014": {
				"id": 14672,
				"name": "085",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"27018": {
				"id": 14676,
				"name": "093",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"29014": {
				"id": 14714,
				"name": "084",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"29015": {
				"id": 14715,
				"name": "087",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"29016": {
				"id": 14716,
				"name": "088",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			},
			"30021": {
				"id": 14742,
				"name": "155",
				"type": "seat",
				"status": "FREE",
				"window": false,
				"power": false,
				"computer": false,
				"local": false
			}
		},
		"page": 1,
		"hasMore": false
	},
	"message": null,
	"status": true
}
```
## /图书馆座位管理接口/预约座位
```text
暂无描述
```
#### 接口状态
> 开发中

#### 接口URL
> http://seatlib.hpu.edu.cn/rest/v2/freeBook?token=ZFHWC5PO7A12065227&seat=13218&startTime=1140&endTime=1170&date=2021-12-06

#### 请求方式
> POST

#### Content-Type
> form-data

#### 请求Header参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
HOST | seatlib.hpu.edu.cn:8443 | Text | 是 | -
#### 请求Query参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
token | ZFHWC5PO7A12065227 | Text | 是 | -
seat | 13218 | Text | 是 | -
startTime | 1140 | Text | 是 | -
endTime | 1170 | Text | 是 | -
date | 2021-12-06 | Text | 是 | -
#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
token | GBZU8G587G11282250 | Text | 是 | -
seat | 14163 | Text | 是 | -
startTime | 760 | Text | 是 | -
endTime | 860 | Text | 是 | -
date | 2021-11-28 | Text | 是 | -
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"status": "success",
	"data": {
		"id": 4737674,
		"receipt": "0330-674-1",
		"onDate": "2021 年 12 月 06 日",
		"begin": "21 : 00",
		"end": "21 : 30",
		"location": "南校区第二图书馆5层5层工程技术类借阅区，座位号097",
		"checkedIn": false,
		"checkInMsg": "当前没有可用预约"
	},
	"message": "",
	"code": "0"
}
```
参数名 | 示例值 | 参数类型 | 参数描述
--- | --- | --- | ---
status | success | Text | 返回状态
data | - | Text | 返回数据
data.id | 4737674 | Text | 用户iD
data.receipt | 0330-674-1 | Text | 
data.onDate | 2021 年 12 月 06 日 | Text | 
data.begin | 21 : 00 | Text | 
data.end | 21 : 30 | Text | 
data.location | 南校区第二图书馆5层5层工程技术类借阅区，座位号097 | Text | 
data.checkedIn | false | Text | 是否签到
data.checkInMsg | 当前没有可用预约 | Text | 
message | - | Text | 错误信息
code | 0 | Text | 错误码
## /图书馆座位管理接口/获取各馆信息
```text
暂无描述
```
#### 接口状态
> 开发中

#### 接口URL
> http://seatlib.hpu.edu.cn/rest/v2/free/filters?token=B5IQ0U721T11262738

#### 请求方式
> GET

#### Content-Type
> form-data

#### 请求Query参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
token | B5IQ0U721T11262738 | Text | 是 | -
#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
token | GBZU8G587G11282250 | Text | 是 | -
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"status": "success",
	"data": {
		"buildings": [
			[
				1,
				"南校区第一图书馆",
				6
			],
			[
				3,
				"南校区第二图书馆",
				8
			],
			[
				2,
				"北校区图书馆",
				4
			]
		],
		"rooms": [
			[
				1,
				"五楼天井区",
				1,
				5
			],
			[
				2,
				"五楼自习区",
				1,
				5
			],
			[
				3,
				"三楼天井区",
				1,
				3
			],
			[
				4,
				"四楼天井区",
				1,
				4
			],
			[
				5,
				"六楼自习区",
				1,
				6
			],
			[
				11,
				"朗读亭",
				1,
				2
			],
			[
				12,
				"一层大厅",
				1,
				1
			],
			[
				15,
				"4层工程技术类借阅区",
				3,
				4
			],
			[
				17,
				"5层工程技术类借阅区",
				3,
				5
			],
			[
				19,
				"5层自然科学借阅区",
				3,
				5
			],
			[
				23,
				"6层社会科学借阅区（Ⅰ）",
				3,
				6
			],
			[
				25,
				"7层社会科学类借阅区2",
				3,
				7
			],
			[
				26,
				"7层社会科学类借阅区1",
				3,
				7
			],
			[
				28,
				"7层自主学习空间（V）",
				3,
				7
			],
			[
				29,
				"1层自主学习空间（Ⅰ）",
				3,
				1
			],
			[
				30,
				"3层自主学习空间（Ⅱ）",
				3,
				3
			],
			[
				31,
				"7层自主学习空间（Ⅳ）",
				3,
				7
			],
			[
				32,
				"3层自主学习空间（Ⅲ）",
				3,
				3
			],
			[
				33,
				"2层报刊阅览区",
				3,
				2
			],
			[
				34,
				"4层计算机类借阅区",
				3,
				4
			],
			[
				35,
				"6层社会科学类借阅区(Ⅱ)",
				3,
				6
			],
			[
				7,
				"负一楼自习区",
				2,
				1
			],
			[
				8,
				"一楼自习区",
				2,
				1
			],
			[
				9,
				"三楼自习区A",
				2,
				3
			],
			[
				10,
				"三楼自习区B",
				2,
				3
			]
		],
		"hours": 4,
		"dates": [
			"2021-11-26"
		]
	},
	"message": "",
	"code": "0"
}
```
参数名 | 示例值 | 参数类型 | 参数描述
--- | --- | --- | ---
status | success | Text | 返回状态
data | - | Text | 返回数据
data.buildings | - | Text | 各馆信息
data.buildings.0 | 1 | Text | 图书馆ID
data.buildings.1 | 南校区第一图书馆 | Text | 图书馆名称
data.buildings.2 | 6 | Text | 楼层总数
data.rooms | - | Text | 图书馆房间信息
data.rooms.0 | 1 | Text | 房间ID
data.rooms.1 | 五楼天井区 | Text | 房间名
data.rooms.2 | 1 | Text | 所属图书馆ID
data.rooms.3 | 5 | Text | 所在楼层
data.hours | 4 | Text | 默认允许预约时长
data.dates | 2021-11-26 | Text | 日期
message | - | Text | 返回信息
code | 0 | Text | 错误码
## /图书馆座位管理接口/获取房间信息
```text
暂无描述
```
#### 接口状态
> 开发中

#### 接口URL
> http://seatlib.hpu.edu.cn/rest/v2/room/stats2/:date?token=B5IQ0U721T11262738

#### 请求方式
> GET

#### Content-Type
> form-data

#### 请求Query参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
token | B5IQ0U721T11262738 | Text | 是 | -
#### 路径变量
参数名 | 示例值 | 参数描述
--- | --- | ---
date | 2021-11-28 | 
#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
token | GBZU8G587G11282250 | Text | 是 | -
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"status": "success",
	"data": [
		{
			"roomId": 29,
			"room": "1层自主学习空间（Ⅰ）",
			"floor": 1,
			"maxHour": -1,
			"totalSeats": 164,
			"free": 0,
			"reserved": 0,
			"inUse": 0,
			"away": 0
		},
		{
			"roomId": 12,
			"room": "一层大厅",
			"floor": 1,
			"maxHour": -1,
			"totalSeats": 169,
			"free": 0,
			"reserved": 0,
			"inUse": 0,
			"away": 0
		},
		{
			"roomId": 8,
			"room": "一楼自习区",
			"floor": 1,
			"maxHour": 4,
			"totalSeats": 156,
			"free": 0,
			"reserved": 0,
			"inUse": 0,
			"away": 0
		},
		{
			"roomId": 7,
			"room": "负一楼自习区",
			"floor": 1,
			"maxHour": 4,
			"totalSeats": 204,
			"free": 0,
			"reserved": 0,
			"inUse": 0,
			"away": 0
		},
		{
			"roomId": 33,
			"room": "2层报刊阅览区",
			"floor": 2,
			"maxHour": -1,
			"totalSeats": 74,
			"free": 0,
			"reserved": 0,
			"inUse": 0,
			"away": 0
		},
		{
			"roomId": 11,
			"room": "朗读亭",
			"floor": 2,
			"maxHour": 1,
			"totalSeats": 1,
			"free": 0,
			"reserved": 0,
			"inUse": 0,
			"away": 0
		},
		{
			"roomId": 30,
			"room": "3层自主学习空间（Ⅱ）",
			"floor": 3,
			"maxHour": -1,
			"totalSeats": 266,
			"free": 0,
			"reserved": 0,
			"inUse": 0,
			"away": 0
		},
		{
			"roomId": 32,
			"room": "3层自主学习空间（Ⅲ）",
			"floor": 3,
			"maxHour": -1,
			"totalSeats": 80,
			"free": 0,
			"reserved": 0,
			"inUse": 0,
			"away": 0
		},
		{
			"roomId": 3,
			"room": "三楼天井区",
			"floor": 3,
			"maxHour": -1,
			"totalSeats": 40,
			"free": 0,
			"reserved": 0,
			"inUse": 0,
			"away": 0
		},
		{
			"roomId": 9,
			"room": "三楼自习区A",
			"floor": 3,
			"maxHour": 4,
			"totalSeats": 240,
			"free": 0,
			"reserved": 0,
			"inUse": 0,
			"away": 0
		},
		{
			"roomId": 10,
			"room": "三楼自习区B",
			"floor": 3,
			"maxHour": 4,
			"totalSeats": 240,
			"free": 0,
			"reserved": 0,
			"inUse": 0,
			"away": 0
		},
		{
			"roomId": 15,
			"room": "4层工程技术类借阅区",
			"floor": 4,
			"maxHour": -1,
			"totalSeats": 68,
			"free": 0,
			"reserved": 0,
			"inUse": 0,
			"away": 0
		},
		{
			"roomId": 34,
			"room": "4层计算机类借阅区",
			"floor": 4,
			"maxHour": -1,
			"totalSeats": 266,
			"free": 0,
			"reserved": 0,
			"inUse": 0,
			"away": 0
		},
		{
			"roomId": 4,
			"room": "四楼天井区",
			"floor": 4,
			"maxHour": -1,
			"totalSeats": 40,
			"free": 0,
			"reserved": 0,
			"inUse": 0,
			"away": 0
		},
		{
			"roomId": 17,
			"room": "5层工程技术类借阅区",
			"floor": 5,
			"maxHour": -1,
			"totalSeats": 128,
			"free": 0,
			"reserved": 0,
			"inUse": 0,
			"away": 0
		},
		{
			"roomId": 19,
			"room": "5层自然科学借阅区",
			"floor": 5,
			"maxHour": -1,
			"totalSeats": 68,
			"free": 0,
			"reserved": 0,
			"inUse": 0,
			"away": 0
		},
		{
			"roomId": 1,
			"room": "五楼天井区",
			"floor": 5,
			"maxHour": -1,
			"totalSeats": 80,
			"free": 0,
			"reserved": 0,
			"inUse": 0,
			"away": 0
		},
		{
			"roomId": 2,
			"room": "五楼自习区",
			"floor": 5,
			"maxHour": -1,
			"totalSeats": 256,
			"free": 0,
			"reserved": 0,
			"inUse": 0,
			"away": 0
		},
		{
			"roomId": 23,
			"room": "6层社会科学借阅区（Ⅰ）",
			"floor": 6,
			"maxHour": -1,
			"totalSeats": 68,
			"free": 0,
			"reserved": 0,
			"inUse": 0,
			"away": 0
		},
		{
			"roomId": 35,
			"room": "6层社会科学类借阅区(Ⅱ)",
			"floor": 6,
			"maxHour": -1,
			"totalSeats": 266,
			"free": 0,
			"reserved": 0,
			"inUse": 0,
			"away": 0
		},
		{
			"roomId": 5,
			"room": "六楼自习区",
			"floor": 6,
			"maxHour": -1,
			"totalSeats": 312,
			"free": 0,
			"reserved": 0,
			"inUse": 0,
			"away": 0
		},
		{
			"roomId": 26,
			"room": "7层社会科学类借阅区1",
			"floor": 7,
			"maxHour": -1,
			"totalSeats": 174,
			"free": 0,
			"reserved": 0,
			"inUse": 0,
			"away": 0
		},
		{
			"roomId": 25,
			"room": "7层社会科学类借阅区2",
			"floor": 7,
			"maxHour": -1,
			"totalSeats": 116,
			"free": 0,
			"reserved": 0,
			"inUse": 0,
			"away": 0
		},
		{
			"roomId": 28,
			"room": "7层自主学习空间（V）",
			"floor": 7,
			"maxHour": -1,
			"totalSeats": 64,
			"free": 0,
			"reserved": 0,
			"inUse": 0,
			"away": 0
		},
		{
			"roomId": 31,
			"room": "7层自主学习空间（Ⅳ）",
			"floor": 7,
			"maxHour": -1,
			"totalSeats": 336,
			"free": 0,
			"reserved": 0,
			"inUse": 0,
			"away": 0
		}
	],
	"message": "",
	"code": "0"
}
```
参数名 | 示例值 | 参数类型 | 参数描述
--- | --- | --- | ---
status | success | Text | 返回状态
data | - | Text | 返回数据
data.roomId | 29 | Text | 房间ID
data.room | 1层自主学习空间（Ⅰ） | Text | 房间名
data.floor | 1 | Text | 房间楼层
data.maxHour | -1 | Text | 允许预约时长(-1未开放)
data.totalSeats | 164 | Text | 座位总数
data.free | 0 | Text | 空闲座位数
data.reserved | 0 | Text | 被预约的座位数
data.inUse | 0 | Text | 正在使用的座位数
data.away | 0 | Text | 暂离座位数
message | - | Text | 返回信息
code | 0 | Text | 错误码
## /图书馆座位管理接口/获取房间布局
```text
暂无描述
```
#### 接口状态
> 开发中

#### 接口URL
> http://seatlib.hpu.edu.cn/rest/v2/room/layoutByDate/:room_id/:date?token=JS7DRH2LGW12054702

#### 请求方式
> GET

#### Content-Type
> form-data

#### 请求Query参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
token | JS7DRH2LGW12054702 | Text | 是 | -
#### 路径变量
参数名 | 示例值 | 参数描述
--- | --- | ---
room_id | 25 | 房间ID

date | 2021-12-05 | 日期
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /图书馆座位管理接口/获取座位的空闲开始时间
```text
暂无描述
```
#### 接口状态
> 开发中

#### 接口URL
> http://seatlib.hpu.edu.cn/rest/v2/startTimesForSeat/:seat_id/:date?token=NZSVGRI4X912054659

#### 请求方式
> GET

#### Content-Type
> form-data

#### 请求Query参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
token | NZSVGRI4X912054659 | Text | 是 | -
#### 路径变量
参数名 | 示例值 | 参数描述
--- | --- | ---
seat_id | 8964 | 座位ID
date | 2021-12-05 | 日期
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /图书馆座位管理接口/获取座位的空闲结束时间
```text
暂无描述
```
#### 接口状态
> 开发中

#### 接口URL
> http://seatlib.hpu.edu.cn/rest/v2/endTimesForSeat/:seat_id/:date/:start_time?token=NZSVGRI4X912054659

#### 请求方式
> GET

#### Content-Type
> form-data

#### 请求Query参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
token | NZSVGRI4X912054659 | Text | 是 | -
#### 路径变量
参数名 | 示例值 | 参数描述
--- | --- | ---
seat_id | 8964 | 
date | 2021-12-05 | 
start_time | now | 
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /图书馆座位管理接口/暂离
```text
暂无描述
```
#### 接口状态
> 开发中

#### 接口URL
> http://seatlib.hpu.edu.cn/rest/v2/leave?token=JGJVNZC3HM11243643

#### 请求方式
> GET

#### Content-Type
> form-data

#### 请求Query参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
token | JGJVNZC3HM11243643 | Text | 是 | -
#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
token | GBZU8G587G11282250 | Text | 是 | -
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"status": "success",
	"data": null,
	"message": "请于18时30分前返回",
	"code": "0"
}
```
#### 错误响应示例
```javascript
{
	"status": "fail",
	"data": null,
	"message": "请连接此场馆无线网或在触屏机上操作",
	"code": "1"
}
```
