#!/bin/bash
#
# Prison Architect Mods - Automatic Setup Script
# Generates all sprites, creates graphics.txt, and copies mods to Prison Architect directory
# Run: bash SETUP.sh
#

set -e

echo "╔════════════════════════════════════════════════════════════╗"
echo "║   Prison Architect Mods - Automatic Setup                 ║"
echo "║   Sprite Generation & Installation Tool                   ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Step 1: Check and install dependencies
echo "[1/4] Checking Python & Pillow..."
if ! command -v python3 &> /dev/null; then
  echo "✗ Python3 not found. Please install Python 3.7 or higher"
  exit 1
fi

python3 -m pip install --quiet Pillow 2>/dev/null || {
  echo "Installing Pillow..."
  python3 -m pip install Pillow
}
echo "✓ Dependencies ready"
echo ""

# Step 2: Generate sprites
echo "[2/4] Generating sprite PNGs and graphics.txt files..."
python3 generate_sprites.py
echo "✓ All sprites generated successfully"
echo ""

# Step 3: Find Prison Architect mods directory
echo "[3/4] Locating Prison Architect mods directory..."

# Try common paths
if [[ "$OSTYPE" == "darwin"* ]]; then
  # macOS
  PA_MODS_DIR="$HOME/Library/Application Support/Prison Architect/mods"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
  # Linux
  PA_MODS_DIR="$HOME/.local/share/Introversion Software/Prison Architect/mods"
else
  # Windows (Git Bash / WSL)
  PA_MODS_DIR="$USERPROFILE/AppData/Local/Introversion Software/Prison Architect/mods"
fi

if [ ! -d "$PA_MODS_DIR" ]; then
  echo "✗ Could not find Prison Architect mods directory"
  echo "   Expected: $PA_MODS_DIR"
  echo ""
  echo "   Please ensure Prison Architect is installed and run it at least once"
  echo "   Then run this script again"
  exit 1
fi

echo "✓ Found mods directory: $PA_MODS_DIR"
echo ""

# Step 4: Copy mods
echo "[4/4] Installing mods to Prison Architect..."
MODS=(
  "IndustrialMod"
  "AdvancedStaffMod"
  "PrisonRoles"
  "SecurityEnhancements"
  "HospitalMod"
  "UtilitiesMod"
  "AdvancedWorkshops"
  "LuxuryRooms"
  "VivekGym"
)

for mod in "${MODS[@]}"; do
  if [ -d "$mod" ]; then
    rm -rf "$PA_MODS_DIR/$mod" 2>/dev/null || true
    cp -r "$mod" "$PA_MODS_DIR/"
    echo "  ✓ Installed $mod"
  else
    echo "  ⚠ Skipped $mod (folder not found)"
  fi
done

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║   ✓ Setup Complete!                                        ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "Next steps:"
echo "1. Launch Prison Architect"
echo "2. Go to: Mods menu"
echo "3. Enable each mod individually"
echo "4. Create a new Sandbox prison"
echo "5. Your custom objects should appear in Quick Build menus!"
echo ""
echo "Installed to: $PA_MODS_DIR"
echo ""
