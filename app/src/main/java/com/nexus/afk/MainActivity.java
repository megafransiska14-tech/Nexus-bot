package com.nexus.afk;

import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;
import android.widget.ScrollView;
import android.widget.LinearLayout;
import android.content.Intent;
import android.provider.Settings;
import android.util.Log;
import androidx.appcompat.app.AppCompatActivity;

/**
 * NEXUS v7.0 ULTIMATE - PHOENIX EDITION
 * Main Activity dengan Dashboard Lengkap
 */
public class MainActivity extends AppCompatActivity {
    
    private static final String TAG = "NEXUS_MAIN";
    private TextView statusText;
    private LinearLayout logContainer;
    private NexusEngine nexusEngine;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        Log.d(TAG, "╔════════════════════════════════════════╗");
        Log.d(TAG, "║  NEXUS v7.0 ULTIMATE - PHOENIX        ║");
        Log.d(TAG, "║  Advanced AFK Bot with AI Engine      ║");
        Log.d(TAG, "╚════════════════════════════════════════╝");
        
        initializeUI();
        nexusEngine = new NexusEngine(this);
        
        checkAccessibilityService();
    }
    
    private void initializeUI() {
        statusText = findViewById(R.id.statusText);
        logContainer = findViewById(R.id.logContainer);
        
        // START MLBB
        Button startMLBB = findViewById(R.id.btnStartMLBB);
        startMLBB.setOnClickListener(v -> {
            nexusEngine.startMLBB();
            addLog("🚀 MLBB Bot Started");
        });
        
        // AUTO FARM
        Button autoFarm = findViewById(R.id.btnAutoFarm);
        autoFarm.setOnClickListener(v -> {
            nexusEngine.startAutoFarm();
            addLog("🌾 Auto Farm Mode Activated");
        });
        
        // STOP BOT
        Button stopBot = findViewById(R.id.btnStop);
        stopBot.setOnClickListener(v -> {
            nexusEngine.stopBot();
            addLog("⏹️ Bot Stopped");
        });
        
        // TROLL VOICE BUTTONS
        Button trollCewek = findViewById(R.id.btnTrollCewek);
        trollCewek.setOnClickListener(v -> {
            nexusEngine.activateTrollVoice("cewek");
            addLog("🎤 Suara Cewek Activated");
        });
        
        Button trollCowok = findViewById(R.id.btnTrollCowok);
        trollCowok.setOnClickListener(v -> {
            nexusEngine.activateTrollVoice("cowok");
            addLog("🎤 Suara Cowok Deep Activated");
        });
        
        Button trollRobot = findViewById(R.id.btnTrollRobot);
        trollRobot.setOnClickListener(v -> {
            nexusEngine.activateTrollVoice("robot");
            addLog("🤖 Suara Robot Activated");
        });
        
        Button trollMonster = findViewById(R.id.btnTrollMonster);
        trollMonster.setOnClickListener(v -> {
            nexusEngine.activateTrollVoice("monster");
            addLog("👹 Suara Monster Activated");
        });
        
        Button trollBebek = findViewById(R.id.btnTrollBebek);
        trollBebek.setOnClickListener(v -> {
            nexusEngine.activateTrollVoice("bebek");
            addLog("🦆 Suara Bebek Activated");
        });
        
        updateStatus();
    }
    
    private void checkAccessibilityService() {
        if (!isAccessibilityServiceEnabled()) {
            addLog("⚠️ Accessibility Service not enabled!");
            addLog("Go to Settings → Accessibility → NEXUS Bot");
            Intent intent = new Intent(Settings.ACTION_ACCESSIBILITY_SETTINGS);
            startActivity(intent);
        } else {
            addLog("✅ Accessibility Service Enabled");
        }
    }
    
    private boolean isAccessibilityServiceEnabled() {
        int accessibilityEnabled = 0;
        try {
            accessibilityEnabled = Settings.Secure.getInt(
                getContentResolver(),
                Settings.Secure.ACCESSIBILITY_ENABLED
            );
        } catch (Settings.SettingNotFoundException e) {
            Log.e(TAG, "Error checking accessibility: " + e.getMessage());
        }
        return accessibilityEnabled == 1;
    }
    
    private void updateStatus() {
        statusText.setText("NEXUS v7.0 ULTIMATE - PHOENIX EDITION\n" +
                          "Status: Ready\n" +
                          "131 Heroes Database: Loaded\n" +
                          "AI Engine: Active\n" +
                          "Anti-Ban System: Active");
    }
    
    private void addLog(String message) {
        runOnUiThread(() -> {
            TextView logEntry = new TextView(this);
            logEntry.setText("[" + getCurrentTime() + "] " + message);
            logEntry.setTextColor(0xFF00FF41);
            logEntry.setTextSize(12);
            logContainer.addView(logEntry);
            
            // Auto scroll to bottom
            ScrollView scrollView = findViewById(R.id.scrollView);
            scrollView.post(() -> scrollView.fullScroll(ScrollView.FOCUS_DOWN));
        });
    }
    
    private String getCurrentTime() {
        return new java.text.SimpleDateFormat("HH:mm:ss", java.util.Locale.getDefault())
            .format(new java.util.Date());
    }
    
    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (nexusEngine != null) {
            nexusEngine.stopBot();
        }
    }
}
