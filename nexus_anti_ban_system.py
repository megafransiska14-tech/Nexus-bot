# NEXUS v7.0 ULTIMATE - ANTI-BAN SECURITY LAYER

import random
import time

class NexusAntiBanSystem:
    """Anti-Ban System untuk menghindari deteksi Moonton"""
    
    def __init__(self):
        self.behavior_pattern = []
        self.last_action_time = time.time()
        self.action_delay_variance = 0.2  # 20% variance
        
    def humanize_action_timing(self, base_delay):
        """Tambah human-like delay pada setiap action"""
        variance = random.uniform(-self.action_delay_variance, self.action_delay_variance)
        actual_delay = base_delay * (1 + variance)
        return max(0.1, actual_delay)  # Minimum 0.1 second
    
    def random_idle_behavior(self):
        """Random idle behavior untuk terlihat natural"""
        if random.random() < 0.05:  # 5% chance
            idle_duration = random.uniform(1, 3)
            return {"action": "idle", "duration": idle_duration}
        return None
    
    def simulate_human_mistakes(self):
        """Simulasi human mistakes untuk terlihat natural"""
        if random.random() < 0.02:  # 2% chance
            return {"action": "mistake", "type": random.choice(["wrong_skill", "misclick", "late_dodge"])}
        return None
    
    def check_detection_risk(self, play_time_hours):
        """Check risk level berdasarkan play time"""
        if play_time_hours > 12:
            return "HIGH"
        elif play_time_hours > 8:
            return "MEDIUM"
        else:
            return "LOW"
    
    def rotate_device_fingerprint(self):
        """Rotate device fingerprint untuk menghindari ban"""
        return {
            "device_id": f"device_{random.randint(10000, 99999)}",
            "mac_address": f"{random.randint(0,255):02x}:{random.randint(0,255):02x}:{random.randint(0,255):02x}:{random.randint(0,255):02x}:{random.randint(0,255):02x}:{random.randint(0,255):02x}",
            "build_fingerprint": f"build_{random.randint(1000, 9999)}"
        }

print("✅ Anti-Ban System initialized!")
