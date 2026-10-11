import cv2
import numpy as np

print("📷 Generating realistic macro tray field photograph...")

# 1. Create a 700x700 White Matte Calibration Tray
tray = np.full((700, 700, 3), 244, dtype=np.uint8)

# Add subtle outdoor canopy lighting gradient (field test simulation)
for y in range(700):
    val = int(240 + (y / 700.0) * 8)
    tray[y, :] = np.clip(tray[y, :] - (y // 70), 225, 250)

# Tray Calibration Grid Lines (10mm intervals)
for step in range(0, 700, 70):
    cv2.line(tray, (step, 0), (step, 700), (220, 226, 222), 1)
    cv2.line(tray, (0, step), (700, step), (220, 226, 222), 1)

# Outer Tray Lip and Scale Stamp
cv2.rectangle(tray, (20, 20), (680, 680), (200, 210, 204), 2)
cv2.putText(tray, "VANAVAL DEPOT FIELD CALIBRATION TRAY - 100mm", (40, 660), cv2.FONT_HERSHEY_SIMPLEX, 0.42, (120, 145, 130), 1)

# Seed Layout Coordinates (Positions on tray)
seeds = [
    (150, 160, 38, 28, 25, False),
    (320, 140, 42, 30, -15, False),
    (490, 180, 40, 29, 60, True),   # Defective (fungal mycelium)
    (220, 310, 44, 32, -45, False),
    (390, 330, 39, 27, 10, False),
    (560, 340, 41, 30, 75, False),
    (180, 480, 43, 31, -30, True),  # Defective (rot patch)
    (340, 500, 40, 28, 40, False),
    (510, 520, 42, 30, -60, False),
    (270, 610, 39, 29, 15, False),
]

for cx, cy, rx, ry, ang, has_defect in seeds:
    # 1. Soft 3D Drop Shadow on Tray
    shadow = tray.copy()
    cv2.ellipse(shadow, (cx + 8, cy + 9), (rx + 2, ry + 2), ang, 0, 360, (190, 198, 194), -1)
    cv2.addWeighted(shadow, 0.4, tray, 0.6, 0, tray)

    # 2. Organic Amla Body (Greenish-gold botanical shading)
    cv2.ellipse(tray, (cx, cy), (rx, ry), ang, 0, 360, (45, 145, 110), -1)
    cv2.ellipse(tray, (cx - 3, cy - 3), (int(rx * 0.78), int(ry * 0.78)), ang, 0, 360, (65, 175, 135), -1)
    # Natural sunlight reflection highlight
    cv2.ellipse(tray, (cx - 8, cy - 8), (int(rx * 0.32), int(ry * 0.32)), ang, 0, 360, (135, 225, 190), -1)
    # Segment seam line
    cv2.line(tray, (cx - rx + 5, cy), (cx + rx - 5, cy), (38, 120, 90), 1)

    # 3. Fungal Mycelium / Decay Patch on Defective Kernels
    if has_defect:
        def_x = cx + 4
        def_y = cy - 2
        # Whitish-grey outer fungal spore halo
        cv2.circle(tray, (def_x, def_y), 12, (215, 222, 226), -1)
        # Inner necrotic rot core
        cv2.circle(tray, (def_x + 1, def_y), 5, (105, 120, 130), -1)

# Save image file directly to project folder
output_filename = "amla_field_sample.jpg"
cv2.imwrite(output_filename, tray)
print(f"✅ Success! Realistic photo saved as: '{output_filename}'")