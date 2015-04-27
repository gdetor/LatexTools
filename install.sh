OPTDIR="/opt/"
DOCDIR="Man/"
MANDIR="/usr/local/man/man1/"

em="emlatex.1"
dl="delatex.1"
wl="wclatex.1"

echo "LatexTools Installation!"
if [ -d "$OPTDIR" ]; then
    echo "Copying files..."
    sudo cp Tools/*.py $OPTDIR
else
    sudo mkdir /opt
    sudo cp Tools/*.py $OPTDIR
fi

echo "Installing man pages..."
sudo install -g 0 -o 0 -m 0644 $DOCDIR$em $MANDIR
sudo gzip $MANDIR$em
sudo install -g 0 -o 0 -m 0644 $DOCDIR$wl $MANDIR
sudo gzip $MANDIR$wl
sudo install -g 0 -o 0 -m 0644 $DOCDIR$dl $MANDIR
sudo gzip $MANDIR$dl
echo "... Done!"
