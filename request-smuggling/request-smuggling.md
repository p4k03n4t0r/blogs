# Request smuggling

With more and more techniques being built on top of others, it’s getting more difficult for a developer to understand what is actually happening when he writes some code. On top of this the DevOps movement is progressing, where a developer is also supposed to know something about the infrastructure the code runs on. I think for a developer knowing how things work under the hood is not always necessary, but it helps choose better solutions and decreases the amount of mistakes made.

In this blog post I’ll be taking a look at request smuggling, which could utilize a wrongly configured proxy to ‘smuggle’ HTTP requests out of the network. For example responses from endpoints which are supposed to be inaccessible from the internet can be smuggled out of the network by a malicious user. I’ll be diving a bit into the HTTP protocol to show how this is possible and I’ll be giving working examples request smuggling via proxies with what it seems like harmless configuration.

## HTTP requests

An HTTP request always follows a specification which can be found in the rfc2616 spec (https://tools.ietf.org/html/rfc2616). This specification describes how HTTP should work in an abstract way and I’ll be referring to it later on. All proxies, webservers and HTTP clients should follow this specification.

An HTTP request can include a body, where the length of this body must be indicated. This can be done in two ways:

- Using the `Content-Length` header, where the value is an integer indicating the amount of characters the body exists of.
- Using chunked encoding, where the `Transfer-Encoding` header has the value `chunked`. The body will be cut up in chunks, where every chunk is preceded by a hexidecimal number indicating the amount of characters the following chunk exists of. The last chunk to indicate the body is finished is empty and has the length `0`
- If both are provided, the chunked encoding takes priority for indicating the length of the body

The body of an HTTP request always begins with an empty line after the headers and also ends with an empty line.

## Abusing HTTP body length

Although the specification seems to be quite clear, it still depends on the developer of the HTTP client and server to implement this correctly. The abstraction of the specification makes it sometimes hard to translate this to code. It could be possible that the specification is interpreted differently between proxies, servers and clients. It would also be possible to interpretate the length of the body of a HTTP request differently. Let's see what we can do with this.

To find out the length of the body, the headers must be interpreted. This seems easy, but as later on will be shown, this isn't always the case.
We would have to find a way to trick
Of course this only applies if both of the headers are aknowledged properly and this depends on how the HTTP server is implemented.
But what will happen if I can trick a proxy into using the content length and the server using chunked encoding? They will have different interpretations of the length of the body:

## Request smuggling using Mitmproxy and Gunicorn

https://github.com/p4k03n4t0r/http-request-smuggling-demo

## Other smuggle techniques

In the example above the proxy uses the `Transfer-Encoding` (TE) header and the server uses the `Content-Length` (CL) header. This is called TE-CL request smuggling, but there are of course more possibilities:

- **CL-TE**: for an example see: https://ctftime.org/writeup/20655
- **CL-CL**: what happens if we supply multiple `Content-Length` headers?
- **TE-TE**: what happens if we supply multiple `Transfer-Encoding` headers?

In this post we played around with the lenght of the body to smuggle an additional request, but there are of course other ways to achieve this. Take for example this post (https://labs.bishopfox.com/tech-blog/h2c-smuggling-request-smuggling-via-http/2-cleartext-h2c), in which is described how upgrading a HTTP/1.1 connection to HTTP/2 allows smuggling of requests.

## Closing notes

I hope this post was interesting to read and allowed you to learn a bit more about the possibilities with techniques which we use every day. By diving into this topic, I myself learned a lot about how HTTP clients and servers work (I also wrote them myself in Python) and how to interpret a IETF specification. Luckily techniques are always evolving and it seems they keep increasing, so there's always more to dive into!
