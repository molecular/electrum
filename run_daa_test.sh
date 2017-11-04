export HOME=tmp
mkdir -p $HOME/.electron-cash
rm -f $HOME/.electron-cash/blockchain_headers
touch $HOME/.electron-cash/blockchain_headers
if 2>&1 python2 test.py; then
	echo "TEST SUCCESSFUL"
else
	echo "TEST FAILED"
fi
