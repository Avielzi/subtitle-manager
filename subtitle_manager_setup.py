#!/usr/bin/env python3
"""
Subtitle Manager — Setup & Dependency Manager
==============================================
Handles: Python check, pip packages, run, and clean uninstall.

Usage:
    python subtitle_manager_setup.py install   # Install dependencies
    python subtitle_manager_setup.py run       # Install (if needed) + launch
    python subtitle_manager_setup.py uninstall # Remove installed packages
    python subtitle_manager_setup.py check     # Check status only
    python subtitle_manager_setup.py           # Interactive menu
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

# ----------------------------
# CONFIG
# ----------------------------

REQUIRED_PACKAGES = {
    'subliminal': 'subliminal',
    'babelfish': 'babelfish',
}

# Track what WE installed (so uninstall doesn't nuke user's existing packages)
INSTALL_MANIFEST = Path(__file__).parent / '.subtitle_manager_installed.txt'
MAIN_SCRIPT = Path(__file__).parent / 'subtitle_manager_gui_single_file_v_1_python.py'

MIN_PYTHON = (3, 8)

# ----------------------------
# HELPERS
# ----------------------------

def color(text, code):
    """ANSI color wrapper — degrades gracefully on Windows without VT."""
    if sys.platform == 'win32':
        try:
            os.system('')  # enable VT100 on Win10+
        except Exception:
            return text
    return f'\033[{code}m{text}\033[0m'

def green(t):  return color(t, '32')
def red(t):    return color(t, '31')
def yellow(t): return color(t, '33')
def bold(t):   return color(t, '1')

def header(text):
    print(f'\n{bold("=" * 50)}')
    print(f'  {bold(text)}')
    print(f'{bold("=" * 50)}\n')

# ----------------------------
# CHECKS
# ----------------------------

def check_python():
    """Verify Python version."""
    v = sys.version_info
    ok = (v.major, v.minor) >= MIN_PYTHON
    label = f'Python {v.major}.{v.minor}.{v.micro}'

    if ok:
        print(f'  [✓] {green(label)} (>= {MIN_PYTHON[0]}.{MIN_PYTHON[1]} required)')
    else:
        print(f'  [✗] {red(label)} — need {MIN_PYTHON[0]}.{MIN_PYTHON[1]}+')
        print(f'      Download: https://www.python.org/downloads/')

    return ok

def check_pip():
    """Verify pip is available."""
    try:
        subprocess.check_output(
            [sys.executable, '-m', 'pip', '--version'],
            stderr=subprocess.STDOUT
        )
        print(f'  [✓] {green("pip available")}')
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print(f'  [✗] {red("pip not found")}')
        print(f'      Try: python -m ensurepip --upgrade')
        return False

def check_tkinter():
    """Verify tkinter is available (comes with Python but not always)."""
    try:
        import tkinter
        print(f'  [✓] {green("tkinter available")}')
        return True
    except ImportError:
        print(f'  [✗] {red("tkinter not found")}')
        if sys.platform == 'linux':
            print(f'      Try: sudo apt install python3-tk')
        elif sys.platform == 'darwin':
            print(f'      Try: brew install python-tk')
        else:
            print(f'      Reinstall Python with tcl/tk support enabled.')
        return False

def check_package(import_name):
    """Check if a Python package is importable."""
    try:
        __import__(import_name)
        return True
    except ImportError:
        return False

def check_packages():
    """Check all required packages."""
    all_ok = True
    for import_name, pip_name in REQUIRED_PACKAGES.items():
        if check_package(import_name):
            print(f'  [✓] {green(pip_name)}')
        else:
            print(f'  [✗] {red(pip_name)} — not installed')
            all_ok = False
    return all_ok

def check_main_script():
    """Check if the main script exists."""
    if MAIN_SCRIPT.exists():
        print(f'  [✓] {green(MAIN_SCRIPT.name)} found')
        return True
    else:
        print(f'  [✗] {red(MAIN_SCRIPT.name)} not found in same directory')
        return False

# ----------------------------
# INSTALL / UNINSTALL
# ----------------------------

def load_manifest():
    """Load list of packages we installed."""
    if INSTALL_MANIFEST.exists():
        return set(INSTALL_MANIFEST.read_text().strip().splitlines())
    return set()

def save_manifest(packages):
    """Save list of packages we installed."""
    INSTALL_MANIFEST.write_text('\n'.join(sorted(packages)))

def install_packages():
    """Install missing packages, track what we add."""
    header('Installing Dependencies')
    
    already_installed = load_manifest()
    newly_installed = set()

    for import_name, pip_name in REQUIRED_PACKAGES.items():
        if check_package(import_name):
            print(f'  {green("✓")} {pip_name} already installed')
            continue

        print(f'  Installing {pip_name}...', end=' ', flush=True)
        try:
            subprocess.check_call(
                [sys.executable, '-m', 'pip', 'install', pip_name],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE
            )
            print(green('OK'))
            newly_installed.add(pip_name)
        except subprocess.CalledProcessError as e:
            print(red('FAILED'))
            print(f'      Error: {e.stderr.decode() if e.stderr else "unknown"}')
            return False

    # Save combined manifest
    all_tracked = already_installed | newly_installed
    if all_tracked:
        save_manifest(all_tracked)

    if newly_installed:
        print(f'\n  Installed: {", ".join(newly_installed)}')
    else:
        print(f'\n  Nothing new to install.')

    return True

def uninstall_packages():
    """Remove only packages WE installed (from manifest)."""
    header('Uninstalling Dependencies')

    tracked = load_manifest()
    if not tracked:
        print('  Nothing to uninstall — no install manifest found.')
        print('  (Only packages installed by this setup script are tracked.)')
        return

    print(f'  Packages to remove: {", ".join(sorted(tracked))}')
    confirm = input(f'\n  Proceed? [y/N]: ').strip().lower()
    if confirm != 'y':
        print('  Cancelled.')
        return

    for pip_name in sorted(tracked):
        print(f'  Removing {pip_name}...', end=' ', flush=True)
        try:
            subprocess.check_call(
                [sys.executable, '-m', 'pip', 'uninstall', '-y', pip_name],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE
            )
            print(green('OK'))
        except subprocess.CalledProcessError:
            print(yellow('SKIPPED (not found or error)'))

    # Clean up manifest and log file
    INSTALL_MANIFEST.unlink(missing_ok=True)
    
    log_file = Path(__file__).parent / 'subtitle_manager.log'
    if log_file.exists():
        remove_log = input(f'  Also delete {log_file.name}? [y/N]: ').strip().lower()
        if remove_log == 'y':
            log_file.unlink()
            print(f'  {green("Log file removed.")}')

    print(f'\n  {green("Uninstall complete.")}')

# ----------------------------
# RUN
# ----------------------------

def run_app():
    """Install if needed, then launch the GUI."""
    header('Launching Subtitle Manager')

    if not check_python():
        return
    if not check_pip():
        return
    if not check_tkinter():
        return
    if not check_main_script():
        return

    if not check_packages():
        print(f'\n  Missing packages detected. Installing...\n')
        if not install_packages():
            print(red('  Installation failed. Cannot launch.'))
            return

    print(f'  Starting GUI...\n')
    subprocess.Popen([sys.executable, str(MAIN_SCRIPT)])

# ----------------------------
# STATUS
# ----------------------------

def full_check():
    """Run all checks and print status."""
    header('System Check')

    print(bold('  Environment:'))
    py_ok = check_python()
    pip_ok = check_pip()
    tk_ok = check_tkinter()

    print(f'\n{bold("  Packages:")}')
    pkg_ok = check_packages()

    print(f'\n{bold("  Files:")}')
    script_ok = check_main_script()

    manifest = load_manifest()
    if manifest:
        print(f'\n{bold("  Install manifest:")}')
        for p in sorted(manifest):
            print(f'    • {p}')

    all_ok = py_ok and pip_ok and tk_ok and pkg_ok and script_ok
    print()
    if all_ok:
        print(f'  {green("All checks passed. Ready to run.")}')
    else:
        print(f'  {yellow("Some checks failed. Run: python subtitle_manager_setup.py install")}')

    return all_ok

# ----------------------------
# INTERACTIVE MENU
# ----------------------------

def menu():
    header('Subtitle Manager — Setup')

    print('  1) Check status')
    print('  2) Install dependencies')
    print('  3) Run application')
    print('  4) Uninstall (clean removal)')
    print('  5) Exit')
    print()

    choice = input('  Choose [1-5]: ').strip()

    if choice == '1':
        full_check()
    elif choice == '2':
        if not check_python() or not check_pip():
            return
        install_packages()
    elif choice == '3':
        run_app()
    elif choice == '4':
        uninstall_packages()
    elif choice == '5':
        print('  Bye!')
    else:
        print(red('  Invalid choice.'))

# ----------------------------
# CLI ENTRY
# ----------------------------

if __name__ == '__main__':
    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()
        if cmd == 'install':
            if check_python() and check_pip():
                install_packages()
        elif cmd == 'run':
            run_app()
        elif cmd == 'uninstall':
            uninstall_packages()
        elif cmd == 'check':
            full_check()
        else:
            print(f'Unknown command: {cmd}')
            print(__doc__)
    else:
        menu()
