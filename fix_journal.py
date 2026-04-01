import os

filepath = '.jules/palette.md'

if not os.path.exists(filepath):
    print("File doesn't exist.")
else:
    with open(filepath, 'r') as f:
        content = f.read()

    new_content = """## 2024-04-01 - Accessible and Performant UI Logging
**Learning:** Using a `TextBlock` for frequent text updates causes O(N^2) memory allocations and lacks screen reader accessibility out-of-the-box.
**Action:** Use a `TextBox` with `Background="Transparent"`, `BorderThickness="0"`, and `IsReadOnly="True"` to visually mimic a `TextBlock`. Use `.AppendText()` for updates, and apply `AutomationProperties.Name` and `ToolTip` to ensure accessibility for screen readers.
"""

    if content.strip() == new_content.strip():
        print("Journal looks correct.")
    else:
        # Check if we overwrote. Let's see original content from git.
        os.system('git checkout origin/main -- .jules/palette.md 2>/dev/null || git checkout HEAD~1 -- .jules/palette.md 2>/dev/null || true')
