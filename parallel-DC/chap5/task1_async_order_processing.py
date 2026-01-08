# ============================================================================
# CHAP 5 - TASK 1 - ADDED
# ============================================================================
# Program: Asynchronous Online Food Order Processing System
# Description: Demonstrates asyncio coroutines with futures using a real-life
#              scenario of processing food orders - calculating bill total
#              and loyalty points concurrently.
# ============================================================================

import asyncio
import sys


@asyncio.coroutine
def calculate_bill_total(future, num_items):
    """
    Coroutine to calculate the total bill amount.
    
    Real-life scenario: When a customer places an order at a restaurant,
    this coroutine calculates the total cost of all items ordered.
    Each item costs $10 for simplicity.
    
    Args:
        future: asyncio.Future object to store the result
        num_items: Number of food items ordered
    """
    total_bill = 0
    item_price = 10  # Each item costs $10
    
    # Calculate total bill by adding price of each item
    for i in range(1, num_items + 1):
        total_bill += item_price
        print(f"  [Bill Calculator] Adding item {i}: ${item_price}")
    
    # Simulate processing time (e.g., checking inventory, applying taxes)
    yield from asyncio.sleep(2)
    
    # Add 10% tax
    tax = total_bill * 0.10
    final_bill = total_bill + tax
    
    future.set_result(f'BILL SUMMARY: {num_items} items = ${total_bill} + Tax(${tax:.2f}) = ${final_bill:.2f}')


@asyncio.coroutine
def calculate_loyalty_points(future, num_orders):
    """
    Coroutine to calculate customer loyalty points.
    
    Real-life scenario: Restaurant rewards program calculates points
    based on customer's order history. Points = factorial of orders
    (simplified for demonstration).
    
    Args:
        future: asyncio.Future object to store the result
        num_orders: Number of previous orders by the customer
    """
    points = 1
    
    # Calculate loyalty points (using factorial as bonus multiplier)
    for i in range(2, num_orders + 1):
        points *= i
        print(f"  [Loyalty System] Processing order {i}: Points multiplied to {points}")
    
    # Simulate database lookup and calculation time
    yield from asyncio.sleep(2)
    
    future.set_result(f'LOYALTY POINTS: Based on {num_orders} orders, you earned {points} bonus points!')


def display_result(future):
    """
    Callback function to display results when a future completes.
    
    This is called automatically when each coroutine finishes,
    similar to how a notification would appear on a customer's app.
    """
    print(f"\n✓ COMPLETED: {future.result()}")


if __name__ == '__main__':
    print("=" * 60)
    print("    RESTAURANT ORDER PROCESSING SYSTEM")
    print("    Using Asyncio Coroutines with Futures")
    print("=" * 60)
    
    # Get input from command line arguments
    # Usage: python task1_async_order_processing.py <num_items> <num_previous_orders>
    if len(sys.argv) < 3:
        print("\nUsage: python task1_async_order_processing.py <num_items> <num_previous_orders>")
        print("Example: python task1_async_order_processing.py 5 4")
        print("\nUsing default values: 5 items, 4 previous orders")
        num_items = 5
        num_previous_orders = 4
    else:
        num_items = int(sys.argv[1])
        num_previous_orders = int(sys.argv[2])
    
    print(f"\nProcessing order with {num_items} items...")
    print(f"Customer has {num_previous_orders} previous orders.\n")
    
    # Create the event loop
    loop = asyncio.get_event_loop()
    
    # Create Future objects to hold results
    bill_future = asyncio.Future()
    loyalty_future = asyncio.Future()
    
    # Create tasks - both will run concurrently
    tasks = [
        calculate_bill_total(bill_future, num_items),
        calculate_loyalty_points(loyalty_future, num_previous_orders)
    ]
    
    # Add callbacks to display results when futures complete
    bill_future.add_done_callback(display_result)
    loyalty_future.add_done_callback(display_result)
    
    print("Starting concurrent processing...\n")
    
    # Run both coroutines concurrently until they complete
    loop.run_until_complete(asyncio.wait(tasks))
    
    # Clean up
    loop.close()
    
    print("\n" + "=" * 60)
    print("    ORDER PROCESSING COMPLETE!")
    print("=" * 60)
