#!/bin/bash

# -----------------------------
# PyHub Installer
# -----------------------------
# Version: 1.0.0
# Works with main branch if tag does not exist
# -----------------------------

# Set variables
VERSION="1.0.0"                        # Change this for future versioned installers
REPO="https://github.com/SebCodesHere/PyHub"
INSTALL_DIR="$HOME/PyHub"

echo "Installing PyHub v$VERSION..."

# Create install directory
mkdir -p "$INSTALL_DIR"

# Download zip (try tag first, fallback to main branch)
ZIP_URL="$REPO/archive/refs/tags/v$VERSION.zip"
TMP_ZIP="/tmp/pyhub.zip"

echo "Downloading PyHub..."
curl -L "$ZIP_URL" -o "$TMP_ZIP" 2>/dev/null || {
    echo "Tag v$VERSION not found, downloading main branch instead..."
    ZIP_URL="$REPO/archive/refs/heads/main.zip"
    curl -L "$ZIP_URL" -o "$TMP_ZIP" || { echo "Download failed. Exiting."; exit 1; }
}

# Extract zip
echo "Extracting..."
unzip -o "$TMP_ZIP" -d /tmp || { echo "Extraction failed. Exiting."; exit 1; }

# Determine extracted folder name
EXTRACTED_FOLDER=$(unzip -Z -1 "$TMP_ZIP" | head -n1 | cut -d/ -f1)

# Copy files to install directory
rm -rf "$INSTALL_DIR"/*
cp -r "/tmp/$EXTRACTED_FOLDER/"* "$INSTALL_DIR"

# Install dependencies
echo "Installing Python dependencies..."
python3 -m pip install --user pyfiglet requests speedtest-cli

# Create command
echo "Creating global pyhub command..."
mkdir -p "$HOME/.local/bin"
cat <<EOF > "$HOME/.local/bin/pyhub"
#!/bin/bash
python3 $INSTALL_DIR/pyhub.py
EOF
chmod +x "$HOME/.local/bin/pyhub"

# Add to PATH if not already
if ! grep -q ".local/bin" "$HOME/.bashrc"; then
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"
fi

# Finish
echo ""
echo "PyHub v$VERSION installed successfully!"
echo "Restart your terminal or run:"
echo "source ~/.bashrc"
echo ""
echo "Then run:"
echo "pyhub"