#!/usr/bin/env python3
"""
Sicherer Commit und Push für nebenläufige Agenten.
Verhindert Kollisionen bei .git/index.lock und fängt parallele Pushes mit git pull --rebase ab.
"""

import sys
import os
import time
import subprocess
import argparse

def run_cmd(cmd, check=False, retry_lock=True):
    for attempt in range(20):
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if res.returncode == 0:
            return res
        stderr = res.stderr or ""
        stdout = res.stdout or ""
        combined = stderr + "\n" + stdout
        if retry_lock and ("index.lock" in combined or "lock file" in combined):
            time.sleep(1.0 + 0.5 * attempt)
            continue
        if check:
            print(f"Command failed: {cmd}\nOutput:\n{combined}", file=sys.stderr)
            raise subprocess.CalledProcessError(res.returncode, cmd, res.stdout, res.stderr)
        return res
    return res

def main():
    parser = argparse.ArgumentParser(description="Safely commit and push specific files with retry.")
    parser.add_argument("files", nargs="+", help="Files or directories to add and commit")
    parser.add_argument("-m", "--message", required=True, help="Commit message")
    args = parser.parse_args()

    files_to_add = " ".join(f"'{f}'" for f in args.files)

    # 1. Wait for lock and stage files
    print(f"Staging files: {files_to_add}")
    run_cmd(f"git add {files_to_add}", check=True)

    # 2. Commit
    print(f"Committing with message: {args.message}")
    res = run_cmd(f"git commit -m \"{args.message}\"")
    if res.returncode != 0:
        combined = res.stdout + res.stderr
        if "nothing to commit" in combined or "no changes added to commit" in combined:
            status_res = run_cmd("git rev-list @{u}..HEAD")
            if not status_res.stdout.strip():
                print("Nothing to commit and nothing to push.")
                return 0
            print("Nothing to commit, but unpushed commits exist. Proceeding to push...")
        else:
            print(f"Commit failed: {res.stderr}\n{res.stdout}", file=sys.stderr)
            return res.returncode

    # 3. Pull rebase and Push loop
    for attempt in range(15):
        print(f"Pulling with rebase (attempt {attempt + 1})...")
        pull_res = run_cmd("git pull --rebase --autostash")
        if pull_res.returncode != 0:
            print(f"Pull rebase failed: {pull_res.stderr}", file=sys.stderr)
            time.sleep(2.0)
            continue

        print(f"Pushing to origin main (attempt {attempt + 1})...")
        push_res = run_cmd("git push origin main")
        if push_res.returncode == 0:
            print("Successfully committed and pushed!")
            return 0
        else:
            print(f"Push rejected or failed, retrying in 2s... Details: {push_res.stderr}")
            time.sleep(2.0)

    print("Failed to push after multiple attempts.", file=sys.stderr)
    return 1

if __name__ == "__main__":
    sys.exit(main())
