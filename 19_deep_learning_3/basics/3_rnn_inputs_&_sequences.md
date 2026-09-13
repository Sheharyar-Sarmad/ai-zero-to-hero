

# Time, Semantic Meaning, Input Features & Workflow 

## 1. Semantic Meaning of "Time Step" in RNNs

- Each time step `t` doesn't have to mean literal "time" — it means **position in a sequence**.
- Interpretation depends on data type:

| Data Type | What a "time step" represents |
|---|---|
| Text | A word / token / character |
| Speech | An audio frame (e.g., 20ms chunk) |
| Time series (stock, weather) | An actual timestamp (hour, day) |
| Video | A single frame |
| Sensor data (IoT) | A reading at a fixed interval |

- The RNN doesn't inherently "know" what time means — it just learns patterns in the **order** of inputs it's fed.
- Semantic meaning comes from **how you encode** the input at each step, not from the model itself.

---

## 2. Timestamps as Input Features

When working with real time-series data (not just plain sequences), the raw timestamp itself is usually **not fed directly**. Instead, it's decomposed into meaningful numeric/categorical features.

### Common Timestamp-Derived Features
- Second, minute, hour
- Day of week
- Day of month
- Week of year
- Month
- Quarter
- Year
- Is weekend (0/1)
- Is holiday (0/1)
- Time since last event (delta time)
- Cyclical encoding (for periodicity):
```
hour_sin = sin(2π · hour / 24)
hour_cos = cos(2π · hour / 24)
```
  (Same idea applies to day-of-week, month, etc. — avoids the "23 → 0" discontinuity problem.)

### Why Cyclical Encoding Matters
- Raw hour value (0–23) treats hour 23 and hour 0 as far apart numerically, even though they're adjacent in real time.
- Sin/cos encoding preserves this cyclical closeness.

---

## 3. Input Feature Types (General, for Sequence Models)

| Feature Category | Examples |
|---|---|
| Raw signal | Token embedding, pixel value, sensor reading |
| Positional | Time step index, timestamp-derived features |
| Static/context | User ID, category, location (doesn't change across sequence) |
| Derived/engineered | Moving average, delta, lag features |
| External | Weather, holidays, events (for time series) |

### Lag Features (important for time series)
```
lag_1 = value at (t-1)
lag_7 = value at (t-7)     # e.g., same day last week
rolling_mean_7 = average of last 7 values
```

---

## 4. Overall Workflow (End-to-End)

```
1. Data Collection
   → Raw sequential/time-stamped data

2. Preprocessing
   → Handle missing timestamps/values
   → Sort by time
   → Resample if needed (e.g., fill gaps to fixed interval)

3. Feature Engineering
   → Extract timestamp features (hour, day, cyclical encoding)
   → Create lag/rolling features
   → Normalize/scale numeric features
   → Encode categorical features (embeddings or one-hot)

4. Sequence Construction
   → Convert data into (input_sequence, target) pairs
   → Define sequence length / window size
   → Split into train/val/test (respecting time order — no shuffling across time!)

5. Model Input Formatting
   → Shape: (batch_size, sequence_length, num_features)

6. Model (RNN/LSTM/GRU/etc.)
   → Feed sequence step-by-step
   → Hidden state carries forward information

7. Output
   → Single value (forecast) or sequence (multi-step prediction)

8. Post-processing
   → Inverse-transform scaled outputs
   → Map back to real time values

9. Evaluation
   → MAE, RMSE, MAPE (time series)
   → Accuracy, F1 (classification tasks)
```

---

## 5. Important Notes on Time-Series Specific Handling

- **Never shuffle** time-series data randomly before splitting train/test — always split chronologically.
- **Data leakage risk**: using future information (e.g., a rolling mean that includes future values) will inflate performance falsely.
- **Windowing**: input is typically a sliding window of past `n` steps to predict the next step(s).

```
Example (window size = 3, predicting next step):
[x1, x2, x3] → predict x4
[x2, x3, x4] → predict x5
[x3, x4, x5] → predict x6
```

---

## 6. Input Shape Summary for RNNs

```
Input Tensor Shape: (batch_size, time_steps, features)

Example:
- batch_size = 32 (samples per batch)
- time_steps = 10 (past 10 time steps used)
- features = 5 (e.g., temperature, humidity, hour_sin, hour_cos, day_of_week)

Shape: (32, 10, 5)
```