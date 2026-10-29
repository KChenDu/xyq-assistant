#!/usr/bin/env bash
# 人物修炼消耗；供Agent参考并自行构造curl命令，变量赋值为示例。
# 参数 cultivation_type：1攻击、2防御、3法术、4抗法、5猎术。
# 参数 current_cultivation_lv：当前修炼等级，0～25。
# 参数 target_cultivation_lv：目标修炼等级，0～25，须大于当前等级。
# 返回原始JSON；status=ok且success=true表示业务成功，读取data。
# data：exp_sum：修炼经验；cash_sum：金钱（两）；min_role_grade：角色等级要求；need_bg：需要达到的帮贡；zc_sum：消耗资财。
cultivation_type=1
current_cultivation_lv=0
target_cultivation_lv=1

curl --silent --show-error --fail --max-time 30 --get \
  "https://xyqtransfer.webapp.163.com/api/get_expt_need_res_by_lv_range" \
  --data-urlencode "expt_type=$cultivation_type" \
  --data-urlencode "from_lv=$current_cultivation_lv" \
  --data-urlencode "to_lv=$target_cultivation_lv"
