#!/usr/bin/env bash
# 师门技能升级消耗；供Agent参考并自行构造curl命令，变量赋值为示例。
# 参数 current_sect_skill_lv：当前师门技能等级，0～180。
# 参数 target_sect_skill_lv：目标师门技能等级，0～180，须大于当前等级。
# 返回原始JSON；status=ok且success=true表示业务成功，读取data。
# data：exp_sum：经验；cash_sum：金钱（两）。
current_sect_skill_lv=0
target_sect_skill_lv=1

curl --silent --show-error --fail --max-time 30 --get \
  "https://xyqtransfer.webapp.163.com/api/get_school_skill_upgrade_need" \
  --data-urlencode "from_lv=$current_sect_skill_lv" \
  --data-urlencode "to_lv=$target_sect_skill_lv"
