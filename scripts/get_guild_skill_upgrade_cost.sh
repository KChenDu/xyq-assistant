#!/usr/bin/env bash
# 帮派技能升级消耗；供Agent参考并自行构造curl命令，变量赋值为示例。
# 参数 guild_skill_identifier：技能ID及等级上限见下方注释。
# 参数 current_guild_skill_lv：当前技能等级，0～该技能上限。
# 参数 target_guild_skill_lv：目标技能等级，0～该技能上限，须大于当前等级。
# 技能ID（网页允许等级上限）：
# 201强身术、202冥想：140级；218灵石技巧：120级；230强壮、237神速：60级。
# 239风之感应、240雨之感应、241雪之感应：20级。
# 以下均160级：203暗器技巧、204打造技巧、205裁缝技巧、206中药医理、207炼金术、
# 208烹饪技巧、209追捕技巧、210逃离技巧、211养生之道、212健身术、
# 216巧匠之术、217熔炼技巧、231淬灵之术。
# 返回原始JSON；status=ok且success=true表示业务成功，读取data。
# data：exp_sum：经验；cash_sum：金钱（两）；req_bg：需要达到的帮贡；bg_sum：实际消耗帮贡。
guild_skill_identifier=201
current_guild_skill_lv=0
target_guild_skill_lv=1

curl --silent --show-error --fail --max-time 30 --get \
  "https://xyqtransfer.webapp.163.com/api/get_life_skill_upgrade_need" \
  --data-urlencode "skill_id=$guild_skill_identifier" \
  --data-urlencode "from_lv=$current_guild_skill_lv" \
  --data-urlencode "to_lv=$target_guild_skill_lv"
