# ============================================================================
# CHAP 5 - TASK 4 - ADDED
# ============================================================================
# Program: Image Processing Service - Sequential vs Parallel Execution
# Description: Demonstrates concurrent.futures with ThreadPoolExecutor and
#              ProcessPoolExecutor using a real-life image processing scenario.
#              Compares performance of sequential, thread pool, and process pool.
# ============================================================================

import concurrent.futures
import time

# Simulating 10 images to process (each with different sizes in MB)
image_list = [
    {"id": 1, "name": "photo_001.jpg", "size_mb": 2},
    {"id": 2, "name": "photo_002.jpg", "size_mb": 5},
    {"id": 3, "name": "photo_003.jpg", "size_mb": 3},
    {"id": 4, "name": "photo_004.jpg", "size_mb": 8},
    {"id": 5, "name": "photo_005.jpg", "size_mb": 4},
    {"id": 6, "name": "photo_006.jpg", "size_mb": 6},
    {"id": 7, "name": "photo_007.jpg", "size_mb": 2},
    {"id": 8, "name": "photo_008.jpg", "size_mb": 7},
    {"id": 9, "name": "photo_009.jpg", "size_mb": 3},
    {"id": 10, "name": "photo_010.jpg", "size_mb": 5},
]


def apply_filter(image_size):
    """
    Simulate CPU-intensive image filter processing.
    
    Real-life scenario: Applying filters like blur, sharpen, color correction
    to an image requires heavy computation based on image size.
    
    Args:
        image_size: Size of image in MB (affects processing time)
    
    Returns:
        Number of pixels processed (simulated)
    """
    pixels_processed = 0
    # Simulate processing - more pixels for larger images
    for i in range(0, 1000000 * image_size):
        pixels_processed += 1
    return pixels_processed


def process_image(image):
    """
    Process a single image with filters.
    
    Real-life scenario: Photo editing app processing uploaded images
    - Applies filters
    - Resizes image
    - Optimizes for web
    
    Args:
        image: Dictionary containing image details
    """
    pixels = apply_filter(image["size_mb"])
    print(f'📷 Processed: {image["name"]} ({image["size_mb"]}MB) - {pixels:,} pixels')
    return pixels


if __name__ == '__main__':
    print("=" * 70)
    print("    IMAGE PROCESSING SERVICE - Performance Comparison")
    print("    Sequential vs Thread Pool vs Process Pool Execution")
    print("=" * 70)
    print(f"\n📁 Processing {len(image_list)} images...\n")
    
    # =========================================================================
    # METHOD 1: Sequential Execution (One image at a time)
    # =========================================================================
    print("-" * 70)
    print("🔄 METHOD 1: SEQUENTIAL EXECUTION")
    print("   Processing images one by one (like a single worker)")
    print("-" * 70)
    
    start_time = time.perf_counter()  # Using perf_counter (time.clock deprecated)
    
    for image in image_list:
        process_image(image)
    
    sequential_time = time.perf_counter() - start_time
    print(f'\n⏱️  Sequential Execution Time: {sequential_time:.2f} seconds\n')
    
    # =========================================================================
    # METHOD 2: Thread Pool Execution (Multiple threads, shared memory)
    # =========================================================================
    print("-" * 70)
    print("🧵 METHOD 2: THREAD POOL EXECUTION (5 workers)")
    print("   Like having 5 editors working on images simultaneously")
    print("-" * 70)
    
    start_time = time.perf_counter()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Submit all images for processing
        futures = [executor.submit(process_image, image) for image in image_list]
        # Wait for all to complete
        concurrent.futures.wait(futures)
    
    thread_pool_time = time.perf_counter() - start_time
    print(f'\n⏱️  Thread Pool Execution Time: {thread_pool_time:.2f} seconds\n')
    
    # =========================================================================
    # METHOD 3: Process Pool Execution (Multiple processes, separate memory)
    # =========================================================================
    print("-" * 70)
    print("⚙️  METHOD 3: PROCESS POOL EXECUTION (5 workers)")
    print("   Like having 5 separate computers processing images")
    print("-" * 70)
    
    start_time = time.perf_counter()
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        # Submit all images for processing
        futures = [executor.submit(process_image, image) for image in image_list]
        # Wait for all to complete
        concurrent.futures.wait(futures)
    
    process_pool_time = time.perf_counter() - start_time
    print(f'\n⏱️  Process Pool Execution Time: {process_pool_time:.2f} seconds\n')
    
    # =========================================================================
    # Performance Summary
    # =========================================================================
    print("=" * 70)
    print("    📊 PERFORMANCE SUMMARY")
    print("=" * 70)
    print(f"    Sequential:    {sequential_time:.2f} seconds")
    print(f"    Thread Pool:   {thread_pool_time:.2f} seconds")
    print(f"    Process Pool:  {process_pool_time:.2f} seconds")
    print("-" * 70)
    
    # Calculate speedup
    thread_speedup = sequential_time / thread_pool_time if thread_pool_time > 0 else 0
    process_speedup = sequential_time / process_pool_time if process_pool_time > 0 else 0
    
    print(f"    🚀 Thread Pool Speedup:  {thread_speedup:.2f}x faster")
    print(f"    🚀 Process Pool Speedup: {process_speedup:.2f}x faster")
    print("=" * 70)
