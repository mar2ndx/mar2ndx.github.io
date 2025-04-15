---
title: 【Tech】 HTTP learning notes (1/3) all about http
category: unknown
tags: technology
comments: true
date: 2015-06-06 00:00:00
---


# _图解 http_读书笔记

_[HTTP の教科書](http://www.amazon.co.jp/HTTP%E3%81%AE%E6%95%99%E7%A7%91%E6%9B%B8-%E4%B8%8A%E9%87%8E-%E5%AE%A3/dp/479812625X)_ by Tricorder CEO 上野宣

# Foundamentals

## 1989, birth of HTTP

[Tim Berners-Lee first proposed the "WorldWideWeb" project in 1989](http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#History) — now known as the World Wide Web. The first version of the protocol had only one method, namely GET, which would request a page from a server.
 
1991, HTTP/0.9 现在的HTTP其实含有HTTP1.0之前版本的意思,因此被称为HTTP/0.9。

1996 HTTP/1.0, rfc1945. widely used today. 

1997 HTTP/1.1, rfc2068, and later released updates with rfc2616. 

today, HTTP/2.0 is under dev.

1994 - 2000 is the time for Browser War between IE and Netscape Navigator. 

2004 - now, the war started again as Mozilla released Firefox. 

## HTTP versions

HTTP/1.0 defined GET, POST and HEAD methods and HTTP/1.1 added 5 new methods: OPTIONS, PUT, DELETE, TRACE and CONNECT. 

In HTTP/0.9 and 1.0, the connection is closed after a single request/response pair. In HTTP/1.1 a keep-alive-mechanism was introduced, where a connection could be reused for more than one request. (client does not need to re-negotiate the TCP 3-Way-Handshake connection after the first request)

> 当年 HTTP 协议的出现主要是为了解决文本传输的难题。由于协议本 身非常简单,于是在此基础上设想了很多应用方法并投入了实际使用。现 在 HTTP 协议已经超出了 Web 这个框架的局限,被运用到了各种场景里。

# TCP/IP 

1. application layer
1. transport (tcp/udp) layer
1. internet (ip) layer
1. data link (ethernet/fddi) layer

## 应用层

应用层决定了向用户提供应用服务时通信的活动。

TCP/IP 协议族内预存了各类通用的应用服务。比如,FTP(File Transfer Protocol,文件传输协议)和 DNS(Domain Name System, 域名系统)服务就是其中两类。

HTTP 协议也处于该层。

## 传输层

传输层提供处于网络连接中的两台计算机之间的数据传输。

## 网络层

网络层用来处理在网络上流动的数据包。

数据包是网络传输的最小数据单位。该层规定了通过怎样的路径(所谓的传输路线)到达对 方计算机,并把数据包传送给对方。 

与对方计算机之间通过多台计算机或网络设备进行传输时,网络层所起的作用就是在众多的选项内选择一条传输路线。

## 链路层(又名数据链路层)

用来处理连接网络的硬件部分。包括控制操作系统、硬件的设备驱 动、NIC(Network Interface Card,网络适配器,即网卡),及光纤等

{<1>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-06-06%20at%2012.33.28%20AM.png)

## more on IP

IP 协议的作用是把各种数据包传送给对方。

IP 地址指明了节点被分配到的地址,MAC 地址是指网卡所属的固 定地址。IP 地址可以和 MAC 地址进行配对。IP 地址可变换,但 MAC 地址基本上不会更改。

### IP 间的通信依赖 MAC 地址。

经过多台计算机和网络设备中转才 能连接到对方。而在进行中转时,会利用下一站中转设备的 MAC 地址 来搜索下一个中转目标。

这时,会采用 ARP 协议(Address Resolution Protocol)。ARP 是一种用以解析地址的协议,根据通信方的 IP 地址就可以反查出对应的 MAC 地址。

### routing

在到达通信目标前的中转过程中,那些计算机和路由器等网络设备 只能获悉很粗略的传输路线。
这种机制称为路由选择(routing),有点像快递公司的送货过程。

## more on TCP and DNS

为了准确无误地将数据送达目标处,TCP 协议采用了三次握手 (three-way handshaking)策略。

用 TCP 协议把数据包送出去后,TCP 不会对传送后的情况置之不理,它一定会向对方确认是否成功送达。握 手过程中使用了 TCP 的标志(flag)——SYN(synchronize)和 ACK( acknowledgement)。

DNS(Domain Name System)服务是和 HTTP 协议一样位于应用层

## dry run

{<2>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-06-06%20at%2012.53.44%20AM.png)

# the basics of HTTP protocol

在两台计算机之间使用 HTTP 协议通信时,在一条通信线路上必定 有一端是客户端,另一端则是服务器端。

有时候,按实际情况,两台计算机角色可能会互换。但就仅从一条通信路线来说,服务器端和客户端的角色是 确定的。

## request

{<3>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-06-06%20at%2012.58.05%20AM.png)

## response

{<4>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-06-06%20at%2012.58.11%20AM.png)

## stateless

HTTP 是一种不保存状态,即无状态(stateless)协议。

HTTP/1.1 虽然是无状态协议,但为了实现期望的保持状态功能, 于是引入了 Cookie 技术。有了 Cookie 再用 HTTP 协议通信,就可以管 理状态了。

## 请求 URI 定位资源

In request header, we specify either the full path or the relative path. 

{<5>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-06-06%20at%201.00.49%20AM.png)

## other than GET method

POST: 功能与 GET 很相似,但 POST 的主要目的并不是获取响应的主体内容。

PUT: 传输文件

HEAD: 和 GET 方法一样,只是不返回报文主体部分。用于确认 URI 的有效性及资源更新的日期时间等。

DELETE: HTTP/1.1 的 DELETE 方法本身和 PUT 方法一样不带验证机 制,所以一般的 Web 网站也不使用 DELETE 方法。当配合 Web 应用程 序的验证机制,或遵守 REST 标准时还是有可能会开放使用的。

OPTIONS: 查询针对请求 URI 指定的资源支持的方法。

and TRACE, CONNECT.

{<6>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-06-06%20at%201.07.22%20AM.png)

## HTTP persistent connection

{<7>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-06-06%20at%202.53.44%20AM.png)

随着 HTTP 的普及,文档中包含大量图片的 情况多了起来。每次的请求都会造成无谓的 TCP 连接建立和断开, 增加通信量的开销。

HTTP/1.1 和一部分的 HTTP/1.0 想出 了持久连接(HTTP Persistent Connections,也称为 HTTP keep-alive 或 HTTP connection reuse)的方法。持久连接的特点是,只要任意一端没 有明确提出断开连接,则保持 TCP 连接状态。

{<8>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-06-06%20at%202.55.45%20AM.png)

Under HTTP 1.0, there is [no official specification for how keepalive operates](http://en.wikipedia.org/wiki/HTTP_persistent_connection#HTTP_1.0). It was, in essence, added to an existing protocol. If the client supports keep-alive, it adds an additional header to the request:

	Connection: Keep-Alive

In HTTP 1.1, all connections are considered persistent unless declared otherwise.

## Cookie

Cookie 会根据从服务器端发送的响应报文内的一个叫做 Set-Cookie 的首部字段信息,通知客户端保存 Cookie。

当下次客户端再往该服务器 发送请求时,客户端会自动在请求报文中加入 Cookie 值后发送出去。

{<9>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-06-06%20at%203.25.58%20AM.png)

# Inside a HTTP message

HTTP 报文大致可分为报文首部和报文主体两块。两者由 __最初出现的空行(CR+LF)来划分__。

通常,并不一定要有报文主体。

{<10>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-06-06%20at%203.29.47%20AM.png)

## message vs. entity

HTTP 报文的主体用于传输请求或响应的实体主体。

	HTTP-message   = Request | Response     ; HTTP/1.1 messages

A HTTP-message has >=0 message-headers and may have ONE message-body:

      generic-message = start-line
                        *(message-header CRLF)
                         CRLF
                         [ message-body ]

通常,报文主体等于实体主体。只有当传输中进行编码操作时,实体主体的内容发生变化,才导致它和报文主体产生差异。

So not every HTTP-message has a message-body. But if it has a message-body, then that’s also the entity-body:

      message-body = entity-body
                   | <entity-body encoded as per Transfer-Encoding>

## HTTP compression

HTTP data is compressed before it is sent from the server: 

1. compliant browsers will announce what methods are supported
1. browsers that do not support compliant compression method will download uncompressed data. 
1. The most common compression schemes include gzip and Deflate

## Chunked transfer encoding

Only in version 1.1 of HTTP.

在传输大容量数据时,通过把数据分割 成多块,能够让浏览器逐步显示页面。

这种把实体主体分块的功能称为分块传输编码(Chunked Transfer Coding)。

## multipart

HTTP 协议中也采纳了多部分对象集合,发送的一份报文 主体内可含有多类型实体。通常是在图片或文本文件等上传时使用。

[The following example illustrates "multipart/form-data" encoding](http://www.w3.org/TR/html401/interact/forms.html#h-17.13.4.2). Suppose we have the following form:

    <FORM action="http://server.com/cgi/handle"
           enctype="multipart/form-data"
           method="post">
       <P>
       What is your name? <INPUT type="text" name="submit-name"><BR>
       What files are you sending? <INPUT type="file" name="files"><BR>
       <INPUT type="submit" value="Send"> <INPUT type="reset">
    </FORM>

If the user enters "Larry" in the text input, and selects the text file "file1.txt", the user agent might send back the following data:

    Content-Type: multipart/form-data; boundary=AaB03x

    --AaB03x
    Content-Disposition: form-data; name="submit-name"

    Larry
    --AaB03x
    Content-Disposition: form-data; name="files"; filename="file1.txt"
    Content-Type: text/plain

    ... contents of file1.txt ...
    --AaB03x--

使用 boundary 字符串来划分多部分对象集合指明的各类实体。在 boundary 字符串指定的各个实体的起始行之前插入“--”标记

## HTTP Range Requests

指定范围发送的 请求叫做范围请求(Range Request)。

对一份 10 000 字节大小的资源,如果使用范围请求,可以只请求 5001~10 000 字节内的资源。

[Clients which request byte-serving might do so](http://en.wikipedia.org/wiki/Byte_serving) in cases in which a large file has been only partially delivered and a limited portion of the file is needed in a particular range. 

In the HTTP/1.0 standard, clients were only able to request an entire document. 

## Content negotiation

当浏览器的默认语言为英语或中文,访问相同 URI 的 Web 页面时, 则会显示对应的英语版或中文版的 Web 页面。

{<11>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-06-06%20at%2011.30.18%20AM.png)

Content negotiation makes it possible to serve different versions of a document (or more generally, a resource representation) at the same URI, so that user agents can specify which version fit their capabilities the best. 

# Status codes in HTTP

1. 1xx Informational
2. 2xx Success
3. 3xx Redirection
4. 4xx Client Error
5. 5xx Server Error

Read more at [w3.org](http://www.w3.org/Protocols/HTTP/HTRESP.html)

{<12>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-06-06%20at%201.36.46%20PM.png)

## HTTP 301

当 301、302、303 响应状态码返回时,几乎所有的浏览器都会把 POST 改成 GET,并删除请求报文内的主体,之后请求会自动再次发送。

301、302 标准是禁止将 POST 方法改变成 GET 方法的,但实际使用 时大家都会这么做。

Google recommends using a 301 redirect to change the URL of a page as it is shown in search engine results.

# web server

HTTP/1.1 规范允许一台 HTTP 服务器搭建多个 Web 站点。

即使物理层面只有一台服务器,但只要使用虚拟主机 (VPS) 的功能,则可 以假想已具有多台服务器。

{<13>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-06-06%20at%202.07.04%20PM.png)

在相同的 IP 地址下,由于虚拟主机可以寄存多个不同主机名和域 名的 Web 网站,因此在发送 HTTP 请求时,必须在 Host 首部内完整指 定主机名或域名的 URI。

## 代理

代理是一种有转发功能的应用程序,它扮演了位于服务器和客户端 “中间人”的角色,接收由客户端发送的请求并转发给服务器,同时也接收服务器返回的响应并转发给客户端。

{<14>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-06-06%20at%202.32.34%20PM.png)

there're mainly 2 kinds of proxy:

1. 缓存代理

    代理转发响应时,缓存代理(Caching Proxy)会预先将资源的副本 (缓存)保存在代理服务器上。

    当代理再次接收到对相同资源的请求时,就将之前缓存的资源作为响应返回。

1. 透明代理

    转发请求或响应时,不对报文做任何加工的代理类型被称为透明代 理(Transparent Proxy)。反之,对报文内容进行加工的代理被称为非透明代理。

## 网关

网关是转发其他服务器通信数据的服务器,接收从客户端发送来的 请求时,它就像自己拥有资源的源服务器一样对请求进行处理。

有时客户端可能都不会察觉,自己的通信目标是一个网关。

{<15>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-06-06%20at%202.38.42%20PM.png)

网关的工作机制和代理十分相似。而网关能使通信线路上的服务器 提供非 HTTP 协议服务。(eg. 连接数据库,使用 SQL 语句查询数据。另外,在 Web 购物网站上进行信用卡结算时,网关可以和信用卡结算系统联动。)

## 隧道

HTTP tunneling is a technique by which communications performed using various network protocols are encapsulated using the HTTP protocol. 

{<16>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-06-06%20at%202.47.52%20PM.png)

隧道可按要求建立起一条与其他服务器的通信线路,届时使用 SSL等加密手段进行通信。隧道的目的是确保客户端能与服务器进行安全的 通信。

隧道本身不会去解析 HTTP 请求。隧道会在通信双方断开连接时结束。
