# 🚀 NEXUS v6.0 - Multi-Game AFK Bot

**NEXUS v6.0** adalah bot otomasi game Android yang mendukung **Mobile Legends** dan **FC Mobile** dengan fitur **24/7 AFK**, **multi-account**, dan **intelligent detection system**.

## ⚠️ DISCLAIMER

**Bot ini melanggar Terms of Service (ToS) dari Moonton (Mobile Legends) dan EA (FC Mobile).**

Dengan menggunakan bot ini, Anda menerima risiko:
- ❌ Ban akun permanen
- ❌ Kehilangan semua progress dan item
- ❌ Tidak bisa claim reward

**Kami tidak bertanggung jawab atas konsekuensi penggunaan bot ini.**

---

## 🎯 Fitur Utama

| Fitur | Status |
|-------|--------|
| Multi-game (MLBB + FC Mobile) | ✅ |
| 24/7 AFK Operation | ✅ |
| AFK Scheduler (Set Jam) | ✅ |
| Multi-Account Support (up to 5) | ✅ |
| Performance Optimizer | ✅ |
| Anti-Detection System | ✅ |
| Accessibility Service (No Root) | ✅ |
| Real-time Dashboard | ✅ |
| Comprehensive Logging | ✅ |

---

## 📦 Instalasi

### Opsi 1: Download APK (Recommended)

1. Buka **GitHub Releases** di repository ini
2. Download file `app-release.apk` terbaru
3. Transfer ke HP OPPO Anda
4. Install APK
5. Enable Accessibility Service di Settings

### Opsi 2: Build Sendiri

```bash
git clone https://github.com/yourusername/nexus-bot.git
cd nexus-bot
./gradlew assembleRelease
```

APK akan tersimpan di: `app/build/outputs/apk/release/app-release.apk`

---

## 🔧 Setup Awal

### 1. Enable Unknown Sources
Settings → Security → Unknown Sources → Enable

### 2. Enable Accessibility Service
Settings → Accessibility → Accessibility Services → NEXUS AFK Bot → Enable

### 3. Disable Battery Optimization
Settings → Battery → Battery Optimization → NEXUS AFK Bot → Don't Optimize

### 4. Setup Schedule
Buka NEXUS App → Schedule → Set Start & End Time

---

## 🎮 Cara Menggunakan

### Untuk Mobile Legends:
1. Buka game ML
2. Login dengan akun yang ingin di-automate
3. Pastikan di Lobby
4. Buka NEXUS App → Add Account → Select "Mobile Legends"
5. Tap "START BOT"

### Untuk FC Mobile:
1. Buka game FC Mobile
2. Login dengan akun Anda
3. Pastikan di Main Menu
4. Buka NEXUS App → Add Account → Select "FC Mobile"
5. Tap "START BOT"

---

## ⏰ Schedule Examples

### Night AFK (22:00 - 08:00)
```
Start: 22:00 (10 PM)
End: 08:00 (8 AM)
Duration: 10 jam per malam
```

### 24/7 Mode
```
Start: 00:00
End: 23:59
Duration: 24 jam
```

---

## 🛠️ Teknologi

- **Language**: Java
- **Framework**: Android Accessibility Service
- **Min SDK**: Android 7.0 (API 24)
- **Target SDK**: Android 13 (API 33)
- **Build Tool**: Gradle 7.3.0

---

## 📊 Modul Utama

### 1. NexusAFKService
Main accessibility service yang menjalankan bot logic

### 2. GameDetector
Deteksi game, state, dan elemen penting (skill, enemy, minion, HP)

### 3. AFKController
Handle semua action (tap, swipe, dodge, attack, retreat)

### 4. SchedulerManager
Manage jadwal AFK (set jam mulai-selesai)

### 5. PerformanceMonitor
Monitor CPU, Memory, Battery usage

### 6. MultiAccountManager
Manage multiple akun (up to 5)

---

## 🔐 Security & Privacy

- ✅ All data stored locally on device
- ✅ No data sent to external servers
- ✅ No personal information collected
- ✅ Open source - you can review the code

---

## 📝 Changelog

### v6.0 (Latest)
- ✅ Multi-game support (MLBB + FC Mobile)
- ✅ AFK Scheduler
- ✅ Multi-account manager
- ✅ Performance optimizer
- ✅ Anti-detection system
- ✅ Real-time dashboard
- ✅ Advanced logging

### v5.0
- MLBB only
- Basic AFK logic
- Single account

---

## 🐛 Troubleshooting

### Accessibility Service tidak bisa di-enable
1. Settings → Apps → NEXUS
2. Permissions → Accessibility
3. Enable "Accessibility Service"
4. Restart app

### Bot tidak detect game
1. Pastikan game sudah terbuka
2. Pastikan di Lobby (bukan loading/match)
3. Restart NEXUS app
4. Coba ulang

### Bot jalan tapi tidak ada action
1. Check Accessibility Service (harus enabled)
2. Check Battery Optimization (harus disabled)
3. Check Notification permission
4. Restart HP

---

## 📞 Support

Untuk pertanyaan atau masalah:
1. Check Logs di NEXUS App
2. Read Setup Guide di `/docs/NEXUS_v6_SETUP_GUIDE.md`
3. Open GitHub Issue

---

## ⚖️ Legal

**NEXUS v6.0 adalah tool edukasi untuk research purposes.**

Penggunaan bot ini untuk farming/grinding di game online melanggar ToS dan dapat mengakibatkan:
- Ban akun
- Kehilangan data
- Tindakan hukum dari publisher

**Gunakan dengan bijak dan pada risiko Anda sendiri.**

---

## 📄 License

MIT License - See LICENSE file for details

---

## 🙏 Credits

Developed by: **Manus AI**
Date: 2026-03-31
Version: 6.0

---

**⚠️ REMEMBER: Use at your own risk!**

**NEXUS v6.0 - Multi-Game AFK Bot**
