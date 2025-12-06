#!/usr/bin/env python3
"""
Prison Architect Mod Sprite Generator
Generates all required sprite PNG files and graphics.txt configurations for mods
Run: python3 generate_sprites.py
"""

from PIL import Image, ImageDraw, ImageFont
import os
import json

# Define all mods and their requirements
MODS_CONFIG = {
    'IndustrialMod': {
        'objects': {
            'CoalPowerPlant': {'color': (101, 67, 33), 'size': (6, 4)},  # Brown
            'SteelPlant': {'color': (100, 100, 110), 'size': (5, 5)},     # Steel gray
            'CocaColaFactory': {'color': (200, 50, 50), 'size': (5, 4)},  # Red
            'TrainTrack': {'color': (80, 80, 80), 'size': (1, 1)},        # Dark gray
            'TrainStation': {'color': (150, 120, 80), 'size': (3, 3)},    # Tan
            'TrainCarriage': {'color': (100, 80, 60), 'size': (2, 4)},    # Dark tan
        },
        'staff': {}
    },
    'AdvancedStaffMod': {
        'objects': {},
        'staff': {
            'CalmingOfficer': {'color': (128, 0, 128)},      # Purple
            'PhysicalTherapist': {'color': (34, 139, 34)},   # Green
            'MentalHealthCounselor': {'color': (0, 0, 205)}, # Blue
            'HungerRelief': {'color': (255, 165, 0)},        # Orange
            'FitnessCoach': {'color': (220, 20, 60)},        # Crimson
            'LeisureDirector': {'color': (255, 255, 0)},     # Yellow
            'SecurityPsychologist': {'color': (25, 25, 112)},# Dark blue
            'EducationCoordinator': {'color': (210, 180, 140)},  # Tan
            'SocialWorker': {'color': (50, 205, 50)},        # Lime
            'MoodStabilizer': {'color': (147, 112, 219)},    # Purple
            'AngerManagementOfficer': {'color': (220, 20, 60)},  # Crimson
            'HealthClerk': {'color': (255, 255, 255)},       # White
            'PrisonBeautician': {'color': (255, 192, 203)},  # Pink
            'LifeCoach': {'color': (192, 192, 192)},         # Silver
            'SeniorCounselor': {'color': (25, 25, 112)},     # Navy
            'FamilyMediator': {'color': (255, 215, 0)},      # Gold
            'RehabilitationOfficer': {'color': (0, 128, 128)},   # Teal
            'WellnessCoordinator': {'color': (64, 224, 208)},    # Turquoise
            'ConflictResolution': {'color': (184, 134, 11)},     # Dark goldenrod
            'IndividualTherapist': {'color': (75, 0, 130)},      # Indigo
            'RecreationSpecialist': {'color': (50, 205, 50)},    # Lime green
        }
    },
    'PrisonRoles': {
        'objects': {},
        'staff': {
            'Priest': {'color': (100, 50, 100)},             # Dark purple
            'Chaplain': {'color': (128, 0, 128)},            # Purple
            'Nun': {'color': (200, 200, 255)},               # Light blue
            'PrayerCounselor': {'color': (150, 0, 150)},     # Dark purple
            'SpiritualGuide': {'color': (180, 82, 45)},      # Brown
            'ReligiousTeacher': {'color': (210, 105, 30)},   # Chocolate
            'Deacon': {'color': (100, 100, 150)},            # Slate
            'WorshipFacilitator': {'color': (138, 43, 226)}, # Blue violet
            'CounselingAdvisor': {'color': (72, 209, 204)},  # Medium turquoise
            'MoralEducator': {'color': (240, 128, 128)},     # Light coral
            'SupportCounselor': {'color': (135, 206, 250)},  # Light sky blue
            'WellnessChaplain': {'color': (144, 238, 144)},  # Light green
        }
    },
    'SecurityEnhancements': {
        'objects': {},
        'staff': {
            'SecurityGuardMetalDetector': {'color': (25, 25, 112)},   # Dark blue
            'K9SecurityHandler': {'color': (139, 69, 19)},            # Brown
            'AdvancedSearchOfficer': {'color': (0, 0, 0)},            # Black
        }
    },
    'HospitalMod': {
        'objects': {
            'HospitalBed': {'color': (255, 255, 255), 'size': (2, 2)},
            'OperatingTable': {'color': (200, 200, 200), 'size': (3, 3)},
            'MoodUplifter': {'color': (255, 200, 0), 'size': (2, 2)},
            'AdvancedDiagnosticMachine': {'color': (100, 150, 200), 'size': (2, 2)},
        },
        'staff': {}
    },
    'UtilitiesMod': {
        'objects': {
            'AdvancedLaundry': {'color': (135, 206, 235), 'size': (3, 3)},
            'ProfessionalKitchen': {'color': (255, 140, 0), 'size': (4, 4)},
            'EnhancedPowerPlant': {'color': (128, 128, 0), 'size': (3, 3)},
        },
        'staff': {}
    },
    'SecurityEnhancements_Objects': {
        'objects': {
            'AutoWiretap': {'color': (50, 100, 50), 'size': (1, 1)},
            'WirelessCamera': {'color': (100, 100, 100), 'size': (1, 1)},
            'RemoteDoor': {'color': (150, 50, 50), 'size': (2, 1)},
        },
        'staff': {}
    }
}

def create_sprite(filename, color, text="", size=64):
    """Create a 64x64 sprite with given color and optional text"""
    img = Image.new('RGB', (size, size), color=color)
    draw = ImageDraw.Draw(img)
    
    # Add border
    draw.rectangle([(1, 1), (size-2, size-2)], outline=(0, 0, 0), width=2)
    
    # Add gradient effect (darker right/bottom)
    for i in range(size):
        for j in range(size):
            if i > size * 0.7 or j > size * 0.7:
                alpha_adjust = 0.8
                current = img.getpixel((i, j))
                new_color = tuple(int(c * alpha_adjust) for c in current)
                img.putpixel((i, j), new_color)
    
    # Add text if provided
    if text:
        try:
            # Try to use default font
            draw.text((size//2, size//2), text[:3], fill=(255, 255, 255), anchor="mm")
        except:
            pass
    
    return img

def create_icon(filename, color, size=32):
    """Create a 32x32 icon sprite"""
    img = Image.new('RGB', (size, size), color=color)
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (size-1, size-1)], outline=(0, 0, 0), width=1)
    return img

def create_staff_sprites(filename, color):
    """Create head and body sprites for staff"""
    # Head sprite (64x64, top half colored)
    head = Image.new('RGB', (64, 64), color=(255, 200, 180))  # Skin tone
    draw = ImageDraw.Draw(head)
    # Draw head circle
    draw.ellipse([(16, 8), (48, 40)], fill=(255, 200, 180), outline=(0, 0, 0))
    # Draw eyes
    draw.ellipse([(24, 20), (28, 24)], fill=(0, 0, 0))
    draw.ellipse([(36, 20), (40, 24)], fill=(0, 0, 0))
    
    # Body sprite (64x64, with uniform)
    body = Image.new('RGB', (64, 64), color=color)
    draw_body = ImageDraw.Draw(body)
    # Draw shoulders
    draw_body.rectangle([(10, 30), (54, 55)], fill=color, outline=(0, 0, 0))
    
    return head, body

def generate_all_sprites():
    """Generate all sprites for all mods"""
    
    for mod_name, mod_data in MODS_CONFIG.items():
        # Create mod directory structure
        mod_dir = f"{mod_name}/data/graphics"
        os.makedirs(f"{mod_dir}/objects", exist_ok=True)
        os.makedirs(f"{mod_dir}/staff", exist_ok=True)
        
        graphics_txt = "# Auto-generated graphics configuration\n\n"
        
        # Generate object sprites
        for obj_name, obj_data in mod_data.get('objects', {}).items():
            color = obj_data.get('color', (128, 128, 128))
            
            # Main sprite
            sprite = create_sprite(f"{mod_dir}/objects/{obj_name}.png", color)
            sprite.save(f"{mod_dir}/objects/{obj_name}.png")
            
            # Icon sprite
            icon = create_icon(f"{mod_dir}/objects/{obj_name}_icon.png", color)
            icon.save(f"{mod_dir}/objects/{obj_name}_icon.png")
            
            size = obj_data.get('size', (2, 2))
            graphics_txt += f"""[ObjectDefinition {obj_name}]
  Graphic ./graphics/objects/{obj_name}.png
  GraphicIcon ./graphics/objects/{obj_name}_icon.png
  Size {size[0]} {size[1]}

"""
        
        # Generate staff sprites
        for staff_name, staff_data in mod_data.get('staff', {}).items():
            color = staff_data.get('color', (128, 128, 128))
            
            # Head and body
            head, body = create_staff_sprites(staff_name, color)
            head.save(f"{mod_dir}/staff/{staff_name}_head.png")
            body.save(f"{mod_dir}/staff/{staff_name}_body.png")
            
            # Icon
            icon = create_icon(f"{mod_dir}/staff/{staff_name}_icon.png", color)
            icon.save(f"{mod_dir}/staff/{staff_name}_icon.png")
            
            graphics_txt += f"""[StaffDefinition {staff_name}]
  GraphicHead ./graphics/staff/{staff_name}_head.png
  GraphicBody ./graphics/staff/{staff_name}_body.png
  GraphicIcon ./graphics/staff/{staff_name}_icon.png

"""
        
        # Write graphics.txt
        with open(f"{mod_dir}/graphics.txt", 'w') as f:
            f.write(graphics_txt)
        
        print(f"✓ Generated sprites for {mod_name}")

if __name__ == "__main__":
    print("Prison Architect Mod Sprite Generator")
    print("=====================================\n")
    
    try:
        generate_all_sprites()
        print("\n✓ All sprites generated successfully!")
        print("\nGenerated files:")
        print("- All PNG sprites (64x64 objects, 32x32 icons)")
        print("- graphics.txt configuration files for each mod")
        print("\nNext steps:")
        print("1. Make sure PIL/Pillow is installed: pip install Pillow")
        print("2. Run this script: python3 generate_sprites.py")
        print("3. Copy all generated mods to Prison Architect's mods folder")
        print("4. Launch Prison Architect and enable mods in menu")
    except Exception as e:
        print(f"✗ Error: {e}")
        print("Make sure Pillow is installed: pip install Pillow")
