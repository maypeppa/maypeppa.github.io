all:runnable_so.exe \
	test_spirit.exe \
	test_bind.exe \
	test_ptree.exe \
	test_pye.so \
	ob_math_pic.exe

PYTHON=/usr/include/python2.7/
CXXFLAGS=-std=c++11 -fPIC -g -O2
runnable_so.exe:runnable_so.o
	g++ -o $@ $^ -shared -e so_main
%.exe:%.o
	g++ -o $@ $^

%.o:%.cc
	g++ -o $@ -c $^ $(CXXFLAGS)

test_pye.o:test_pye.cc
	g++ -o $@ -c $^ $(CXXFLAGS) -I$(PYTHON)
test_pye.so: test_pye.o
	g++ -o $@ $^ -shared -lboost_python

clean:
	rm -rf *.exe *.o *.so
