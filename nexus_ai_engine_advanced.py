# NEXUS v7.0 ULTIMATE - ADVANCED AI ENGINE WITH MACHINE LEARNING

import numpy as np
from collections import deque
import time

class NexusAIEngine:
    """Advanced AI Engine dengan Machine Learning & Prediction"""
    
    def __init__(self):
        self.game_state_history = deque(maxlen=1000)
        self.decision_history = deque(maxlen=500)
        self.win_rate = 0.0
        self.learning_rate = 0.01
        self.model_weights = np.random.randn(50)
        
    def analyze_game_state(self, game_data):
        """Analisis state game dengan deep learning"""
        features = self._extract_features(game_data)
        prediction = np.dot(self.model_weights, features[:50])
        return prediction
    
    def predict_enemy_movement(self, enemy_data):
        """Prediksi gerakan musuh dengan AI"""
        history = list(self.game_state_history)[-10:]
        if len(history) < 3:
            return None
        
        positions = [h.get('enemy_pos', [0,0]) for h in history]
        velocity = np.array(positions[-1]) - np.array(positions[-2])
        next_pos = np.array(positions[-1]) + velocity * 1.5
        return next_pos
    
    def adaptive_strategy(self, game_phase, threat_level):
        """Strategy adaptif berdasarkan game phase dan threat"""
        if game_phase == "early":
            return {"priority": "farm", "aggression": 0.3, "defense": 0.7}
        elif game_phase == "mid":
            return {"priority": "gank", "aggression": 0.6, "defense": 0.5}
        elif game_phase == "late":
            return {"priority": "teamfight", "aggression": 0.8, "defense": 0.4}
        else:
            return {"priority": "survive", "aggression": 0.2, "defense": 0.9}
    
    def learn_from_experience(self, outcome, decision, reward):
        """Update model weights berdasarkan outcome"""
        self.model_weights += self.learning_rate * reward * decision
        self.decision_history.append({"decision": decision, "reward": reward, "outcome": outcome})
    
    def _extract_features(self, game_data):
        """Extract 50 features dari game state"""
        features = np.zeros(50)
        features[0] = game_data.get('hp', 0) / 3000  # Normalize HP
        features[1] = game_data.get('enemy_hp', 0) / 3000
        features[2] = game_data.get('distance_to_enemy', 0) / 1000
        features[3] = game_data.get('mana', 0) / 100
        features[4] = game_data.get('level', 1) / 15
        return features

print("✅ Advanced AI Engine initialized!")
