FROM golang:1.17.3-alpine3.14
WORKDIR /root/
COPY ./app.go ./
RUN go build app.go

FROM alpine:latest
EXPOSE 9000
WORKDIR /root/
COPY --from=0 /root/app ./
CMD ["./app"]