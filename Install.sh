#!/bin/bash

VERSION="1.0.0"
REPO="https://github.com/YOUR_USERNAME/PyHub"
INSTALL_DIR="$HOME/PyHub"

echo "Installing PyHub v$VERSION"

# create install directory
mkdir -p "$INSTALL_DIR"

# download release
echo "Downloading PyHub..."
curl -L "$REPO/archive/refs/tags/v$VERSION.zip" -o /tmp/pyhub.zip

# extract
echo "Extracting..."
unzip -o /tmp/pyhub.zip -d /tmp

# copy files
rm -rf "$INSTALL_DIR"/*
cp -r /tmp/PyHub-$VERSION/* "$INSTALL_DIR"

# install dependencies
echo "Installing dependencies..."
python3 -m pip install --user pyfiglet requests speedtest-cli

# create command
echo "Creating pyhub command..."
cat <<EOF > "$HOME/.local/bin/pyhub"
#!/bin/bash
python3 $INSTALL_DIR/pyhub.py
EOF

chmod +x "$HOME/.local/bin/pyhub"

# add to PATH if needed
if ! grep -q ".local/bin" "$HOME/.bashrc"; then
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"
fi

echo ""
echo "PyHub v$VERSION installed!"
echo "Restart your terminal or run:"
echo "source ~/.bashrc"
echo ""
echo "Then run:"
echo "pyhub"