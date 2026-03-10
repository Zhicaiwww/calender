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
            "summary": "NVIDIA GTC 2026 Keynote (Jensen Huang)",
            "start": "2026-03-16 09:00:00",
            "end": "2026-03-16 11:00:00",
            "description": "NVIDIA GTC San Jose 2026. Keynote at SAP Center."
        },
        {
            "summary": "Oppo Find N6 Global Launch",
            "start": "2026-03-17 14:00:00",
            "end": "2026-03-17 16:00:00",
            "description": "Global launch of Oppo flagship foldable Find N6."
        },
        {
            "summary": "Huawei Spring Launch 2026 (Expected)",
            "start": "2026-03-24 14:30:00",
            "end": "2026-03-24 17:00:00",
            "description": "Expected launch of Mate 80 series and new wearables. Date based on rumors."
        },
        {
            "summary": "NVIDIA GTC 2026 Special Panel",
            "start": "2026-03-18 12:30:00",
            "end": "2026-03-18 14:00:00",
            "description": "Open Models panel moderated by Jensen Huang."
        }
    ]
    
    for event in events:
        dt = datetime.strptime(event["start"], "%Y-%m-%d %H:%M:%S")
        dt_end = datetime.strptime(event["end"], "%Y-%m-%d %H:%M:%S")
        add_event_to_calendar(event["summary"], dt, dt_end, event["description"])

if __name__ == "__main__":
    main()
