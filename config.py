# ============================================================
# Group Manager Bot
# Author: Pravin (https://github.com/cyberpravin)
# Support: https://t.me/pravin_bio
# Channel: https://t.me/pravin_bio
# YouTube: https://www.youtube.com/@mrhacked2.0
# License: Open-source (keep credits, no resale)
# ============================================================

import os

# Required configurations (loaded from environment variables)
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_URI = os.getenv("MONGO_URI", "")
DB_NAME = os.getenv("DB_NAME", "Cluster0")

# Owner and bot details
OWNER_ID = os.getenv("OWNER_ID", "pravin_bio"))
BOT_USERNAME = os.getenv("BOT_USERNAME", "khatarnak_help_bot")

# Links and visuals
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/KHATARNAK_bothelp")
UPDATE_CHANNEL = os.getenv("UPDATE_CHANNEL", "https://t.me/pravin_bio")
START_IMAGE = os.getenv("START_IMAGE", "https://primitive-olive-coptw1kusn.edgeone.app/file_00000000797c72079bdbb8a6690d59c8.png")
