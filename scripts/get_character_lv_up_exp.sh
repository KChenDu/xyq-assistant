#!/usr/bin/env bash
# 角色升级所需经验；供Agent参考并自行构造curl命令，变量赋值为示例。
# 参数 current_character_lv：当前角色等级，0～175。
# 参数 target_character_lv：目标角色等级，0～175，须大于当前等级。
# 返回原始JSON；status=ok且success=true表示业务成功，读取data。
# data.exp：所需经验。
current_character_lv=69
target_character_lv=70

curl --silent --show-error --fail --max-time 30 --get \
  "https://xyqtransfer.webapp.163.com/api/get_role_need_exp_to_grade" \
  --data-urlencode "from_grade=$current_character_lv" \
  --data-urlencode "to_grade=$target_character_lv"
