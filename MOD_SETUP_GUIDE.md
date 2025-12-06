# Prison Architect Mods - Complete Setup Guide

## Why Mods Aren't Working: Missing Components

Your mod definitions (objects.txt, staff.txt) are just **text files**. Prison Architect requires **3 key components** for each mod to work:

### 1. **MANIFEST FILE** ✓ (You Have This)
```
ID: ModName
Name: Display Name
Description: What it does
Version: 1.0
Includes: data/objects.txt, data/staff.txt
```

### 2. **DATA FILES** ✓ (Partially - You Have This)
- `data/objects.txt` - Furniture/structures definitions
- `data/staff.txt` - Staff roles definitions

**BUT:** These files reference graphics that don't exist yet!

### 3. **GRAPHICS FILES** ✗ (THIS IS MISSING!)
This is why your mods don't work. Each object/staff needs image files.

---

## What Graphics Are Needed

### File Structure Required:
```
YourMod/
├── manifest.txt
└── data/
    ├── objects.txt
    ├── staff.txt
    ├── graphics/
    │   ├── objects/
    │   │   ├── object_name.png (64x64 pixels)
    │   │   └── object_name_icon.png (32x32 pixels)
    │   ├── staff/
    │   │   ├── staff_role_head.png (64x64)
    │   │   ├── staff_role_body.png (64x64)
    │   │   └── staff_role_icon.png (32x32)
    │   └── graphics.txt (Configuration file!)
    └── lang/
        └── en.txt (Optional: text translations)
```

---

## CRITICAL: graphics.txt Configuration File

Every mod with graphics needs a `data/graphics.txt` file mapping objects to images:

```
[ObjectDefinition MyObject]
  Graphic ./object_name.png
  GraphicIcon ./object_name_icon.png
  Size 2x2

[StaffDefinition Chaplain]
  GraphicHead ./chaplain_head.png
  GraphicBody ./chaplain_body.png
  GraphicIcon ./chaplain_icon.png
```

---

## Minimum Image Requirements

### For Objects (64x64 PNG):
- Default state graphic
- Icon/cursor graphic (32x32)
- States for broken/working/lit (if applicable)

### For Staff (64x64 PNG):
- Head sprite (top half when visible)
- Body sprite (uniform)
- Icon for selection

---

## Current Mod Status & What's Missing

| Mod | Manifest | Data Files | graphics.txt | Sprites | Status |
|-----|----------|-----------|--------------|---------|--------|
| AdvancedStaffMod | ✓ | ✓ | ✗ | ✗ | 50% - Need graphics.txt + 21 staff sprites |
| AdvancedWorkshops | ✓ | ✓ | ✗ | ✗ | 50% - Need graphics.txt + sprites |
| HospitalMod | ✓ | ✓ | ✗ | ✗ | 50% - Need graphics.txt + room sprites |
| IndustrialMod | ✓ | ✓ | ✗ | ✗ | 50% - Need graphics.txt + 6 object sprites |
| LuxuryRooms | ✓ | ✗ | ✗ | ✗ | Need data files + graphics |
| PrisonRoles | ✓ | ✓ | ✗ | ✗ | 50% - Need graphics.txt + 11 staff sprites |
| SecurityEnhancements | ✓ | ✓ | ✗ | ✗ | 50% - Need graphics.txt + 3 staff + equipment sprites |
| UtilitiesMod | ✓ | ✓ | ✗ | ✗ | 50% - Need graphics.txt + sprites |
| VivekGym | ✓ | ✗ | ✗ | ✗ | Need data files + graphics |

---

## Quick Fix: How to Make Mods Work

### Step 1: Create graphics.txt for Each Mod
Add `ModName/data/graphics.txt` with object/staff mappings

### Step 2: Add Placeholder Sprites
For now, use simple colored rectangles (64x64 PNG):
- Coal Power Plant = Brown rectangle
- Staff roles = Colored person silhouettes
- Equipment = Simple shape icons

### Step 3: File Naming Convention
```
CoalPowerPlant.png → maps to ID: CoalPowerPlant in objects.txt
Priest.png → maps to ID: Priest in staff.txt
```

---

## Tools to Create Sprites

### Free Options:
1. **GIMP** - Free, full image editor
2. **Krita** - Free, designed for digital art
3. **Aseprite** - Free trial (Lua scripting for animations)
4. **Online Tool**: pixelart.com (web-based)
5. **ImageMagick** - Command-line sprite generation

### Quick Sprite Generation (Python):
```python
from PIL import Image
# Create 64x64 colored rectangle
img = Image.new('RGB', (64, 64), color='brown')
img.save('CoalPowerPlant.png')
```

---

## Next Steps to Fix Your Mods

1. **Create graphics.txt** for each mod (maps object names to PNG files)
2. **Create simple placeholder sprites** (64x64 PNGs) for each object/staff
3. **Organize in data/graphics/objects/** and **data/graphics/staff/** folders
4. **Test in Prison Architect** - Should recognize mods now
5. **Upgrade sprites** later with better graphics

---

## Example: Complete Working Mod Structure

```
IndustrialMod/
├── manifest.txt
└── data/
    ├── objects.txt (6 objects defined)
    ├── staff.txt (if needed)
    ├── graphics.txt (CRITICAL!)
    ├── graphics/
    │   ├── objects/
    │   │   ├── CoalPowerPlant.png
    │   │   ├── CoalPowerPlant_icon.png
    │   │   ├── SteelPlant.png
    │   │   ├── SteelPlant_icon.png
    │   │   ├── CocaColaFactory.png
    │   │   ├── CocaColaFactory_icon.png
    │   │   ├── TrainTrack.png
    │   │   ├── TrainTrack_icon.png
    │   │   ├── TrainStation.png
    │   │   ├── TrainStation_icon.png
    │   │   ├── TrainCarriage.png
    │   │   └── TrainCarriage_icon.png
```

---

## Debugging: If Mods Still Don't Load

Check Prison Architect's mod error log:
- Windows: `%AppData%/Introversion Software/Prison Architect/mods/`
- Look for error messages about missing graphics.txt or sprite references

---

## Summary

**Your mods fail because they're missing:**
1. **graphics.txt** - Configuration mapping objects to image files
2. **Sprite PNG files** - The actual graphics (64x64 pixels each)

Everything else is correctly structured. Once you add graphics.txt + sprites, your mods will work!

Would you like me to create graphics.txt files and placeholder sprite generation scripts for you?
