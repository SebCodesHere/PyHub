#!/bin/bash

VERSION="1.5.0.B2"
REPO="https://github.com/SebCodesHere/PyHub"
INSTALL_DIR="$HOME/PyHub"

echo "Installing PyHub $VERSION..."

mkdir -p "$INSTALL_DIR"

echo "Downloading PyHub release $VERSION..."
curl -L "$REPO/archive/refs/tags/$VERSION.zip" -o /tmp/pyhub.zip || { echo "Download failed"; exit 1; }

echo "Extracting..."
unzip -o /tmp/pyhub.zip -d /tmp || { echo "Extraction failed"; exit 1; }

EXTRACTED_FOLDER="PyHub-$VERSION"

rm -rf "$INSTALL_DIR"/*
cp -r "/tmp/$EXTRACTED_FOLDER/"* "$INSTALL_DIR"

echo "Installing dependencies..."
python3 -m pip install --user pyfiglet requests speedtest-cli colorama

mkdir -p "$HOME/.local/bin"
cat <<EOF > "$HOME/.local/bin/pyhub"
#!/bin/bash
python3 $INSTALL_DIR/pyhub.py
EOF

chmod +x "$HOME/.local/bin/pyhub"

if ! grep -q ".local/bin" "$HOME/.bashrc"; then
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"
fi

echo ""
echo "PyHub installed! Restart your terminal or run:"
echo "source ~/.bashrc"
echo "Then run: pyhub"