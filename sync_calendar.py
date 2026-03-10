import json
import os
import subprocess
from datetime import datetime

# Project paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "events.json")

def add_event_to_calendar(summary, dt, dt_end, description=""):
    """
    Adds an event to the local Apple Calendar using AppleScript.
    Calendar name: "发布会"
    """
    # Simplified AppleScript for maximum compatibility
    applescript = f'''
    set start_date to current date
    set month of start_date to {dt.month}
    set day of start_date to {dt.day}
    set year of start_date to {dt.year}
    set hours of start_date to {dt.hour}
    set minutes of start_date to {dt.minute}
    set seconds of start_date to {dt.second}

    set end_date to current date
    set month of end_date to {dt_end.month}
    set day of end_date to {dt_end.day}
    set year of end_date to {dt_end.year}
    set hours of end_date to {dt_end.hour}
    set minutes of end_date to {dt_end.minute}
    set seconds of end_date to {dt_end.second}

    tell application "Calendar"
        -- Force find the first iCloud account if possible, or just default to first account
        set theAccount to (first account whose name contains "iCloud")
        if not (exists calendar "发布会" of theAccount) then
            make new calendar at theAccount with properties {{name:"发布会"}}
        end if
        set targetCal to calendar "发布会" of theAccount
        
        tell targetCal
            make new event with properties {{summary:"{summary}", start date:start_date, end date:end_date, description:"{description}"}}
        end tell
    end tell
    '''
    try:
        subprocess.run(["osascript", "-e", applescript], check=True)
        print(f"Added to Calendar: {summary}")
    except subprocess.CalledProcessError:
        # Final fallback: just try any calendar named "发布会"
        fallback_script = f'''
        set start_date to current date
        set month of start_date to {dt.month}
        set day of start_date to {dt.day}
        set year of start_date to {dt.year}
        set hours of start_date to {dt.hour}
        set minutes of start_date to {dt.minute}
        set seconds of start_date to {dt.second}

        set end_date to current date
        set month of end_date to {dt_end.month}
        set day of end_date to {dt_end.day}
        set year of end_date to {dt_end.year}
        set hours of end_date to {dt_end.hour}
        set minutes of end_date to {dt_end.minute}
        set seconds of end_date to {dt_end.second}

        tell application "Calendar"
            if not (exists calendar "发布会") then
                make new calendar with properties {{name:"发布会"}}
            end if
            tell calendar "发布会"
                make new event with properties {{summary:"{summary}", start date:start_date, end date:end_date, description:"{description}"}}
            end tell
        end tell
        '''
        subprocess.run(["osascript", "-e", fallback_script])
        print(f"Fallback added to Calendar: {summary}")

def main():
    events = [
        {
            "summary": "荣耀 Magic V6 新机发布会",
            "start": "2026-03-10 14:30:00",
            "end": "2026-03-10 16:30:00",
            "description": "荣耀 Magic V6 新机发布会。"
        },
        {
            "summary": "NVIDIA GTC 2026 Keynote (Jensen Huang)",
            "start": "2026-03-17 02:00:00",
            "end": "2026-03-17 04:00:00",
            "description": "NVIDIA 官网官宣：March 16, 11 a.m. PT (北京时间 3/17 凌晨 2点)。地点：SAP Center。"
        },
        {
            "summary": "Oppo Find N6 全球发布会 (预计)",
            "start": "2026-03-17 14:30:00",
            "end": "2026-03-17 16:30:00",
            "description": "来源：小红书/数码博主汇总。注：OPPO 官方新闻稿尚未正式发布带日期的海报，标记为预计。"
        },
        {
            "summary": "华为春季新品发布会 (博主爆料)",
            "start": "2026-03-20 14:30:00",
            "end": "2026-03-20 17:00:00",
            "description": "来源：小红书 @小苏数码速报。核心看点：Mate 80 Air, 畅享 90。注：华为官网尚未上线该活动专题。"
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
            "summary": "一加 15T 新机发布会 (预计)",
            "start": "2026-03-31 14:30:00",
            "end": "2026-03-31 16:30:00",
            "description": "新机发布会，具体日期以官宣为准。"
        }
    ]
    
    for event in events:
        dt = datetime.strptime(event["start"], "%Y-%m-%d %H:%M:%S")
        dt_end = datetime.strptime(event["end"], "%Y-%m-%d %H:%M:%S")
        add_event_to_calendar(event["summary"], dt, dt_end, event["description"])

if __name__ == "__main__":
    main()
