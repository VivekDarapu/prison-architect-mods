#!/usr/bin/env python3
"""
Prison Architect Mods - Enhanced Sprite & Asset Generator
Generates: PNG sprites, graphics.txt, prefabs.txt, thumbnails
Run: python3 generate_sprites_ENHANCED.py
"""
from PIL import Image, ImageDraw, ImageFont
import os
import json

MODS_CONFIG = {
    'IndustrialMod': {
        'objects': {
            'CoalPowerPlant': {'color': (101, 67, 33), 'size': (6, 4)},
            'SteelPlant': {'color': (100, 100, 110), 'size': (5, 5)},
            'CocaColaFactory': {'color': (200, 50, 50), 'size': (5, 4)},
            'TrainTrack': {'color': (80, 80, 80), 'size': (1, 1)},
            'TrainStation': {'color': (150, 120, 80), 'size': (3, 3)},
            'TrainCarriage': {'color': (100, 80, 60), 'size': (2, 4)},
        },
        'staff': {}
    },
    'AdvancedStaffMod': {
        'objects': {},
        'staff': {
            'CalmingOfficer': {'color': (128, 0, 128)},
            'PhysicalTherapist': {'color': (34, 139, 34)},
            'MentalHealthCounselor': {'color': (0, 0, 205)},
            'HungerRelief': {'color': (255, 165, 0)},
            'FitnessCoach': {'color': (220, 20, 60)},
        }
    },
    'PrisonRoles': {
        'objects': {},
        'staff': {
            'Priest': {'color': (100, 50, 100)},
            'Chaplain': {'color': (128, 0, 128)},
        }
    },
    'SecurityEnhancements': {
        'objects': {},
        'staff': {
            'SecurityGuardMetalDetector': {'color': (25, 25, 112)},
            'K9SecurityHandler': {'color': (139, 69, 19)},
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
    'AdvancedWorkshops': {
        'objects': {
            'MetalShop': {'color': (169, 169, 169), 'size': (4, 4)},
            'WoodShop': {'color': (160, 82, 45), 'size': (4, 4)},
            'ElectronicsLab': {'color': (70, 130, 180), 'size': (3, 3)},
        },
        'staff': {}
    },
    'LuxuryRooms': {
        'objects': {
            'DeluxeSofa': {'color': (255, 20, 147), 'size': (2, 2)},
            'HighEndTV': {'color': (0, 0, 0), 'size': (2, 1)},
            'GourmetKitchen': {'color': (184, 134, 11), 'size': (3, 3)},
        },
        'staff': {}
    },
    'VivekGym': {
        'objects': {
            'Treadmill': {'color': (192, 192, 192), 'size': (2, 2)},
            'Weights': {'color': (105, 105, 105), 'size': (1, 1)},
            'YogaMat': {'color': (144, 238, 144), 'size': (2, 2)},
        },
        'staff': {}
    }
}

def create_sprite(filename, color, text="", size=64):
    img = Image.new('RGB', (size, size), color=color)
    draw = ImageDraw.Draw(img)
    draw.rectangle([(1, 1), (size-2, size-2)], outline=(0, 0, 0), width=2)
    for i in range(size):
        for j in range(size):
            if i > size * 0.7 or j > size * 0.7:
                alpha_adjust = 0.8
                current = img.getpixel((i, j))
                new_color = tuple(int(c * alpha_adjust) for c in current)
                img.putpixel((i, j), new_color)
    return img

def create_icon(filename, color, size=32):
    img = Image.new('RGB', (size, size), color=color)
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (size-1, size-1)], outline=(0, 0, 0), width=1)
    return img

def create_thumbnail(filename, color, size=128):
    img = Image.new('RGB', (size, size), color=color)
    draw = ImageDraw.Draw(img)
    draw.rectangle([(5, 5), (size-5, size-5)], outline=(0, 0, 0), width=3)
    return img

def create_staff_sprites(filename, color):
    head = Image.new('RGB', (64, 64), color=(255, 200, 180))
    draw = ImageDraw.Draw(head)
    draw.ellipse([(16, 8), (48, 40)], fill=(255, 200, 180), outline=(0, 0, 0))
    draw.ellipse([(24, 20), (28, 24)], fill=(0, 0, 0))
    draw.ellipse([(36, 20), (40, 24)], fill=(0, 0, 0))
    
    body = Image.new('RGB', (64, 64), color=color)
    draw_body = ImageDraw.Draw(body)
    draw_body.rectangle([(10, 30), (54, 55)], fill=color, outline=(0, 0, 0))
    
    return head, body

def generate_all_assets():
    for mod_name, mod_data in MODS_CONFIG.items():
        mod_dir = f"{mod_name}/data/graphics"
        os.makedirs(f"{mod_dir}/objects", exist_ok=True)
        os.makedirs(f"{mod_dir}/staff", exist_ok=True)
        os.makedirs(f"{mod_dir}/thumbnails", exist_ok=True)
        
        graphics_txt = "# Auto-generated graphics\n\n"
        prefabs_txt = "# Auto-generated prefabs\n\n"
        
        # Generate object sprites and prefabs
        for obj_name, obj_data in mod_data.get('objects', {}).items():
            color = obj_data.get('color', (128, 128, 128))
            size = obj_data.get('size', (2, 2))
            
            sprite = create_sprite(f"{mod_dir}/objects/{obj_name}.png", color)
            sprite.save(f"{mod_dir}/objects/{obj_name}.png")
            
            icon = create_icon(f"{mod_dir}/objects/{obj_name}_icon.png", color)
            icon.save(f"{mod_dir}/objects/{obj_name}_icon.png")
            
            thumb = create_thumbnail(f"{mod_dir}/thumbnails/{obj_name}.png", color)
            thumb.save(f"{mod_dir}/thumbnails/{obj_name}.png")
            
            graphics_txt += f"[ObjectDefinition {obj_name}]\nGraphic ./graphics/objects/{obj_name}.png\nGraphicIcon ./graphics/objects/{obj_name}_icon.png\nSize {size[0]} {size[1]}\n\n"
            
            prefabs_txt += f"[Prefab {obj_name}]\nObject {obj_name}\n\n"
        
        # Generate staff sprites
        for staff_name, staff_data in mod_data.get('staff', {}).items():
            color = staff_data.get('color', (128, 128, 128))
            
            head, body = create_staff_sprites(staff_name, color)
            head.save(f"{mod_dir}/staff/{staff_name}_head.png")
            body.save(f"{mod_dir}/staff/{staff_name}_body.png")
            
            icon = create_icon(f"{mod_dir}/staff/{staff_name}_icon.png", color)
            icon.save(f"{mod_dir}/staff/{staff_name}_icon.png")
            
            thumb = create_thumbnail(f"{mod_dir}/thumbnails/{staff_name}.png", color)
            thumb.save(f"{mod_dir}/thumbnails/{staff_name}.png")
            
            graphics_txt += f"[StaffDefinition {staff_name}]\nGraphicHead ./graphics/staff/{staff_name}_head.png\nGraphicBody ./graphics/staff/{staff_name}_body.png\nGraphicIcon ./graphics/staff/{staff_name}_icon.png\n\n"
        
        # Write graphics.txt
        with open(f"{mod_dir}/graphics.txt", 'w') as f:
            f.write(graphics_txt)
        
        # Write prefabs.txt
        with open(f"{mod_dir}/../prefabs.txt", 'w') as f:
            f.write(prefabs_txt)
        
        print(f"✓ {mod_name} - All assets generated")

if __name__ == "__main__":
    print("Generating Prison Architect Mod Assets...")
    generate_all_assets()
    print("✓ Complete!")
