#!/usr/bin/env bash
# 经验换算角色等级；供Agent参考并自行构造curl命令，变量赋值为示例。
# 参数 current_character_lv：当前角色等级，1～175。
# 参数 available_character_exp：可用于升级的经验，非负整数；网页未设上限。
# 返回原始JSON；status=ok且success=true表示业务成功，读取data。
# data.new_grade：可达等级；data.left_exp：剩余经验。
current_character_lv=69
available_character_exp=10000000

curl --silent --show-error --fail --max-time 30 --get \
  "https://xyqtransfer.webapp.163.com/api/get_obj_grade_by_exp" \
  --data-urlencode "current_grade=$current_character_lv" \
  --data-urlencode "exp=$available_character_exp"
