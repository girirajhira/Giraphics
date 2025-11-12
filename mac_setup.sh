echo "Installing Giraphics Dependencies using Homebrew"

brew install ffmpeg
brew install librsvg
brew install text2svg
brew install mactex
brew install imagemagick

echo "Installing virtualenv"
pip install virtualenv
virtualenv girenv
source girenv/bin/activate

echo "Installing giraphics locally"
pip install .
echo "Installation complete"