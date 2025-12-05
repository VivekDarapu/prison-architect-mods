# Prison Architect Mods Collection

A complete collection of 5 Prison Architect mods ready to copy-paste directly into your game.
## 📦 Mods Included

### 1. **VivekGym** - Premium Fitness & Rehabilitation Equipment
- Treadmill (2x1, Cost: 1200)
- Weight Bench (2x2, Cost: 1500)
- Yoga Mat (1x1, Cost: 400)
- Resistance Bike (2x1, Cost: 1100)
- **Folder**: `VivekGym/`

### 2. **LuxuryRooms** - High-End Prison Facilities
- Marble Floor (1x1, Cost: 800)
- Crystal Chandelier (1x1, Cost: 1500)
- Luxury Bed (2x2, Cost: 2000)
- Premium Desk (2x1, Cost: 1200)
- **Folder**: `LuxuryRooms/`

### 3. **AdvancedWorkshops** - Professional Training Spaces
- Woodworking Bench (2x2, Cost: 1800)
- Electronics Station (2x2, Cost: 2500)
- Metalworking Forge (3x2, Cost: 3200)
- Textile Loom (2x3, Cost: 2000)
- **Folder**: `AdvancedWorkshops/`

### 4. **SecurityEnhancements** - Advanced Security Systems
- Facial Scanner (1x1, Cost: 2500)
- Motion Detector (1x1, Cost: 1500)
- Reinforced Door (1x2, Cost: 3500)
- Security Checkpoint (2x2, Cost: 4500)
- **Folder**: `SecurityEnhancements/`

- ### 5. **PrisonRoles** - Enhanced Staff & Prisoner Role System

- Bodyguard (High-risk protection, Cost: 2800)
- Military Police Officer (Tactical enforcement, Cost: 2600)
- Priest/Chaplain (Spiritual guidance, Salary: 1400)
- Counselor (Psychological support, Salary: 1300)
- Teacher (Education & development, Salary: 1500)
- Trade Instructor (Vocational training, Salary: 1600)
- Maintenance Inspector (Facility oversight, Salary: 1200)
- Electrician (Technical maintenance, Salary: 1800)
- IT Specialist (Tech infrastructure, Salary: 2000)
- Medical Officer (Healthcare oversight, Salary: 2200)
- Nurse (Patient care, Salary: 1100)
- Gang Leader (Prisoner influence, Special)
- Informant (Intelligence gathering, Special)
- Mentor/Reformer (Rehabilitation, Special)
- Maintenance Crew (Facility upkeep, Special)
- **Folder**: `PrisonRoles/`

## 🚀 Quick Start Installation

### Step 1: Find Your Prison Architect Mods Folder

**Windows:**
```
C:\Users\[YOUR_NAME]\AppData\Local\Introversion\Prison Architect\mods
```

**Mac:**
```
~/Library/Application Support/Introversion/Prison Architect/mods
```

**Linux:**
```
~/.local/share/Introversion/Prison Architect/mods
```

### Step 2: Copy Mod Folders

1. Clone or download this repository
2. Copy each mod folder (`VivekGym`, `LuxuryRooms`, `AdvancedWorkshops`, `SecurityEnhancements`) into your mods directory, `PrisonRoles`
3. Each mod is self-contained with all necessary files

### Step 3: Enable Mods in Game

1. Launch **Prison Architect**
2. Go to: **Extras → Mods**
3. Find each mod in the list (they appear with their mod names)
4. Check the boxes to enable all mods
5. Restart the game

### Step 4: Test Mods

1. Create a new **Sandbox Prison**
2. Open the **Quick Build** menu
3. New objects from enabled mods will appear in the appropriate categories
4. Start placing your custom objects!

## 📂 Folder Structure

Each mod follows this structure:

```
ModName/
├── manifest.txt           (Mod metadata)
├── data/
│   ├── objects.txt        (Object definitions)
│   ├── prefabs.txt        (Room layouts, if applicable)
│   ├── graphics/          (PNG sprites)
│   │   ├── object1.png
│   │   └── object2.png
│   └── scripts/           (Lua behavior scripts)
│       └── behavior.lua
```

## 🎮 What to Copy-Paste

Each mod folder in this repository contains:
- ✅ `manifest.txt` - Ready to use
- ✅ `data/objects.txt` - All object definitions
- ✅ `data/scripts/*.lua` - Behavioral logic (optional)
- ✅ `data/prefabs.txt` - Room layouts (if included)

**Simply copy the entire mod folder** to your Prison Architect `mods` directory!

## 📝 Key Files Reference

### manifest.txt Example
```
Name           "VivekGym Premium"
Author         "Vivek Darapu"
Description    "Fitness equipment for prisoner rehabilitation"
Version        "v1.0"
Date           "2025-12-06"
```

### objects.txt Example
```
BEGIN Object
    Name               VivekTreadmill
    Width              2
    Height             1
    Sprite             VivekTreadmillSprite
    Cost               1200
    ConstructionTime   20
END
```

## ⚙️ Troubleshooting

### Mods not appearing in Extras > Mods menu?
- ✓ Check `manifest.txt` syntax
- ✓ Verify folder is in correct location
- ✓ Ensure `manifest.txt` is at the root of mod folder

### Objects not showing in Quick Build?
- ✓ Verify `objects.txt` is in `data/` folder
- ✓ Check object names are spelled correctly
- ✓ Restart Prison Architect completely

### Need custom sprites?
- Create 64x64 PNG files with transparent backgrounds
- Place in `data/graphics/` folder
- Reference sprite name in `objects.txt`

## 📖 How to Customize

Each mod can be modified:

1. **Change costs**: Edit `Cost` values in `objects.txt`
2. **Adjust build times**: Modify `ConstructionTime` values
3. **Create presets**: Edit `prefabs.txt` to design room layouts
4. **Add behaviors**: Write custom Lua scripts in `data/scripts/`

## 🔗 Related Resources

- [Prison Architect Modding Wiki](https://prisonarchitect.paradoxwikis.com/Modding)
- [Steam Workshop Guides](https://steamcommunity.com/app/233360/guides/)
- [Official PA Modding Quickstart](https://prisonarchitect.paradoxwikis.com/Modding_Quickstart_Guide)

## ✨ Features

- ✅ AllAll 5 mods4 mods ready to copy-paste
- ✅ Complete manifest.txt configurations
- ✅ Detailed objects.txt with all properties
- ✅ Optional Lua behavior scripts
- ✅ Room layout prefabs included
- ✅ Installation instructions for all platforms
- ✅ Easy customization guide

## 📄 License

Free to use and modify. Share your improvements!

## 🎮 Enjoy!

Happy prison building! If you have questions about the mods, refer to the official Prison Architect modding documentation or customize the files to your liking.
