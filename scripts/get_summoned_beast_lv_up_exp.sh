#!/usr/bin/env bash
# 召唤兽升级所需经验；供Agent参考并自行构造curl命令，变量赋值为示例。
# 参数 current_summoned_beast_lv：当前召唤兽等级，1～180。
# 参数 target_summoned_beast_lv：目标召唤兽等级，1～180，须大于当前等级。
# 返回原始JSON；status=ok且success=true表示业务成功，读取data。
# data.exp：所需经验；月华露数量需查询工具页面。
current_summoned_beast_lv=1
target_summoned_beast_lv=2

curl --silent --show-error --fail --max-time 30 --get \
  "https://xyqtransfer.webapp.163.com/api/get_pet_upgrade_need_exp" \
  --data-urlencode "from_lv=$current_summoned_beast_lv" \
  --data-urlencode "to_lv=$target_summoned_beast_lv"
