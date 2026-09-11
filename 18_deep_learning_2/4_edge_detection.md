

# Edge Finding in CNNs — Complete Notes

---

## 1. How Images Are Represented

### Grayscale Image
A grayscale image is a **single 2D matrix** where every pixel holds one value between 0 and 255.

```
0 = pure black
255 = pure white
1–254 = shades of grey
```

Example (6×6 grayscale — half black, half white):
```
0    0    0    255  255  255
0    0    0    255  255  255
0    0    0    255  255  255
0    0    0    255  255  255
```

- Shape: **H × W × 1** (or just H × W)
- One channel only — brightness information, no color

---

### RGB Image
A color image is **three 2D matrices stacked** together — one per color channel:

```
Red channel   → pixel values 0–255
Green channel → pixel values 0–255
Blue channel  → pixel values 0–255
```

- Shape: **H × W × 3**
- Each pixel's color = combination of its R, G, B values
- Example: (255, 0, 0) = pure red | (0, 0, 255) = pure blue | (255, 255, 255) = white

**Visual:**
```
[ Blue  channel ]
  [ Green channel ]
    [ Red   channel ]
```

---

### Grayscale vs RGB — Quick Comparison

| Property | Grayscale | RGB |
|---|---|---|
| Channels | 1 | 3 |
| Shape | H × W | H × W × 3 |
| Pixel range | 0–255 | (0–255, 0–255, 0–255) |
| Info stored | Brightness only | Full color |
| Memory | 3× less | 3× more |

---

## 2. What Is Edge Finding?

An **edge** in an image is a sharp transition in pixel intensity — a boundary between a dark region and a bright region (or vice versa).

```
Dark pixels → Bright pixels   =   an edge exists here
0   0   0  → 255  255  255
```

CNNs detect edges using small **filter matrices** (kernels) that are convolved across the image.

---

## 3. How Edge Detection Filters Work

### The Core Idea

A filter has **negative weights on one side** and **positive weights on the other**. When it slides over an edge:
- Negative weights land on dark pixels (low values) → small negative
- Positive weights land on bright pixels (high values) → large positive
- They add up → **large output = edge detected**

When it slides over a flat/uniform region:
- Both sides see similar pixel values
- Positives and negatives cancel out → **output ≈ 0 = no edge**

---

### Vertical Edge Filter (Sobel-X)

Detects **left-to-right** brightness transitions (vertical boundaries).

```
-1   0   1
-1   0   1
-1   0   1
```

- Left column: negative → reacts to dark on the left
- Right column: positive → reacts to bright on the right
- Middle column: zero → ignored

**Example:**
```
Image patch:               Filter:              Output:
[  0    0   255 ]         [-1   0   1 ]
[  0    0   255 ]    ×    [-1   0   1 ]   →   large positive → edge!
[  0    0   255 ]         [-1   0   1 ]

Calculation:
(0×-1 + 0×0 + 255×1) × 3 rows = 255 × 3 = 765
```

---

### Horizontal Edge Filter (Sobel-Y)

Detects **top-to-bottom** brightness transitions (horizontal boundaries).

```
-1  -1  -1
 0   0   0
 1   1   1
```

- Top row: negative → reacts to dark on top
- Bottom row: positive → reacts to bright on bottom
- Middle row: zero → ignored

**Example:**
```
Image patch:               Filter:               Output:
[  0    0    0  ]         [-1  -1  -1]
[  0    0    0  ]    ×    [ 0   0   0]   →   large positive → edge!
[255  255  255  ]         [ 1   1   1]

Calculation:
(0×-1 + 0×-1 + 0×-1) + (0) + (255×1 + 255×1 + 255×1)
= 0 + 0 + 765 = 765
```

---

### What Happens with No Edge (Uniform Region)

```
Image patch:               Filter:               Output:
[200  200  200 ]         [-1   0   1 ]
[200  200  200 ]    ×    [-1   0   1 ]   →   0 → no edge
[200  200  200 ]         [-1   0   1 ]

Calculation:
(200×-1 + 200×0 + 200×1) × 3 rows = 0 × 3 = 0
```

Positives and negatives cancel perfectly → output = 0.

---

## 4. Applying Filters to RGB Images

For a grayscale image → 1 filter applied to 1 channel.

For an RGB image → the **same filter applied to each of the 3 channels separately**, then the results are **summed** into a single output value.

```
Red channel   × filter → value_R
Green channel × filter → value_G
Blue channel  × filter → value_B
                         ────────
                         value_R + value_G + value_B = final output
```

So even for color images, the output feature map is still 2D (one number per position).

---

## 5. Output: Feature Map

After sliding the filter across the entire image, every position produces one number. Together they form the **feature map** (also called an activation map).

```
High values  → edge present at that location
Low/zero     → no edge
```

**Output size formula:**
```
Output size = (Input size − Filter size + 2 × Padding) / Stride + 1

Example: 6×6 image, 3×3 filter, no padding, stride 1
= (6 − 3 + 0) / 1 + 1 = 4 × 4 output
```

---

## 6. Multiple Filters → Multiple Feature Maps

In a real CNN layer, many filters run in parallel (e.g., 64 filters):

```
1 image (H × W × 3)
        ↓
64 different filters applied
        ↓
64 feature maps (H × W × 64)
```

Each filter learns to detect a **different pattern**:
- Filter 1 → vertical edges
- Filter 2 → horizontal edges
- Filter 3 → diagonal edges
- Filter 4 → color gradients
- ... and so on (learned automatically during training)

---

## 7. In CNNs — Filters Are Learned, Not Handcrafted

The Sobel filters above are classic handcrafted filters. In a CNN:

- Filters start as **random values**
- During training (backpropagation), filter values are updated to minimize loss
- The network **discovers on its own** which filters best detect useful features
- Early layers → edge/texture detectors (similar to Sobel by coincidence)
- Deeper layers → complex part and object detectors

---

## Summary

```
Grayscale image      →  H × W × 1   (one channel, brightness)
RGB image            →  H × W × 3   (three channels, R + G + B)

Edge = sharp brightness transition (dark → bright or bright → dark)

Vertical filter:     Detects left-right edges
  [-1  0  1]
  [-1  0  1]
  [-1  0  1]

Horizontal filter:   Detects top-bottom edges
  [-1 -1 -1]
  [ 0  0  0]
  [ 1  1  1]

On edge    → large filter output (values don't cancel)
No edge    → output ≈ 0     (values cancel out)

RGB edge detection → filter applied to each channel, outputs summed

Feature map = result of sliding one filter across entire image
Multiple filters → multiple feature maps → richer representation
```