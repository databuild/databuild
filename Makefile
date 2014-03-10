all:
	pip install -r requirements.txt
	make lupa clean test-install

clean:
	rm -rf lupa-master
	rm -rf master.tar.gz

uninstall:
	/usr/bin/yes | pip uninstall lupa

lupa:
	wget https://github.com/scoder/lupa/archive/master.tar.gz
	tar zxf master.tar.gz
	cd lupa-master/ && ARCHFLAGS="-arch x86_64" python setup.py install --no-luajit

test-install:
	python -c "from lupa import LuaRuntime; lua = LuaRuntime()"
