# Sale-Hoard

**Automated Desktop Listing System Powered by ChatGPT o4**

## Overview
Sale-Hoard automates the entire product listing process using image uploads, ChatGPT o4 Desktop Assistant Mode, and browser automation—no external APIs required.

---

## 🧠 Core Workflow

1. **Android App Uploads Images** to cloud folder.
2. **ChatGPT o4 Desktop Assistant**:
   - Analyzes images.
   - Groups products.
   - Generates optimized titles, descriptions, price estimates.
3. **User Reviews Listings** in Android App.
4. **ChatGPT o4 Automates Listing** across eBay, Etsy, Mercari, Facebook, etc.
5. **Completion Notification Sent** back to app with listing URLs.

---

## 📦 Key Modules (Planned)

- `image-analysis/`
  - Vision-based product recognition + grouping
- `listing-generator/`
  - SEO-rich title/description/pricing logic
- `desktop-automation/`
  - Marketplace automation scripts (eBay, Etsy, Mercari, Facebook)
- `integration/`
  - Shared folder sync / confirmation handlers
- `android-app-api/`
  - Receives listings and sends back confirmations

---

## 🔐 Security
- Credentials are encrypted and stored locally via o4 Assistant.
- Secure HTTPS sync with app for confirmations.

---

## 🚀 Goals
- No APIs required — 100% desktop automation
- Auto-classify, group, and price from images
- Fully autonomous, scalable, and secure
