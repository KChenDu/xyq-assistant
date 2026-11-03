#!/usr/bin/env bash
# 藏宝阁指定兽诀价格；Agent 阅读后自行构造 curl，不直接运行本文件。
# cookie_file：本机有效的 Netscape Cookie 文件，登录方式见 get_cbg_login_cookie.sh。
# server_id：用户服务器编号，从官方服务器资料获取。
# skill_name：完整技能名，例如“高级必杀”；UTF-8 -> Base64 -> URL 编码。
# skill_book_types：普通/高级兽诀为 611,18521；超级兽诀为 56870。
# page：从 1 开始，上限以返回的 total_pages 为准。
# result_count：已验证 5、15；接口最大值未确认，不预设上限。
# pass_fair_show=1：排除公示期；省略则包含公示期，0 表示公示期。
# 默认按价格从低到高查看，构造请求时直接使用 query_order=price ASC，无需询问排序方式。
# 只查最低挂牌价时无需遍历全部页面。
# 先检查 status=1 / status_code=OK，再读 equip_list；HTTP 200 不代表业务成功。
# status=2 / SESSION_TIMEOUT 表示需重新登录；3=验证码、4=密保、5=OTP，交由用户处理。
# price 单位为人民币分（除以 100 得元）；price_desc 为元字符串。
# 校验 equip_name、serverid、server_name、pass_fair_show 是否符合查询条件。
# 详情链接：https://xyq.cbg.163.com/equip?s={serverid}&eid={eid}
# 挂牌价不是成交价；正常空列表与登录失败按业务状态区分。

skill_name_base64=$(printf '%s' "$skill_name" | base64 | tr -d '\r\n')

curl --fail --silent --show-error --max-time 30 --get \
  'https://xyq.cbg.163.com/cgi-bin/recommend.py' \
  --cookie "$cookie_file" --cookie-jar "$cookie_file" \
  --data-urlencode 'act=recommd_by_role' \
  --data-urlencode "server_id=$server_id" \
  --data-urlencode 'search_type=search_msyj_neidan' \
  --data-urlencode "s_type=$skill_book_types" \
  --data-urlencode "skill_name=$skill_name_base64" \
  --data-urlencode 'pass_fair_show=1' \
  --data-urlencode 'query_order=price ASC' \
  --data-urlencode "page=$page" \
  --data-urlencode "count=$result_count"
