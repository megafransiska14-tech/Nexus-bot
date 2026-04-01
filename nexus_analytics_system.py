# NEXUS v7.0 ULTIMATE - REAL-TIME ANALYTICS & MONITORING

import time
from datetime import datetime

class NexusAnalytics:
    """Real-time Analytics dan Performance Monitoring"""
    
    def __init__(self):
        self.session_start = time.time()
        self.stats = {
            "total_matches": 0,
            "wins": 0,
            "losses": 0,
            "kills": 0,
            "deaths": 0,
            "assists": 0,
            "gold_earned": 0,
            "damage_dealt": 0,
            "damage_taken": 0,
            "healing": 0,
            "skill_accuracy": 0.0,
            "dodge_success_rate": 0.0,
            "gank_success_rate": 0.0,
        }
        
    def update_match_stats(self, match_data):
        """Update statistik match"""
        self.stats["total_matches"] += 1
        if match_data.get("result") == "win":
            self.stats["wins"] += 1
        else:
            self.stats["losses"] += 1
        
        self.stats["kills"] += match_data.get("kills", 0)
        self.stats["deaths"] += match_data.get("deaths", 0)
        self.stats["assists"] += match_data.get("assists", 0)
        self.stats["gold_earned"] += match_data.get("gold", 0)
        self.stats["damage_dealt"] += match_data.get("damage", 0)
        
    def calculate_win_rate(self):
        """Hitung win rate"""
        if self.stats["total_matches"] == 0:
            return 0.0
        return (self.stats["wins"] / self.stats["total_matches"]) * 100
    
    def calculate_kda(self):
        """Hitung K/D/A ratio"""
        deaths = max(self.stats["deaths"], 1)
        kda = (self.stats["kills"] + self.stats["assists"]) / deaths
        return round(kda, 2)
    
    def get_performance_report(self):
        """Generate performance report"""
        return {
            "win_rate": f"{self.calculate_win_rate():.1f}%",
            "kda": self.calculate_kda(),
            "total_matches": self.stats["total_matches"],
            "avg_gold_per_match": self.stats["gold_earned"] / max(self.stats["total_matches"], 1),
            "avg_damage_per_match": self.stats["damage_dealt"] / max(self.stats["total_matches"], 1),
        }

print("✅ Analytics System initialized!")
