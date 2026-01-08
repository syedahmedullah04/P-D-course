# ============================================================================
# CHAP 5 - TASK 2 - ADDED
# ============================================================================
# Program: Smart Home Automation System - Event Loop Scheduling
# Description: Demonstrates asyncio event loop with call_soon and call_later
#              using a real-life smart home scenario where different devices
#              are controlled in a rotating schedule.
# ============================================================================

import asyncio
import time
import random


def check_security_system(end_time, loop):
    """
    Task A: Security System Check
    
    Real-life scenario: Smart home security system performs periodic checks
    - Checks door/window sensors
    - Verifies camera feeds
    - Updates security status
    
    Args:
        end_time: Time when the automation cycle should end
        loop: The asyncio event loop
    """
    print("🔒 [SECURITY] Checking all door and window sensors...")
    
    # Simulate sensor check time (1-3 seconds)
    check_time = random.randint(1, 3)
    time.sleep(check_time)
    print(f"   ✓ Security check completed in {check_time}s - All sensors OK!")
    
    # Schedule next task if time permits
    if (loop.time() + 1.0) < end_time:
        print("   → Scheduling: Temperature Control in 1 second...\n")
        loop.call_later(1, adjust_temperature, end_time, loop)
    else:
        print("\n⏰ Automation cycle complete. Shutting down...")
        loop.stop()


def adjust_temperature(end_time, loop):
    """
    Task B: Temperature Control
    
    Real-life scenario: Smart thermostat adjusts home temperature
    - Reads current temperature
    - Adjusts heating/cooling
    - Maintains comfort level
    
    Args:
        end_time: Time when the automation cycle should end
        loop: The asyncio event loop
    """
    current_temp = random.randint(18, 28)
    target_temp = 22
    
    print(f"🌡️  [THERMOSTAT] Current temperature: {current_temp}°C")
    
    # Simulate adjustment time (1-3 seconds)
    adjust_time = random.randint(1, 3)
    time.sleep(adjust_time)
    
    if current_temp < target_temp:
        print(f"   ✓ Heating activated! Adjusting to {target_temp}°C (took {adjust_time}s)")
    elif current_temp > target_temp:
        print(f"   ✓ Cooling activated! Adjusting to {target_temp}°C (took {adjust_time}s)")
    else:
        print(f"   ✓ Temperature is perfect at {target_temp}°C!")
    
    # Schedule next task if time permits
    if (loop.time() + 1.0) < end_time:
        print("   → Scheduling: Lighting Control in 1 second...\n")
        loop.call_later(1, control_lights, end_time, loop)
    else:
        print("\n⏰ Automation cycle complete. Shutting down...")
        loop.stop()


def control_lights(end_time, loop):
    """
    Task C: Smart Lighting Control
    
    Real-life scenario: Smart lighting system manages home lights
    - Checks ambient light levels
    - Adjusts brightness
    - Manages energy efficiency
    
    Args:
        end_time: Time when the automation cycle should end
        loop: The asyncio event loop
    """
    rooms = ["Living Room", "Bedroom", "Kitchen", "Bathroom"]
    selected_room = random.choice(rooms)
    brightness = random.randint(0, 100)
    
    print(f"💡 [LIGHTS] Checking {selected_room} lighting...")
    
    # Simulate light adjustment time (1-3 seconds)
    adjust_time = random.randint(1, 3)
    time.sleep(adjust_time)
    
    print(f"   ✓ {selected_room} brightness set to {brightness}% (took {adjust_time}s)")
    
    # Schedule next task (back to security) if time permits
    if (loop.time() + 1.0) < end_time:
        print("   → Scheduling: Security Check in 1 second...\n")
        print("-" * 50)
        loop.call_later(1, check_security_system, end_time, loop)
    else:
        print("\n⏰ Automation cycle complete. Shutting down...")
        loop.stop()


if __name__ == '__main__':
    print("=" * 60)
    print("    SMART HOME AUTOMATION SYSTEM")
    print("    Using Asyncio Event Loop Scheduling")
    print("=" * 60)
    print("\nThis system rotates between three smart home tasks:")
    print("  1. 🔒 Security System Check")
    print("  2. 🌡️  Temperature Control")
    print("  3. 💡 Lighting Control")
    print("\nRunning automation cycle for 30 seconds...")
    print("=" * 60 + "\n")
    
    # Create the event loop
    loop = asyncio.get_event_loop()
    
    # Set automation to run for 30 seconds (reduced from 60 for demo)
    end_loop = loop.time() + 30
    
    # Start with security check immediately using call_soon
    loop.call_soon(check_security_system, end_loop, loop)
    
    # Run the event loop until stop() is called
    loop.run_forever()
    
    # Clean up
    loop.close()
    
    print("\n" + "=" * 60)
    print("    SMART HOME AUTOMATION STOPPED")
    print("    All systems in standby mode")
    print("=" * 60)
