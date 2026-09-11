

# Padding & Strides 

---

## First, a Quick Recap

Before padding and strides, remember how convolution works:

> A small filter (like a 3×3 box) slides across the image, one step at a time, and produces one number at each position.

Padding and strides are just two **settings** that control HOW that sliding happens.

---

## Part 1 — Padding

### The Problem First

Imagine your image is a piece of paper with numbers on it (6×6 grid).
You slide a 3×3 filter across it.

```
Image is 6×6.
Filter is 3×3.
Output you get = 4×4.   ← the image SHRANK!
```

Now imagine doing this 10 times in a deep network:
```
6×6 → 4×4 → 2×2 → GONE
```

The image shrinks to nothing. That's a problem.

---

### What is Padding?

**Padding = adding a border of zeros around the image before applying the filter.**

Think of it like putting a picture frame made of zeros around your image.

```
Original image (4×4):        After padding (6×6):
                              0  0  0  0  0  0
1  2  3  4                   0  1  2  3  4  0
5  6  7  8       →           0  5  6  7  8  0
9 10 11 12                   0  9 10 11 12  0
13 14 15 16                  0 13 14 15 16  0
                              0  0  0  0  0  0
```

Now when you apply the 3×3 filter, the output stays the same size as the original — 4×4.

---

### Real Life Analogy

Imagine you're reading a book through a small window (your filter).
- Without padding: when you reach the edge of the page, you have to stop early.
- With padding: you add blank margins around the page, so your window can reach every word, including the ones in the corners.

---

### Two Types of Padding

**Type 1 — Valid Padding (no padding at all)**

- You add nothing
- Output gets smaller than input
- Simple but the image keeps shrinking

```
Input 6×6  →  Output 4×4  (shrinks by 2)
```

**Type 2 — Same Padding (add zeros)**

- Add a border of zeros
- Output stays the SAME size as input
- This is what most modern CNNs use

```
Input 6×6  →  Output 6×6  (stays same!)
```

How many zeros to add?
```
For a 3×3 filter → add 1 row/column of zeros on each side
For a 5×5 filter → add 2 rows/columns of zeros on each side
Rule: padding = (filter size - 1) / 2
```

---

### Why Padding Matters

1. **Image doesn't shrink** — you can have many layers without losing size
2. **Edge pixels get fair treatment** — without padding, corner pixels are only touched once by the filter; center pixels are touched many times. Padding fixes this.

```
Without padding:  corner pixel → filter sees it 1 time
With padding:     corner pixel → filter sees it the same as center pixels
```

---

## Part 2 — Strides

### What is a Stride?

**Stride = how many pixels the filter jumps after each step.**

By default, the filter moves **1 pixel at a time** (stride = 1).
But you can tell it to jump **2 pixels at a time** (stride = 2).

---

### Simple Example

Imagine you're reading a line of text:

```
Text:  A B C D E F G H
```

**Stride 1** — read every letter:
```
A, B, C, D, E, F, G, H  (read all 8)
```

**Stride 2** — skip every other letter:
```
A, C, E, G  (read only 4)
```

You covered the same text but in fewer steps and got a shorter result.

---

### In Images

```
Input image: 5×5
Filter: 3×3

Stride = 1                    Stride = 2
Filter starts at:             Filter starts at:
(0,0) (0,1) (0,2)            (0,0)       (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2)            (2,0)       (2,2)

Output: 3×3                   Output: 2×2
(9 positions)                 (4 positions)
```

Bigger stride → **smaller output** and **fewer calculations**.

---

### Real Life Analogy

Imagine you're scanning a photo to look for something:

- **Stride 1** = you slide your magnifying glass one centimeter at a time. Very thorough, slow, covers everything.
- **Stride 2** = you slide your magnifying glass two centimeters at a time. Faster, skips some spots, but still gets the big picture.

For most tasks, stride 2 is enough — you don't need to check every single pixel position.

---

### How to Calculate Output Size

This formula works for any combination of padding and stride:

```
Output Size = floor( (Input - Filter + 2 × Padding) / Stride ) + 1
```

Don't be scared of it. Let's plug in simple numbers:

**Example 1** — No padding, stride 1 (the basic case):
```
Input=6, Filter=3, Padding=0, Stride=1
= floor( (6 - 3 + 0) / 1 ) + 1
= floor( 3 ) + 1
= 4
Output: 4×4
```

**Example 2** — Same padding, stride 1:
```
Input=6, Filter=3, Padding=1, Stride=1
= floor( (6 - 3 + 2) / 1 ) + 1
= floor( 5 ) + 1
= 6
Output: 6×6   ← same as input!
```

**Example 3** — No padding, stride 2:
```
Input=6, Filter=3, Padding=0, Stride=2
= floor( (6 - 3 + 0) / 2 ) + 1
= floor( 1.5 ) + 1
= 1 + 1
= 2
Output: 2×2   ← much smaller!
```

---

## Part 3 — Why Do We Use Strides?

### Reason 1 — Make the image smaller (down-sampling)

As the CNN goes deeper, we want to shrink the image progressively.
Stride 2 does this automatically — halves the size in one step.

```
224×224  →  stride 2  →  112×112  →  stride 2  →  56×56
```

This is actually the same job that **pooling** does. But strided convolution is better because the filter **learns** the best way to shrink, instead of just blindly taking the maximum.

---

### Reason 2 — Save computation (make it faster)

Fewer filter positions = fewer calculations = faster training.

```
224×224 image, 3×3 filter:
Stride 1 → ~50,000 filter positions
Stride 2 → ~12,500 filter positions   (4× fewer)
```

In big models with millions of images, this difference is huge.

---

### Reason 3 — See bigger parts of the image faster

With stride 2, each output pixel "summarizes" a larger area of the input. So deeper layers quickly start understanding bigger regions (like an entire face instead of just an eye).

---

## Part 4 — Stride vs Pooling

Both stride and max pooling shrink the image. What's the difference?

| | Max Pooling | Strided Convolution |
|---|---|---|
| What it does | Always picks the maximum value | Learns the best way to shrink |
| Learnable? | No — fixed rule | Yes — trained by the network |
| Speed | Fast | Slightly slower (has weights) |
| Used in | Older CNNs (LeNet, VGG) | Modern CNNs (ResNet, MobileNet) |

**Simple way to think about it:**
- Max pooling = a fixed rule (always take the biggest)
- Strided conv = a smart rule the network figures out itself

---

## Part 5 — Everything Together

Here's a typical CNN using padding and strides:

```
Input image: 224×224×3 (color photo)
        ↓
Conv (3×3, padding=1, stride=1)
→ 224×224×64    (same size, 64 feature maps)
        ↓
Conv (3×3, padding=1, stride=1)
→ 224×224×64    (still same size)
        ↓
Conv (3×3, padding=0, stride=2)
→ 112×112×128   (halved! moved deeper)
        ↓
(keep going deeper...)
```

Same padding keeps the size steady while features are being learned.
Strided conv halves the size when we're ready to go deeper.

---

## Summary (Plain English)

```
PADDING
  Problem:  filter shrinks the image, corners are ignored
  Fix:      add zeros around the border
  Valid:    no zeros added → image shrinks
  Same:     zeros added   → image stays same size

STRIDES
  Stride 1: filter moves 1 pixel at a time (thorough, slow)
  Stride 2: filter jumps 2 pixels at a time (faster, smaller output)

THE FORMULA
  Output = floor( (Input - Filter + 2×Padding) / Stride ) + 1

WHY STRIDES?
  → Shrink the image as we go deeper
  → Reduce computation (fewer positions = faster)
  → See bigger picture faster

STRIDE vs POOLING
  Pooling   = fixed rule (take the max)
  Stride    = learned rule (network decides)
  Modern CNNs prefer strided convolutions
```

---

## One Last Analogy to Remember It All

Think of a CNN as reading a book with a magnifying glass:

- **Padding** = adding blank margins so you can read words right at the edge of the page
- **Stride 1** = moving the magnifying glass one word at a time — thorough but slow
- **Stride 2** = skipping every other word — faster, still gets the meaning
- **Going deeper** = putting down one book and picking up a summary — you lose fine detail but understand the big picture