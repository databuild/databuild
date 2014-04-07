all:
	pip install --quiet -r requirements.txt
	make lupa clean test-install

clean:
	rm -rf lupa-master
	rm -rf master.tar.gz

uninstall:
	/usr/bin/yes | pip uninstall lupa

lupa:
	pip install https://github.com/scoder/lupa/archive/master.tar.gz

test-install:
	python -c "from lupa import LuaRuntime; lua = LuaRuntime()"
