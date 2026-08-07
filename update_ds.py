"""
update_ds.py — 여백 DS 단일 소스(yeobaek.py) 최신본을 GitHub 에서 이 폴더로 내려받아 갱신.

· 도구는 오프라인에서도 폴더 안의 yeobaek.py 로 그대로 동작한다.
· '업데이트할 때만' 인터넷이 필요하다. 실행 후 대시보드를 다시 실행하면 새 디자인이 반영된다.
· 이 파일과 yeobaek.py 는 각 도구 폴더에 함께 둔다(vendoring). 도구가 여러 개면 폴더마다 실행.

실행:  python update_ds.py       또는  DS업데이트.bat 더블클릭
"""
import os
import re
import ssl
import sys
import urllib.request

if sys.platform == "win32":              # 콘솔 UTF-8 (한글 깨짐 방지)
    try:
        import ctypes
        ctypes.windll.kernel32.SetConsoleOutputCP(65001)
    except Exception:
        pass
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

URL = "https://raw.githubusercontent.com/data2102/design-system/main/yeobaek.py"
HERE = os.path.dirname(os.path.abspath(__file__))
DST = os.path.join(HERE, "yeobaek.py")


def cur_version():
    if os.path.exists(DST):
        m = re.search(r'__version__\s*=\s*"([^"]+)"', open(DST, encoding="utf-8").read())
        return m.group(1) if m else "?"
    return "(없음)"


def main():
    print(f"● 현재 버전: {cur_version()}")
    print(f"● 내려받는 중… {URL}")
    ctx = ssl.create_default_context()
    ctx.check_hostname = False           # 사내망 TLS 검사 우회
    ctx.verify_mode = ssl.CERT_NONE
    try:
        req = urllib.request.Request(URL, headers={"User-Agent": "yeobaek-updater"})
        data = urllib.request.urlopen(req, context=ctx, timeout=30).read()
    except Exception as e:
        print(f"❌ 업데이트 실패 (인터넷/사내망 확인): {e}")
        print("   오프라인이면 기존 yeobaek.py 로 도구는 그대로 동작합니다.")
        return 1

    text = data.decode("utf-8", "replace")
    if "__version__" not in text or "TOKENS" not in text or "CSS =" not in text:
        print("❌ 받은 파일이 yeobaek.py 형식이 아닙니다 — 갱신을 중단합니다.")
        return 1

    with open(DST, "wb") as f:
        f.write(data)
    m = re.search(r'__version__\s*=\s*"([^"]+)"', text)
    print(f"✅ 갱신 완료 → v{m.group(1) if m else '?'}  ({len(data):,} bytes)")
    print("   이제 대시보드를 다시 실행하면 새 디자인이 반영됩니다.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
