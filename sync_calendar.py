import json
import os
import subprocess
from datetime import datetime

# Project paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    events = [
        {
            "summary": "NVIDIA GTC 2026 Keynote (Jensen Huang)",
            "start": "2026-03-17 02:00:00",
            "end": "2026-03-17 04:00:00",
            "description": "NVIDIA 官网官宣。链接：https://www.nvidia.com/en-us/gtc/keynote/ (北京时间 3/17 凌晨 2点)"
        },
        {
            "summary": "荣耀 Magic V6 新机发布会",
            "start": "2026-03-10 14:30:00",
            "end": "2026-03-10 16:30:00",
            "description": "荣耀官网官宣。链接：https://www.honor.com/cn/news/"
        },
        {
            "summary": "Oppo Find N6 全球发布会 (预计)",
            "start": "2026-03-17 14:30:00",
            "end": "2026-03-17 16:30:00",
            "description": "来源：小红书/数码博主汇总。链接：http://xhslink.com/o/46FRbbwM999"
        },
        {
            "summary": "华为春季新品发布会 (博主爆料)",
            "start": "2026-03-20 14:30:00",
            "end": "2026-03-20 17:00:00",
            "description": "来源：小红书 @小苏数码速报。链接：http://xhslink.com/o/4pLrsmcp5z9"
        },
        {
            "summary": "Vivo X300 Ultra/X300s 发布会 (预计)",
            "start": "2026-03-22 14:30:00",
            "end": "2026-03-22 16:30:00",
            "description": "新机发布会，避开华为锋芒，日期小幅调整预估。"
        },
        {
            "summary": "iQOO Z11 系列发布 (预计)",
            "start": "2026-03-27 14:00:00",
            "end": "2026-03-27 16:00:00",
            "description": "新机发布会，具体日期以官宣为准。"
        },
        {
            "summary": "Microsoft GDC 2026 Keynote",
            "start": "2026-03-18 10:00:00",
            "end": "2026-03-18 12:00:00",
            "description": "Building for the Future with Xbox. Focus on next-gen hardware/handheld hints."
        },
        {
            "summary": "Google I/O 2026 (预计)",
            "start": "2026-05-12 10:00:00",
            "end": "2026-05-12 13:00:00",
            "description": "Google 年度开发者大会，重点关注 Android 17 和 AI 进展。"
        },
        {
            "summary": "Apple WWDC 2026 (预计)",
            "start": "2026-06-08 10:00:00",
            "end": "2026-06-08 13:00:00",
            "description": "Apple 年度开发者大会，iOS 20, macOS Tahoe 首秀。"
        },
        {
            "summary": "NVIDIA Q1 FY2027 Financial Results Call",
            "start": "2026-05-20 14:00:00",
            "end": "2026-05-20 16:00:00",
            "description": "NVIDIA will host a conference call on Wednesday, May 20, at 2 p.m. PT to discuss its financial results."
        },
        {
            "summary": "Nintendo Yoshi's Incredible Encyclopedia Launch (Switch 2)",
            "start": "2026-05-21 00:00:00",
            "end": "2026-05-21 23:59:59",
            "description": "任天堂 Switch 2 游戏《耀西与不可思议的图鉴》5 月 21 日发售。"
        },
        {
            "summary": "The Mandalorian and Grogu Movie Release",
            "start": "2026-05-22 00:00:00",
            "end": "2026-05-22 23:59:59",
            "description": "Star Wars movie hitting theaters."
        },
        {
            "summary": "vivo S60 系列新机发布会",
            "start": "2026-05-29 14:30:00",
            "end": "2026-05-29 16:30:00",
            "description": "vivo S60 系列新机首发亮相：田曦薇代言，5 月 29 日发布。"
        },
        {
            "summary": "Apple WWDC 2026",
            "start": "2026-06-09 01:00:00",
            "end": "2026-06-09 04:00:00",
            "description": "Apple 官宣北京时间 6 月 9 日凌晨 1 点举办 WWDC26 活动，公布 iOS 27 等动向。"
        },
        {
            "summary": "华为 nova 16 系列 & MatePad Pro Max 发布会",
            "start": "2026-06-01 14:30:00",
            "end": "2026-06-01 16:30:00",
            "description": "华为官宣定档 6 月 1 日发布 nova 16 系列及 MatePad Pro Max。"
        },
        {
            "summary": "比亚迪宋 Ultra DM-i & 迪迪虾发布",
            "start": "2026-05-28 19:30:00",
            "end": "2026-05-28 21:30:00",
            "description": "比亚迪宋 Ultra DM-i 正式上市，同步发布自研 4nm 智驾芯片璇玑 A3 及超级智能体“迪迪虾”。"
        },
        {
            "summary": "小米 17T/Pro 海外发布会",
            "start": "2026-05-28 21:00:00",
            "end": "2026-05-28 23:00:00",
            "description": "小米 17T / 17T Pro 海外正式发布，配备 7000mAh 超大电池。"
        },
        {
            "summary": "华为 3D 影像壁纸上线 (预计)",
            "start": "2026-06-15 10:00:00",
            "end": "2026-06-15 11:00:00",
            "description": "华为 Mate 80、Pura 80 等系列机型确认适配 3D 影像壁纸，预计 6 月支持。"
        },
        {
            "summary": "一加 15T 新机发布会 (预计)",
            "start": "2026-03-31 14:30:00",
            "end": "2026-03-31 16:30:00",
            "description": "新机发布会，具体日期以官宣为准。"
        },
        {
            "summary": "大疆 Osmo Pocket 4 系列发布会",
            "start": "2026-04-16 20:00:00",
            "end": "2026-04-16 22:00:00",
            "description": "大疆官网官宣。链接：https://www.ithome.com/0/938/743.htm"
        },
        {
            "summary": "OPPO Pad 5 Pro 全球首发",
            "start": "2026-04-21 19:00:00",
            "end": "2026-04-21 21:00:00",
            "description": "OPPO 官网官宣。链接：https://www.ithome.com/0/938/733.htm"
        },
        {
            "summary": "《坦克世界：HEAT》游戏发售",
            "start": "2026-05-26 10:00:00",
            "end": "2026-05-26 12:00:00",
            "description": "登录 PS5、Xbox、Steam，支持中文。链接：https://www.ithome.com/0/952/693.htm"
        },
        {
            "summary": "荣耀 600 系列手机发布会",
            "start": "2026-05-28 14:30:00",
            "end": "2026-05-28 16:30:00",
            "description": "荣耀 600 系列手机官宣搭载“教科书级”护眼屏，支持行业独家纸质全彩模式。链接：https://www.ithome.com/0/953/372.htm"
        },
        {
            "summary": "神舟二十三号发射 (预定)",
            "start": "2026-05-24 23:08:00",
            "end": "2026-05-25 01:00:00",
            "description": "神舟二十三号瞄准 5 月 24 日 23:08 发射。链接：https://www.ithome.com/0/954/464.htm"
        },
        {
            "summary": "OPPO Pad 6 平板发布会",
            "start": "2026-05-25 14:30:00",
            "end": "2026-05-25 16:30:00",
            "description": "OPPO Pad 6 平板规格公布：天玑 9500s 旗舰芯、10420mAh 电池，5 月 25 日发布。链接：https://www.ithome.com/0/954/176.htm"
        },
        {
            "summary": "中兴 G5 Pro 5G 移动路由器开售",
            "start": "2026-05-28 10:00:00",
            "end": "2026-05-28 12:00:00",
            "description": "2099 元，中兴 G5 Pro 高性能版 5G 移动路由器 CPE 将于 5 月 28 日开售。链接：https://www.ithome.com/0/954/221.htm"
        },
        {
            "summary": "荣耀 WIN Turbo 系列手机发布会",
            "start": "2026-05-29 14:30:00",
            "end": "2026-05-29 16:30:00",
            "description": "荣耀 WIN Turbo 系列手机官图发布：「快开黑」/「不怕蓝」/「指定赢」三色，5 月 29 日发布。链接：https://www.ithome.com/0/954/531.htm"
        },
        {
            "summary": "东风奕派 M8 登陆粤港澳大湾区车展",
            "start": "2026-05-29 10:00:00",
            "end": "2026-05-29 18:00:00",
            "description": "东风奕派 M8 将登陆 5 月 29 日粤港澳大湾区车展，搭载华为乾崑技术。链接：https://www.ithome.com/0/954/573.htm"
        },
        {
            "summary": "2026 台北电脑展 (COMPUTEX)",
            "start": "2026-06-02 09:00:00",
            "end": "2026-06-05 18:00:00",
            "description": "黄仁勋、苏姿丰已抵达台北，备战 2026 台北电脑展。链接：https://www.ithome.com/0/954/624.htm"
        },
        {
            "summary": "沃尔沃全新 ES90/EX90 上市",
            "start": "2026-05-29 10:00:00",
            "end": "2026-05-29 12:00:00",
            "description": "沃尔沃全新 ES90/EX90 车型 5 月 29 日上市，预售 42.99 万起。链接：https://www.ithome.com/0/954/892.htm"
        },
        {
            "summary": "酷态科电能仓 600 发布 (预计)",
            "start": "2026-05-29 14:00:00",
            "end": "2026-05-29 16:00:00",
            "description": "酷态科电能仓 600 参数曝光：输出功率 1013W MAX，有望 5 月 29 日发布。链接：https://www.ithome.com/0/954/800.htm"
        },
        {
            "summary": "《阿凡达 3》网播上线",
            "start": "2026-05-29 00:00:00",
            "end": "2026-05-29 23:59:59",
            "description": "科幻大片《阿凡达 3》网播定档 5 月 29 日，全球票房超 14.84 亿美元。链接：https://www.ithome.com/0/954/782.htm"
        }
    ]
    
    # Export to ICS
    ics_content = "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//Charles//Tech Calendar//EN\n"
    for event in events:
        dt_start = datetime.strptime(event["start"], "%Y-%m-%d %H:%M:%S").strftime("%Y%m%dT%H%M%S")
        dt_end = datetime.strptime(event["end"], "%Y-%m-%d %H:%M:%S").strftime("%Y%m%dT%H%M%S")
        ics_content += "BEGIN:VEVENT\n"
        ics_content += f"SUMMARY:{event['summary']}\n"
        ics_content += f"DTSTART:{dt_start}\n"
        ics_content += f"DTEND:{dt_end}\n"
        ics_content += f"DESCRIPTION:{event['description']}\n"
        ics_content += "END:VEVENT\n"
    ics_content += "END:VCALENDAR"
    
    with open(os.path.join(BASE_DIR, "calendar.ics"), "w") as f:
        f.write(ics_content)
    print("Generated calendar.ics")

if __name__ == "__main__":
    main()
