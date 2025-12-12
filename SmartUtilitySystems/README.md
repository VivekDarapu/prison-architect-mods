# Smart Utility Systems Mod

## Overview

The Smart Utility Systems mod eliminates the tedious endgame wiring in Prison Architect by automatically connecting surveillance and facility infrastructure using intelligent server objects.

## Features

### 1. **Tele-Tap Server**
- **Purpose:** Automatically wires Phone Booths to available Phone Taps
- **Cost:** $1,500
- **Power Required:** Yes
- **Research Required:** Intelligence
- **Placement:** Security Room or Intelligence Office

**How it works:**
- Scans the map for all Phone Booths and Phone Taps
- Establishes 1:1 connections (One booth per tap for optimal surveillance)
- Warns with yellow icon if you have more phones than taps

### 2. **CCTV Matrix Switcher**
- **Purpose:** Automatically balances camera load across monitors (Max 8 cameras per monitor)
- **Cost:** $2,000
- **Power Required:** High Voltage (Significant power draw)
- **Research Required:** Surveillance
- **Placement:** Security Room

**How it works:**
- Scans for all CCTV Cameras and Monitors
- Distributes cameras evenly (#1-8 to Monitor A, #9-16 to Monitor B, etc.)
- Prevents monitor overload and blacked-out screens

### 3. **Checkpoint Sync Node**
- **Purpose:** Links Scanner Machines and Door Servos to monitoring systems
- **Cost:** $500
- **Power Required:** Yes
- **Research Required:** Deployment
- **Placement:** Near checkpoints or Delivery zones

**How it works:**
- **Mode A:** Auto-wires DoorServo objects to DoorControlSystem within 30-tile radius
- **Mode B:** Connects ScannerMachine (Belt Scanners) to Monitors for viewing
- **Auto-Repair:** Re-heals broken wires if objects are moved

## Installation

1. Extract the SmartUtilitySystems folder to your Prison Architect mods directory:
   - Windows: `C:\Users\[YourName]\AppData\Local\Introversion\Prison Architect\mods\`
   - macOS: `~/Library/Application Support/Introversion/Prison Architect/mods/`
   - Linux: `~/.local/share/Introversion/Prison Architect/mods/`

2. Folder structure should be:
   ```
   SmartUtilitySystems/
   ├── manifest.json
   └── data/
       ├── objects.txt
       └── scripts/
           ├── SmartCCTV.lua
           ├── SmartPhone.lua
           └── SmartSync.lua
   ```

3. Launch Prison Architect
4. Go to Extras > Mods and enable "Smart Utility Systems"
5. Restart game or load a new prison

## Usage

1. **Research** the required technologies:
   - Surveillance (for CCTV Matrix)
   - Intelligence (for Tele-Tap Server)
   - Deployment (for Checkpoint Sync Node)

2. **Build** your infrastructure:
   - Place Phone Booths and Phone Taps
   - Install CCTV Cameras and Monitors
   - Add Scanner Machines and Door Servos

3. **Deploy Smart Servers:**
   - Place the appropriate smart server object in its designated location
   - Provide power
   - The scripts automatically scan and wire connections every 30-60 game minutes

## How the Wiring Works

The mod doesn't use "wireless" technology. Instead, it automatically draws the red wires for you via LUA scripts. This ensures:
- Full compatibility with the Prison Architect engine
- Physical wires that players can see
- Same fog-of-war mechanics as manual wiring
- Automatic re-wiring if objects are repositioned

## Technical Details

- **Script Language:** Lua
- **Update Frequency:** 
  - CCTV Matrix: Every 60 in-game minutes
  - Phone Taps: Every 60 in-game minutes
  - Sync Node: Every 30 in-game minutes (higher priority for door systems)

- **Performance:** Optimized to minimize lag by:
  - Checking only nearby objects when appropriate
  - Running scans on intervals instead of every frame
  - Using efficient connection detection

## Version

**v1.0** - December 12, 2025
- Initial release
- 3 Smart Server objects
- Full auto-wiring functionality

## License

This mod is free to use, modify, and distribute in the Prison Architect modding community.

## Troubleshooting

**Q: The smart servers aren't connecting anything**
- A: Make sure you've researched the required technology
- A: Ensure the smart server is powered
- A: Wait 30-60 game minutes for the scan to complete

**Q: Why do I still need to build objects manually?**
- A: The mod only automates wiring. You still need to place Phone Booths, Cameras, Monitors, etc.

**Q: Can I use multiple smart servers?**
- A: Yes! You can place multiple servers to cover different sections of your prison

## Feedback & Suggestions

Feel free to report issues or suggest improvements in the mod repository!
