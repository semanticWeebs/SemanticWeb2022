build:
	docker build -t semantic-films .
	docker run -h 0.0.0.0 -p 5000:5000 -e PORT=5000 semantic-films

