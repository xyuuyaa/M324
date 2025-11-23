IMAGE_NAME=my_cpp_app

all: a.out docker

a.out: main.cpp
	g++ main.cpp -o a.out

docker: a.out
	docker build -t $(IMAGE_NAME) .
	# Lösche das lokale ausführbare File nach dem Bau
	rm -f a.out

clean:
	docker rmi -f $(IMAGE_NAME)
