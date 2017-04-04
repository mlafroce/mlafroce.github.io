all: link

obj: main.cpp
	g++ -c main.cpp

link: obj
	g++ -o tp main.o $(LDFLAGS) 

clean:
	rm *.o tp