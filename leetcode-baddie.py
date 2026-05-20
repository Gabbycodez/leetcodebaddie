# Leetcode Baddie — Full Python CLI Tracker (Upgraded)
#I had the idea and Chat GPT helped me build it out. This is a more polished version of the original script, with better structure, error handling, and a JSON-based progress tracking system.
import os
import json
import subprocess
from datetime import datetime, timedelta
from colorama import init, Fore

init(autoreset=True)

CONFIG_FILE = "leetcode_config.json"


# -----------------------------
# CONFIG HELPERS
# -----------------------------

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {}

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)


config = load_config()

# -----------------------------
# FIRST TIME SETUP
# -----------------------------

if "repo_url" not in config:
    print(Fore.CYAN + "🔥 First-time setup: Leetcode Baddie")

    repo_url = input("Enter your GitHub repo URL: ").strip()
    config["repo_url"] = repo_url

    repo_name = repo_url.split("/")[-1].replace(".git", "")
    local_path = os.path.join(os.getcwd(), repo_name)

    config["local_path"] = local_path
    save_config(config)

# -----------------------------
# AUTO CLONE IF NEEDED
# -----------------------------

repo_url = config["repo_url"]
repo_path = config["local_path"]

if not os.path.exists(repo_path):
    print(Fore.YELLOW + "📦 Cloning repo...")
    subprocess.run(["git", "clone", repo_url, repo_path])
else:
    print(Fore.GREEN + "✔ Repo already exists locally")

os.chdir(repo_path)

# -----------------------------
# INPUT
# -----------------------------

problem_name = input("\nEnter Leetcode problem name: ").strip()
difficulty = input("Difficulty (Easy/Medium/Hard): ").strip().capitalize()
extension = input("File extension (py/cpp/js/java): ").strip().lower()

print("\nPaste solution (press enter and type END to finish):")

lines = []
while True:
    line = input()
    if line == "END" or line == "end":
        break
    lines.append(line)

solution = "\n".join(lines)

# -----------------------------
# SAVE FILE
# -----------------------------

folder = os.path.join(repo_path, difficulty)
os.makedirs(folder, exist_ok=True)

safe_name = problem_name.replace(" ", "_").replace("/", "_")
file_path = os.path.join(folder, f"{safe_name}.{extension}")

with open(file_path, "w") as f:
    f.write(solution)

print(Fore.GREEN + f"💾 Saved: {file_path}")

# -----------------------------
# STATS + STREAK SYSTEM
# -----------------------------

stats_file = os.path.join(repo_path, "progress.json")

today = datetime.now().strftime("%Y-%m-%d")
yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

if os.path.exists(stats_file):
    with open(stats_file, "r") as f:
        stats = json.load(f)
else:
    stats = {
        "total": 0,
        "Easy": 0,
        "Medium": 0,
        "Hard": 0,
        "streak": 0,
        "last_date": None,
        "problems": []
    }

# streak logic
if stats["last_date"] == today:
    pass
elif stats["last_date"] == yesterday:
    stats["streak"] += 1
else:
    stats["streak"] = 1

stats["last_date"] = today

# update stats
stats["total"] += 1
stats[difficulty] += 1

stats["problems"].append({
    "name": problem_name,
    "difficulty": difficulty,
    "file": f"{difficulty}/{safe_name}.{extension}",
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
})

with open(stats_file, "w") as f:
    json.dump(stats, f, indent=4)

print(Fore.YELLOW + f"📊 Stats updated | 🔥 Streak: {stats['streak']}")

# -----------------------------
# README UPDATE
# -----------------------------

readme = os.path.join(repo_path, "README.md")

entry = f"- {problem_name} | {difficulty} | {today}\n"

if not os.path.exists(readme):
    with open(readme, "w") as f:
        f.write("# Leetcode Progress\n\n## Solved Problems\n\n")

with open(readme, "a") as f:
    f.write(entry)

print("📝 README updated")

# -----------------------------
# GIT AUTO SYNC (FULLY AUTOMATED)
# -----------------------------

print(Fore.CYAN + "\n🔄 Syncing with GitHub...")

# stage changes
subprocess.run(["git", "add", "."])

# commit
commit_msg = f"{problem_name} ({difficulty}) - {today}"
subprocess.run(["git", "commit", "-m", commit_msg])

# pull safely (prevents conflicts)
subprocess.run(["git", "pull", "origin", "main", "--rebase", "--autostash"])

# push
subprocess.run(["git", "push", "origin", "main"])

print(Fore.MAGENTA + "\n🚀 Push complete!")
print(Fore.CYAN + f"🔥 Current streak: {stats['streak']}")
print("Done.")