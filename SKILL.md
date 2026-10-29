---
name: xyq-assistant
description: 一个全能的梦幻西游游戏助手，负责游戏知识的解答、游戏经验计算、游戏内银两计算和给予游戏建议等等。
---

# 技能1：官方工具箱查询

信息获取顺序：[官方工具箱](https://xyq.163.com/tools/index.html) → 梦幻精灵（技能2）。先查询工具箱；未覆盖、信息不足、请求失败或需要核对时再询问GM。

## 1. API计算类

按需阅读对应`.sh`，并执行curl命令。

| 计算功能 | 对应`.sh` |
|---|---|
| 角色升级经验 | [get_character_lv_up_exp.sh](scripts/get_character_lv_up_exp.sh) |
| 经验换算角色等级 | [get_character_lv_from_exp.sh](scripts/get_character_lv_from_exp.sh) |
| 人物修炼消耗 | [get_character_cultivation_upgrade_cost.sh](scripts/get_character_cultivation_upgrade_cost.sh) |
| 师门技能升级消耗 | [get_sect_skill_upgrade_cost.sh](scripts/get_sect_skill_upgrade_cost.sh) |
| 帮派技能升级消耗 | [get_guild_skill_upgrade_cost.sh](scripts/get_guild_skill_upgrade_cost.sh) |
| 召唤兽升级经验 | [get_summoned_beast_lv_up_exp.sh](scripts/get_summoned_beast_lv_up_exp.sh) |

## 2. 前端展示类

按需打开以下链接查阅资料或使用页面本地计算。

| 页面功能 | 信息概述 |
|---|---|
| [人物常规计算](https://xyq.163.com/tools/index.html?menu=1&type=2) | 人物技能要求、携带金钱上限 |
| [转门派计算](https://xyq.163.com/tools/index.html?menu=1&type=4) | 转门派所需经验和潜能果 |
| [商会免税计算](https://xyq.163.com/tools/index.html?menu=1&type=5) | 商会免税需求卖出额 |
| [宝石合成规则](https://xyq.163.com/tools/index.html?menu=1&type=6) | 宝石工艺要求、高等级宝石及星辉石合成额外材料、时间锁说明 |
| [人物修炼乾元丹](https://xyq.163.com/tools/index.html?menu=1&type=7) | 按人物等级查询人物/召唤兽修炼上限、基础乾元丹上限；页面未计129/159级金乌额外丹，相关问题向GM补查 |
| [潜能果兑换经验](https://xyq.163.com/tools/index.html?menu=1&type=8) | 兑换潜能果所需经验 |
| [钟灵石](https://xyq.163.com/tools/index.html?menu=1&type=9) | 单件特效、套装效果及8/16/24/28/32级数值 |
| [三级药表](https://xyq.163.com/tools/index.html?menu=2&type=3) | 药品功效、品质相关恢复公式、配方及获取方式 |
| [家具配方](https://xyq.163.com/tools/index.html?menu=2&type=4) | 家具材料组合、制作金钱、活力、体力消耗 |
| [烹饪表](https://xyq.163.com/tools/index.html?menu=2&type=5) | 烹饪技能等级对应的食物 |
| [法宝大全](https://xyq.163.com/tools/index.html?menu=2&type=6) | 法宝类型、主动/被动、使用等级、门派限制、作用及使用效果 |
| [法宝吸收灵气地点](https://xyq.163.com/tools/index.html?menu=2&type=7) | 按法宝等级、境界层数查询吸收灵气场景 |
| [符石组合](https://xyq.163.com/tools/index.html?menu=2&type=8) | 颜色和顺序、门派限制、装备部位、组合效果 |
| [灵饰属性](https://xyq.163.com/tools/index.html?menu=2&type=9) | 不同等级、部位的基础及附加属性范围 |
| [乾元丹消耗计算](https://xyq.163.com/tools/index.html?menu=2&type=10) | 乾元丹经验和金钱消耗 |
| [装备特技](https://xyq.163.com/tools/index.html?menu=2&type=11) | 主动特技的愤怒消耗和效果、被动装备特效 |
| [神器大全](https://xyq.163.com/tools/index.html?menu=2&type=12) | 门派神器、流派、神器技能和效果 |
| [装备打造属性](https://xyq.163.com/tools/index.html?menu=2&type=13) | 0～160级各部位普通/强化打造属性范围 |
| [召唤兽大全](https://xyq.163.com/tools/index.html?menu=3&type=1) | 图片、等级、场景、资质、成长、寿命、携带技能及效果；神兽物理/法术技能 |
| [召唤兽技能](https://xyq.163.com/tools/index.html?menu=3&type=2) | 技能图标、名称和效果 |
| [召唤兽练级场景](https://xyq.163.com/tools/index.html?menu=3&type=3) | 场景适用等级及五人组队领双经验 |
| [召唤兽修炼计算](https://xyq.163.com/tools/index.html?menu=3&type=4) | 修炼经验、人物等级要求、100环次数 |
| [召唤兽升级计算](https://xyq.163.com/tools/index.html?menu=3&type=5) | 升级所需经验和月华露数量 |
| [召唤兽内丹](https://xyq.163.com/tools/index.html?menu=3&type=6) | 内丹名称和效果 |
| [变身卡大全](https://xyq.163.com/tools/index.html?menu=4&type=1) | 变化之术等级、附加技能和属性、战斗中使用要求 |
| [打传说地点](https://xyq.163.com/tools/index.html?menu=4&type=2) | 场景和适用出传说等级 |
| [牧场动物产出](https://xyq.163.com/tools/index.html?menu=4&type=3) | 动物的普通及特殊产出 |
| [牧场称谓](https://xyq.163.com/tools/index.html?menu=4&type=4) | 兑换积分、物品、称谓和时效 |
| [教师节·看图说话](https://xyq.163.com/tools/index.html?menu=5&type=0) | 技能图标和名称，含坐骑、辅助、剧情、门派等分类 |
| [教师节·谁是学霸](https://xyq.163.com/tools/index.html?menu=5&type=1) | 正确/错误题目和判断答案 |
| [元宵节题库](https://xyq.163.com/tools/index.html?menu=5&type=2) | 灯谜题目和答案 |
| [科举题库](https://xyq.163.com/tools/index.html?menu=5&type=3) | 页面收录的新增题目和答案 |


# 技能2：询问梦幻精灵（GM）

工具页面未覆盖问题、信息不足、请求失败或需要核对规则时，再询问游戏GM补充。不要将一次查询未命中视为该内容不存在。具体步骤：
1. 拆解用户的问题并提取问题内所有游戏名词
2. 询问GM对应名词的含义（请求形式可参考`scripts/gm_request.sh`）。如果GM的回复涉及新的名词知识，可以再次追问GM获取更多信息
3. 如有需要，调用后续其他技能帮助完成复杂计算
4. 回答用户问题


# 技能3：查询金价

如果用户询问当前金价，需要先反问用户所在的服务器名称，然后参考`scripts/get_rate3000.sh`查询该服务器的金价（`rate3000`，单位：元/3000万银两）。注意请求中的参数`flag`可取值1、2和3，对应服务器类型：
- 1：一年内
- 2：三年内
- 3：三年外

可以先询问用户的服务器是哪种类型，如果用户不清楚也可全部查询。


# 技能4：价格换算

梦幻西游这个游戏涉及了几个重要货币单位：银两（`tael`）、点卡（`point`）、元（`yuan`）、三界功绩（`merit`）、仙玉（`jade`）和储备金（`reserve`），它们之间可以互相转换。如果遇到转换相关的计算，需要先参考`scripts/price_converter.py`中对应的函数，然后按需询问用户当前的比例（`rate`，单位：元/万银两）或者点卡价格（`price`, 银两/点）（如果用户提供不了，可以调用技能3查询），最后调用函数计算。

**注意**：技能3查询到的`rate3000`单位是元/3000万银两，需要按需调用`scripts/price_converter.py`中的`rate30002rate`函数转换成元/万银两。


# 技能5：体力转换

梦幻西游中的体力（`stamina`）也可以转换成银两（`tael`）和储备金（`reserve`）。如果被用户询问体力的价值，可以参考`scripts/stamina_calculator.py`中对应的函数计算。


# 技能6：帮贡

待完善…


# 技能7：宝石

计算宝石数量（`n`）与合成所需体力（`stamina`）时，需要先询问用户该宝石的等级。计算宝石价格(`price`)时，需要先询问用户该宝石的等级，以及其对应的1级宝石价格是多少。然后调用`scripts/gem_calculator.py `中对应的函数计算宝石数量、价格和体力消耗。宝石一共有三种类型：
1. 普通宝石（gem）：光芒石、太阳石、月亮石、红宝石、黄宝石、蓝宝石、绿宝石、黑宝石、红玛瑙、舍利子、神秘石、翡翠石
2. 星辉石（star stone）
3. 五色灵尘（spirit dust）


# 技能8：附魔宝珠

如果用户询问了装备点化所需的附魔宝珠数量或价格，需先反问对方期望的点化类型为以下哪种：变身术、变化咒、法术追加、附加状态，以及装备当前的祈福值。然后可参考`scripts/orb_calculator.py`中对应的函数计算期望消耗。


# 技能9：赐福系统


