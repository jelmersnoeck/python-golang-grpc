FROM golang:1.7.4

COPY . /go/src/golang
RUN go get -d -v golang

WORKDIR /go/src/golang

CMD ["go", "run", "main.go"]
