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
