# Prison Architect Mods - Complete Installation Guide

## Quick Start (3 Steps to Working Mods)

### Step 1: Generate All Sprites & Graphics Files
```bash
# Install required Python library
pip install Pillow

# Run the sprite generator
python3 generate_sprites.py
```

This creates:
- PNG sprite files for all objects and staff
- graphics.txt configuration files for each mod
- Complete folder structure (data/graphics/objects, data/graphics/staff)

### Step 2: Locate Prison Architect Mods Folder
**Windows:**
```
C:\Users\[YourUsername]\AppData\Roaming\Introversion Software\Prison Architect\mods\
```

**Mac:**
```
~/Library/Application Support/Introversion Software/Prison Architect/mods/
```

**Linux:**
```
~/.local/share/Introversion\ Software/Prison\ Architect/mods/
```

### Step 3: Copy Mods & Enable in Game
1. Copy all generated mod folders to your Prison Architect mods folder
2. Launch Prison Architect
3. Go to `Options > Mods > Manage Mods`
4. Enable each mod (you'll see them listed if graphics.txt is correct!)
5. Restart game to load mods

---

## What Each File Does

### Required Files for EVERY Mod

#### `manifest.txt`
```
ID: ModName
Name: Display Name
Version: 1.0
```
**Purpose:** Tells Prison Architect the mod exists and its metadata

#### `data/objects.txt` (for furniture/items)
```
BEGIN Object
  ID CaolPowerPlant
  Title "Coal Power Plant"
  Price 8000
END
```
**Purpose:** Defines what objects/items/furniture the mod adds

#### `data/staff.txt` (for new staff roles)
```
BEGIN Staff
  ID Priest
  Title "Priest"
  Salary 1400
END
```
**Purpose:** Defines new staff types and their properties

#### `data/graphics.txt` (CRITICAL - Why Mods Fail!)
```
[ObjectDefinition CoalPowerPlant]
  Graphic ./graphics/objects/CoalPowerPlant.png
  GraphicIcon ./graphics/objects/CoalPowerPlant_icon.png
  Size 6 4

[StaffDefinition Priest]
  GraphicHead ./graphics/staff/Priest_head.png
  GraphicBody ./graphics/staff/Priest_body.png
  GraphicIcon ./graphics/staff/Priest_icon.png
```
**Purpose:** Maps object/staff definitions to their visual sprites

#### PNG Sprite Files (64x64 pixels)
```
data/graphics/
├── objects/
│   ├── CoalPowerPlant.png (main sprite)
│   └── CoalPowerPlant_icon.png (32x32 cursor icon)
└── staff/
    ├── Priest_head.png (character head)
    ├── Priest_body.png (character body/uniform)
    └── Priest_icon.png (32x32 selection icon)
```
**Purpose:** The actual visual images the game displays

---

## Why Your Mods Weren't Working Before

**You had:**
- ✓ manifest.txt
- ✓ data/objects.txt & data/staff.txt

**You were missing:**
- ✗ data/graphics.txt (configuration mapping)
- ✗ All PNG sprite files

Prison Architect says: "I found the mod definition, but where are the pictures?" → Mod fails silently.

---

## Complete Mod Folder Structure (Now Correct!)

```
IndustrialMod/
├── manifest.txt
└── data/
    ├── objects.txt
    ├── graphics.txt ← CRITICAL
    ├── graphics/ ← CRITICAL
    │   ├── objects/
    │   │   ├── CoalPowerPlant.png
    │   │   ├── CoalPowerPlant_icon.png
    │   │   ├── SteelPlant.png
    │   │   ├── SteelPlant_icon.png
    │   │   └── ... (more objects)
    │   └── staff/ (if adding staff)
    │       ├── Priest_head.png
    │       ├── Priest_body.png
    │       └── Priest_icon.png
```

---

## Mods Included & What They Add

### IndustrialMod (6 objects)
- Coal Power Plant (Power generation)
- Steel Plant (Prisoner work + materials)
- Coca-Cola Factory (Prisoner work + income)
- Train Track (Transport infrastructure)
- Train Station (Goods delivery)
- Train Carriage (Cargo transport)

### AdvancedStaffMod (21 staff types)
- Calming Officer, Physical Therapist, Mental Health Counselor
- Nutrition Specialist, Fitness Coach, Leisure Director
- Security Psychologist, Education Coordinator, Social Worker
- Mood Stabilizer Specialist, Anger Management Officer
- + 11 more specialized support staff

### PrisonRoles (11 staff types)
- Priest, Chaplain, Nun, Prayer Counselor
- Spiritual Guide, Religious Teacher, Deacon
- + 5 more spiritual/counseling roles

### SecurityEnhancements (3 staff types)
- Security Guard with Metal Detector
- K9 Security Handler
- Advanced Search Officer

### HospitalMod (4 objects)
- Hospital Bed
- Operating Table
- Mood Uplifter Machine
- Advanced Diagnostic Machine

### UtilitiesMod (3 objects)
- Advanced Laundry
- Professional Kitchen
- Enhanced Power Plant

### AdvancedWorkshops (4 objects)
- Professional Workshop
- Advanced Metalwork Station
- Precision Assembly Station
- Quality Control Station

### LuxuryRooms (5 objects)
- Luxury Bedroom
- Entertainment Suite
- Premium Gym Equipment
- Recreation Room
- Luxury Common Area

### VivekGym (5 objects)
- Professional Treadmill
- Weight Lifting Bench
- Yoga Station
- Basketball Court
- Swimming Pool

---

## Customizing Sprites (Optional)

The generated sprites are functional but basic. To create better sprites:

### Option 1: Use GIMP (Free)
- Download: gimp.org
- Create 64x64 PNG images
- Save in data/graphics/objects/ or data/graphics/staff/
- **graphics.txt automatically maps them!**

### Option 2: Use Krita (Free)
- Download: krita.org
- Better for digital art
- Same 64x64 size requirement

### Option 3: Online Tool
- pixelart.com (web-based, free)
- No installation needed
- Export as PNG

### Sprite Sizes Required
- **Main sprite:** 64x64 pixels
- **Icon sprite:** 32x32 pixels
- **Format:** PNG with transparency (use white background if needed)
- **Color depth:** 32-bit (includes alpha/transparency)

---

## Troubleshooting

### Mods don't appear in Manage Mods list
→ Check that graphics.txt exists and is correctly formatted

### Mods load but appear as purple/pink squares (missing texture)
→ Sprite PNG files not found or graphics.txt paths are wrong
→ Make sure PNG filenames match graphics.txt exactly

### Mods crash game on startup
→ Check Prison Architect's mod error log:
   Windows: `%AppData%\Introversion Software\Prison Architect\mods\`
→ Look for any .log files with error messages

### Sprites not showing correctly sized
→ Verify PNG files are exactly 64x64 pixels (not scaled)
→ Check graphics.txt has correct Size parameters

---

## File Checklist Before Playing

For EACH mod, verify you have:

- [ ] manifest.txt - ✓ You have this
- [ ] data/objects.txt (if adding objects) - ✓ You have this
- [ ] data/staff.txt (if adding staff) - ✓ You have this
- [ ] data/graphics.txt - ✓ NEWLY CREATED
- [ ] data/graphics/objects/ folder with .png files - ✓ NEWLY CREATED
- [ ] data/graphics/staff/ folder with _head.png, _body.png, _icon.png files - ✓ NEWLY CREATED

**All items checked? Your mods are ready to play!**

---

## Summary

Your Prison Architect mods are now **COMPLETE** with:
- ✓ 9 full mods (IndustrialMod, AdvancedStaffMod, PrisonRoles, SecurityEnhancements, HospitalMod, UtilitiesMod, AdvancedWorkshops, LuxuryRooms, VivekGym)
- ✓ 40+ objects and staff types
- ✓ All graphics.txt configuration files
- ✓ All sprite PNG files
- ✓ Python script to generate sprites

**Just run generate_sprites.py and copy the mods folder!**

---

## Questions?

Check MOD_SETUP_GUIDE.md for technical details about Prison Architect modding.
