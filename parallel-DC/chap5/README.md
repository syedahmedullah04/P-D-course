# ============================================================================
# CHAPTER 5 - Asynchronous Programming in Python
# ============================================================================

This chapter demonstrates various asynchronous and parallel programming concepts using Python's `asyncio` module and `concurrent.futures` library.

---

## 📋 Task Summary

| Task | File | Concept | Real-Life Example |
|------|------|---------|-------------------|
| Task 1 | `task1_async_order_processing.py` | Asyncio Coroutines with Futures | Restaurant Order Processing |
| Task 2 | `task2_async_event_loop_scheduling.py` | Event Loop with call_soon/call_later | Smart Home Automation |
| Task 3 | `task3_async_parallel_analytics.py` | Asyncio.Task for Parallel Execution | E-Commerce Analytics |
| Task 4 | `task4_concurrent_futures_comparison.py` | ThreadPool vs ProcessPool | Image Processing Service |

---

## 📌 Task 1: Async Order Processing System

**File:** `task1_async_order_processing.py`

**Concept:** Using `asyncio.coroutine` with `Future` objects to handle asynchronous operations with callbacks.

**Real-Life Scenario:** Restaurant order processing where bill calculation and loyalty points are computed simultaneously.

### How to Run:
```bash
python task1_async_order_processing.py 5 4
```

### Sample Output:
```
============================================================
    RESTAURANT ORDER PROCESSING SYSTEM
    Using Asyncio Coroutines with Futures
============================================================

Processing order with 5 items...
Customer has 4 previous orders.

Starting concurrent processing...

  [Bill Calculator] Adding item 1: $10
  [Bill Calculator] Adding item 2: $10
  [Bill Calculator] Adding item 3: $10
  [Bill Calculator] Adding item 4: $10
  [Bill Calculator] Adding item 5: $10
  [Loyalty System] Processing order 2: Points multiplied to 2
  [Loyalty System] Processing order 3: Points multiplied to 6
  [Loyalty System] Processing order 4: Points multiplied to 24

✓ COMPLETED: BILL SUMMARY: 5 items = $50 + Tax($5.00) = $55.00

✓ COMPLETED: LOYALTY POINTS: Based on 4 orders, you earned 24 bonus points!

============================================================
    ORDER PROCESSING COMPLETE!
============================================================
```

---

## 📌 Task 2: Smart Home Automation System

**File:** `task2_async_event_loop_scheduling.py`

**Concept:** Using `asyncio` event loop with `call_soon` and `call_later` for scheduled task execution.

**Real-Life Scenario:** Smart home system that rotates between security checks, temperature control, and lighting management.

### How to Run:
```bash
python task2_async_event_loop_scheduling.py
```

### Sample Output:
```
============================================================
    SMART HOME AUTOMATION SYSTEM
    Using Asyncio Event Loop Scheduling
============================================================

This system rotates between three smart home tasks:
  1. 🔒 Security System Check
  2. 🌡️  Temperature Control
  3. 💡 Lighting Control

Running automation cycle for 30 seconds...
============================================================

🔒 [SECURITY] Checking all door and window sensors...
   ✓ Security check completed in 2s - All sensors OK!
   → Scheduling: Temperature Control in 1 second...

🌡️  [THERMOSTAT] Current temperature: 25°C
   ✓ Cooling activated! Adjusting to 22°C (took 1s)
   → Scheduling: Lighting Control in 1 second...

💡 [LIGHTS] Checking Living Room lighting...
   ✓ Living Room brightness set to 75% (took 2s)
   → Scheduling: Security Check in 1 second...

--------------------------------------------------
🔒 [SECURITY] Checking all door and window sensors...
   ✓ Security check completed in 1s - All sensors OK!
   → Scheduling: Temperature Control in 1 second...

⏰ Automation cycle complete. Shutting down...

============================================================
    SMART HOME AUTOMATION STOPPED
    All systems in standby mode
============================================================
```

---

## 📌 Task 3: E-Commerce Analytics System

**File:** `task3_async_parallel_analytics.py`

**Concept:** Using `asyncio.Task` to execute multiple coroutines in parallel.

**Real-Life Scenario:** E-commerce platform running sales analysis, traffic tracking, and inventory analysis simultaneously.

### How to Run:
```bash
python task3_async_parallel_analytics.py
```

### Sample Output:
```
=================================================================
    E-COMMERCE ORDER ANALYTICS SYSTEM
    Using Asyncio.Task for Parallel Execution
=================================================================

Running three analytics tasks in PARALLEL:
  📊 Task 1: Daily Sales Revenue Calculation
  👥 Task 2: Customer Traffic Analysis
  📦 Task 3: Inventory Turnover Analysis

-----------------------------------------------------------------

📊 [SALES] Processing order #1 - Value: $25
👥 [TRAFFIC] Hour 1: 15 visitors on site
📦 [INVENTORY] Analyzing product batch #1 - Turnover factor: 15
📊 [SALES] Processing order #2 - Value: $50
👥 [TRAFFIC] Hour 2: 25 visitors on site
📦 [INVENTORY] Analyzing product batch #2 - Turnover factor: 105
📊 [SALES] Processing order #3 - Value: $75
👥 [TRAFFIC] Hour 3: 40 visitors on site
📦 [INVENTORY] Analyzing product batch #3 - Turnover factor: 455
📊 [SALES] Processing order #4 - Value: $100
👥 [TRAFFIC] Hour 4: 65 visitors on site
📦 [INVENTORY] Analyzing product batch #4 - Turnover factor: 1365
📊 [SALES] Processing order #5 - Value: $125
👥 [TRAFFIC] Hour 5: 105 visitors on site
📦 [INVENTORY] Analyzing product batch #5 - Turnover factor: 3003
📊 [SALES] Processing order #6 - Value: $150
👥 [TRAFFIC] Hour 6: 170 visitors on site
📦 [INVENTORY] Analyzing product batch #6 - Turnover factor: 5005
📊 [SALES] Processing order #7 - Value: $175
👥 [TRAFFIC] Hour 7: 275 visitors on site
📦 [INVENTORY] Analyzing product batch #7 - Turnover factor: 6435
📊 [SALES] Processing order #8 - Value: $200
👥 [TRAFFIC] Hour 8: 445 visitors on site
📦 [INVENTORY] Analyzing product batch #8 - Turnover factor: 6435

✅ [SALES COMPLETE] Total Daily Revenue = $900
   Average Order Value = $112.50

✅ [TRAFFIC COMPLETE] Total Visitors Today = 1150
   Peak Hour Visitors = 720

✅ [INVENTORY COMPLETE] Turnover Combinations = 6435
   Stock Efficiency = 53.3%

-----------------------------------------------------------------

=================================================================
    ALL ANALYTICS TASKS COMPLETED!
    Dashboard ready for business review
=================================================================
```

---

## 📌 Task 4: Image Processing - Performance Comparison

**File:** `task4_concurrent_futures_comparison.py`

**Concept:** Comparing `Sequential`, `ThreadPoolExecutor`, and `ProcessPoolExecutor` for CPU-intensive tasks.

**Real-Life Scenario:** Image processing service applying filters to multiple images with performance benchmarking.

### How to Run:
```bash
python task4_concurrent_futures_comparison.py
```

### Sample Output:
```
======================================================================
    IMAGE PROCESSING SERVICE - Performance Comparison
    Sequential vs Thread Pool vs Process Pool Execution
======================================================================

📁 Processing 10 images...

----------------------------------------------------------------------
🔄 METHOD 1: SEQUENTIAL EXECUTION
   Processing images one by one (like a single worker)
----------------------------------------------------------------------
📷 Processed: photo_001.jpg (2MB) - 2,000,000 pixels
📷 Processed: photo_002.jpg (5MB) - 5,000,000 pixels
📷 Processed: photo_003.jpg (3MB) - 3,000,000 pixels
📷 Processed: photo_004.jpg (8MB) - 8,000,000 pixels
📷 Processed: photo_005.jpg (4MB) - 4,000,000 pixels
📷 Processed: photo_006.jpg (6MB) - 6,000,000 pixels
📷 Processed: photo_007.jpg (2MB) - 2,000,000 pixels
📷 Processed: photo_008.jpg (7MB) - 7,000,000 pixels
📷 Processed: photo_009.jpg (3MB) - 3,000,000 pixels
📷 Processed: photo_010.jpg (5MB) - 5,000,000 pixels

⏱️  Sequential Execution Time: 12.45 seconds

----------------------------------------------------------------------
🧵 METHOD 2: THREAD POOL EXECUTION (5 workers)
   Like having 5 editors working on images simultaneously
----------------------------------------------------------------------
📷 Processed: photo_001.jpg (2MB) - 2,000,000 pixels
📷 Processed: photo_003.jpg (3MB) - 3,000,000 pixels
📷 Processed: photo_005.jpg (4MB) - 4,000,000 pixels
📷 Processed: photo_002.jpg (5MB) - 5,000,000 pixels
📷 Processed: photo_007.jpg (2MB) - 2,000,000 pixels
📷 Processed: photo_004.jpg (8MB) - 8,000,000 pixels
📷 Processed: photo_009.jpg (3MB) - 3,000,000 pixels
📷 Processed: photo_006.jpg (6MB) - 6,000,000 pixels
📷 Processed: photo_010.jpg (5MB) - 5,000,000 pixels
📷 Processed: photo_008.jpg (7MB) - 7,000,000 pixels

⏱️  Thread Pool Execution Time: 8.32 seconds

----------------------------------------------------------------------
⚙️  METHOD 3: PROCESS POOL EXECUTION (5 workers)
   Like having 5 separate computers processing images
----------------------------------------------------------------------
📷 Processed: photo_001.jpg (2MB) - 2,000,000 pixels
📷 Processed: photo_003.jpg (3MB) - 3,000,000 pixels
📷 Processed: photo_007.jpg (2MB) - 2,000,000 pixels
📷 Processed: photo_005.jpg (4MB) - 4,000,000 pixels
📷 Processed: photo_002.jpg (5MB) - 5,000,000 pixels
📷 Processed: photo_009.jpg (3MB) - 3,000,000 pixels
📷 Processed: photo_006.jpg (6MB) - 6,000,000 pixels
📷 Processed: photo_010.jpg (5MB) - 5,000,000 pixels
📷 Processed: photo_004.jpg (8MB) - 8,000,000 pixels
📷 Processed: photo_008.jpg (7MB) - 7,000,000 pixels

⏱️  Process Pool Execution Time: 3.21 seconds

======================================================================
    📊 PERFORMANCE SUMMARY
======================================================================
    Sequential:    12.45 seconds
    Thread Pool:   8.32 seconds
    Process Pool:  3.21 seconds
----------------------------------------------------------------------
    🚀 Thread Pool Speedup:  1.50x faster
    🚀 Process Pool Speedup: 3.88x faster
======================================================================
```

---

## 🎯 Key Concepts Learned

| Concept | Description |
|---------|-------------|
| **asyncio.coroutine** | Generator-based coroutines using `@asyncio.coroutine` decorator |
| **Future** | Object representing eventual result of async operation |
| **Event Loop** | Core of asyncio - schedules and runs async tasks |
| **call_soon** | Schedule callback to run on next iteration |
| **call_later** | Schedule callback after specified delay |
| **asyncio.Task** | Wraps coroutines for parallel execution |
| **ThreadPoolExecutor** | Thread-based parallelism (good for I/O-bound tasks) |
| **ProcessPoolExecutor** | Process-based parallelism (good for CPU-bound tasks) |

---

## 🛠️ Requirements

- Python 3.6+
- No external dependencies required

---

## 👨‍💻 Author

**Chapter 5 - Parallel & Distributed Computing Lab**

---
