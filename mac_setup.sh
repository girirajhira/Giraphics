echo "Installing Giraphics Dependencies using Homebrew"

brew install ffmpeg
brew install librsvg
brew install text2svg
brew install mactex
brew install imagemagick

echo "Installing virtualenv"
pip install virtualenv
virtualenv myenv
source myenv/bin/activate

echo "Installing giraphics locally"
pip install -e .
echo "Installation complete"