#!/usr/bin/env bash
# 藏宝阁扫码登录参考；Agent 按阶段构造 curl，不直接运行本文件。
# 参数 area_id、area_name、server_id、server_name：来自官方服务器资料，不能任意填写。
# 服务器资料：https://cbg-xyq.res.netease.com/js/server_list_data.js
# 参数 role_id：扫码后从角色选择页获取；多个角色且目标不明确时询问用户。
# Cookie 为 Netscape 格式；先用已有文件查询，只有缺失或失效时才进行以下登录步骤。
# curl 与浏览器会话独立；所有登录请求共用 cookie_file，并同时接收新 Cookie。
# 示例依赖 curl、jq；二维码使用 uv 临时提供 Python qrcode，不修改项目依赖。
# 认证响应、二维码、Cookie 均留在仓库外；不输出认证原文或 Cookie 值。

umask 077
session_directory="${XDG_CACHE_HOME:-$HOME/.cache}/xyq-assistant/cbg/$server_id"
mkdir -p "$session_directory"
chmod 700 "$session_directory"
cookie_file="$session_directory/cookies.txt"
# 保存此路径供后续查询复用；文件权限保持 0600。有效期未确认，按接口状态判断。

# 1. 初始化目标服务器会话；名称参数由 curl 进行 URL 编码。
curl --fail --silent --show-error --max-time 30 --location --max-redirs 5 --get \
  'https://xyq.cbg.163.com/cgi-bin/show_login.py' \
  --cookie "$cookie_file" --cookie-jar "$cookie_file" \
  --data-urlencode 'act=show_login' \
  --data-urlencode "area_id=$area_id" \
  --data-urlencode "area_name=$area_name" \
  --data-urlencode "server_id=$server_id" \
  --data-urlencode "server_name=$server_name" \
  --output "$session_directory/login.html"

# 2. 获取二维码：status=1 才继续；qrcode_json 是二维码原始内容，poll_url 是轮询地址。
curl --fail --silent --show-error --max-time 30 --request POST \
  'https://xyq.cbg.163.com/cgi-bin/get_login_qrcode.py' \
  --cookie "$cookie_file" --cookie-jar "$cookie_file" \
  --output "$session_directory/qrcode.json"

uv run --with 'qrcode[pil]' --no-project python - "$session_directory" <<'PY'
import json
import sys
from pathlib import Path
import qrcode

directory = Path(sys.argv[1])
response = json.loads((directory / "qrcode.json").read_text())
if str(response.get("status")) != "1":
    raise ValueError("二维码请求未成功，停止登录并检查业务状态")
qrcode.make(response["qrcode_json"]).save(directory / "qrcode.png")
PY
# 向用户展示本地 qrcode.png，请用户用网易大神将军令扫码并确认。

# 3. 按响应中的 poll_url 轮询；仅使用官方 HTTPS 地址，不自行拼接认证参数。
# 已验证地址：https://q.reg.163.com/services/ngxqrcodeauthstatus（参数由服务端返回）。
poll_url=$(jq --exit-status --raw-output '.poll_url' "$session_directory/qrcode.json")
curl --fail --silent --show-error --max-time 30 \
  "$poll_url" \
  --cookie "$cookie_file" --cookie-jar "$cookie_file" \
  --output "$session_directory/poll.json"
# 返回 retCode：200=已确认；408/409=等待，可间隔 2 秒再次轮询；404=过期，重新获取二维码。
# 其他状态停止并检查错误。响应可能是 JSONP，先去除回调包装再按 JSON 解析，不执行响应代码。
# 只有 retCode=200 才进入下一步，不以用户口头确认代替接口确认。

# 4. 完成扫码认证：status=1 时，msg 为角色选择页跳转地址。
curl --fail --silent --show-error --max-time 30 \
  'https://xyq.cbg.163.com/cgi-bin/login_check.py?act=qrcode_login' \
  --cookie "$cookie_file" --cookie-jar "$cookie_file" \
  --data-urlencode "server_id=$server_id" \
  --data-urlencode "server_name=$server_name" \
  --data-urlencode "area_id=$area_id" \
  --data-urlencode "area_name=$area_name" \
  --output "$session_directory/login-result.json"

# 先核对 status=1，再读取 msg；相对地址按藏宝阁站点解析，核对为官方跳转地址后再请求。
role_selection_url=$(jq --exit-status --raw-output '.msg' "$session_directory/login-result.json")
curl --fail --silent --show-error --max-time 30 --location --max-redirs 5 \
  "$role_selection_url" \
  --cookie "$cookie_file" --cookie-jar "$cookie_file" \
  --output "$session_directory/roles.html"
# 从角色页提取角色名称与 role_id（页面可能使用 GBK），确认目标角色后继续。

# 5. 选择角色并保存最终 Cookie；不把 HTTP 200 或跳转本身视为登录成功。
curl --fail --silent --show-error --max-time 30 --location --max-redirs 5 --get \
  'https://xyq.cbg.163.com/cgi-bin/login.py' \
  --cookie "$cookie_file" --cookie-jar "$cookie_file" \
  --data-urlencode 'act=chose_role' \
  --data-urlencode "roleid=$role_id" \
  --output "$session_directory/logged-in.html"
chmod 600 "$cookie_file"

# 6. 用同一 cookie_file 调用目标查询接口，status=1 / status_code=OK 才算可查询。
# 查询 status=2 / SESSION_TIMEOUT：重新扫码；3=验证码、4=密保、5=OTP，交由用户处理。
# 登录成功后删除不再需要的二维码和认证中间文件，仅保留私有 Cookie 文件供后续使用。
