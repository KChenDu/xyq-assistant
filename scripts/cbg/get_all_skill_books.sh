#!/usr/bin/env bash
# 藏宝阁当前服务器的兽诀分类列表；Agent 参考构造 curl，不直接运行本文件。
# cookie_file：本机有效的 Netscape Cookie 文件，登录方式见 get_cbg_login_cookie.sh。
# server_id：服务器编号；kindid=26 为魔兽要诀，包含普通、高级、超级兽诀。
# page 从 1 开始；result_count 已验证 5、15，接口最大值未确认。
# pass_fair_show=1 排除公示期。
# 默认按价格从低到高查看，构造请求时直接使用 query_order=price ASC，无需询问排序方式。
# 先检查 status=1 / status_code=OK，再读 equip_list；HTTP 200 不代表业务成功。
# status=2 / SESSION_TIMEOUT 表示需重新登录；3=验证码、4=密保、5=OTP，交由用户处理。
# price 单位为人民币分；商品字段与详情链接见 get_skill_book_prices.sh。
# total_pages 为接口返回的分页范围，不据此推算精确商品总数。
# 分类第一页不是每种兽诀各自的最低价表；需要逐种价格时按完整技能名分别查询。

curl --fail --silent --show-error --max-time 30 --get \
  'https://xyq.cbg.163.com/cgi-bin/recommend.py' \
  --cookie "$cookie_file" --cookie-jar "$cookie_file" \
  --data-urlencode 'act=recommd_by_role' \
  --data-urlencode "server_id=$server_id" \
  --data-urlencode 'kindid=26' \
  --data-urlencode 'pass_fair_show=1' \
  --data-urlencode 'query_order=price ASC' \
  --data-urlencode "page=$page" \
  --data-urlencode "count=$result_count"
