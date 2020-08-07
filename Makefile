build:
	docker build -t fortuna-cookie:latest .

run:
	docker run -it --rm -p 5000:5000 fortuna-cookie:latest 
