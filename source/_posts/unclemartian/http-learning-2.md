---
title: 【Tech】 HTTP learning notes (2/3) security
category: unknown
tags: technology
comments: true
date: 2015-06-06 00:00:00
---


# _图解 http_读书笔记

_[HTTP の教科書](http://www.amazon.co.jp/HTTP%E3%81%AE%E6%95%99%E7%A7%91%E6%9B%B8-%E4%B8%8A%E9%87%8E-%E5%AE%A3/dp/479812625X)_ by Tricorder CEO 上野宣

# HTTPS

## Disadvantages of HTTP:

1. 通信使用明文(不加密),内容可能会被窃听
1. 不验证通信方的身份,因此有可能遭遇伪装
1. 无法证明报文的完整性,所以有可能已遭篡改

按 TCP/IP 协议族的工作机制,通信内容在所有的通信线路上都有可能遭到窥视。

窃听相同段上的通信并非难事。只需要收集在互联网上流动的数据包(帧)就行了。对于收集来的数据包的解析工作,可交给那些抓包(Packet Capture)或嗅探器(Sniffer)工具。

## 1. 内容的加密

把 HTTP 报 文里所含的内容进行加密处理。

由于该方式不同于 SSL 或 TLS 将整个通信线路加密处理,所以内容仍 有被篡改的风险。比如,从某个 Web 网站上下载内容,是无法确定客户端下载的文件和服务器上存放的文件是否前后一致的。文件内容在传输途中可能已 经被篡改为其他的内容。

{<1>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-06-06%20at%204.56.22%20PM.png)

像这样,请求或响应在传输途中,遭攻击者拦截并篡改内容的攻击 称为中间人攻击(Man-in-the-Middle attack,MITM)。

使用 HTTP 协议确定报文完整性的方法,常用MD5 和 SHA-1 等散列值校验的方法,以及用来确认文件的数字签名方法。但事实上并不便捷、可靠。

用户需要手动下载验证文件。浏览器无法自动帮用户检查。

而且PGP 和 MD5 本身被改写的话,用户是没有办法意识到的。

## 2. 通信的加密: TLS/SSL

HTTP 协议中没有加密机制,但可以通 过和 SSL(Secure Socket Layer,安全套接层)或 TLS(Transport Layer Security,安全层传输协议)的组合使用,加密 HTTP 的通信内容。

Transport Layer Security (TLS) and its predecessor, Secure Sockets Layer (SSL), are cryptographic protocols designed to provide communications security over a computer network. 

当使用 SSL 时,它的处理速度会 变慢。一是指通信慢，因为大量的SSL 通信。另一是指由于大量消耗 CPU 及内存等资源,导致处理速度变慢。和使用 HTTP 相比,网络负载可能会变慢 2 到 100 倍。

针对速度变慢这一问题,并没有根本性的解决方案,我们会使用 SSL 加速器这种(专用服务器)硬件来改善该问题。该硬件为 SSL 通信 专用硬件,相对软件来讲,能够提高数倍 SSL 的计算速度。

### Why not HTTPS?

每当那些访问量较多的 Web 网站在进行加密处理时,它们所承 担着的负载不容小觑。并且，使用的证书必须向认证机 构(CA)购买。

## HTTP+ 加密 + 认证 + 完整性保护 =HTTPS

HTTPS 并非是应用层的一种新协议。

1. HTTP: 直接和 TCP 通信。
1. HTTPS: 先和 SSL 通信,再由 SSL 和 TCP 通信了。

简言之,所谓 HTTPS,其实就是 身披 SSL 协议这层外壳的 HTTP。(TLS and SSL encrypt data in the application layer)

SSL 是独立于 HTTP 的协议,所以不光是 HTTP 协议,其他运行在 应用层的 SMTP 和 Telnet 等协议均可配合 SSL 协议使用。可以说 SSL 是当今世界上应用最为广泛的网络安全技术。

## 密钥

1. common key crypto system
1. private/public key

要想根据密文和公开密钥,恢复到信息原文是异常困难的, 因为解密过程就是在对离散对数进行求值,这并非轻而易举就能办到。

### HTTPS 采用混合加密机制

HTTPS 采用共享密钥加密和公开密钥加密两者并用的混合加密机制。
因为公开密钥加密处理速度慢。

在交换密钥环节使用公开密钥加密方式,之后的建立通信交换报文阶段 则使用共享密钥加密方式。

## how HTTPS works

1. 数字证书认证机构(CA,Certificate Authority) 颁发公开密钥证书。

    website 向数字证书认证机构提出公开密钥的申请。CA 在判明提出申请者的身份之后,会对已申请的 public key 做数字签名,然 后分配这个已签名的公开密钥, 并将该公开密钥放入公钥证书后绑定在 一起。

1. client side request this certificate

	website 会将这份由数字证书认证机构颁发的公钥证书发送给客户 端,以进行公开密钥加密方式通信。公钥证书也可叫做数字证书或直接 称为证书。
	
	接到证书的 client browser 可使用数字证书认证机构的公开密钥,对那张证 书上的数字签名进行验证

1. How does client know CA's public key, then?

    多数浏览器开发商发布版 本时,会事先在内部植入常用认证机关的公开密钥。

{<2>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-06-06%20at%209.25.16%20PM.png)

> 2011 年 7 月,荷兰的一家名叫 DigiNotar 的 认证机构曾遭黑客不法入侵,颁布了 google.com 和 twitter.com 等网站 的伪造证书事件。这一事件从根本上撼动了 SSL 的可信度。

{<3>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-06-06%20at%209.28.47%20PM.png)

## SSL 客户端证书

HTTPS 中还可以使用客户端证书。以客户端证书进行客户端认证, 证明服务器正在通信的对方始终是预料之内的客户端, 银行的网上银行就采用了客户端证书。

but it's not widely used because:

1. not everyone likes (or knows how) to install a certificate.
1. certificate costs
1. if you hack into root access, the certificate will be available to you

现状是,安全性极高的认证机构可颁发客户端证书但仅用于特殊用 途的业务。

## 自签名证书

使用 OpenSSL 这套开源程序,每个人都可以构建一套属于自 己的认证机构,从而自己给自己颁发服务器证书。

浏览器访问该服务器时,会显示“无法确认连接安全性”


# Authentication

HTTP/1.1 使用的认证方式:

1. BASIC 认证(基本认证)
1. DIGEST 认证(摘要认证)
1. SSL 客户端认证
1. FormBase 认证(基于表单认证)

## BASIC 认证

since HTTP/1.0

simplest technique for enforcing access controls to web resources because it doesn't require cookies, session identifier and login pages. 现在仍有一部分的网站会使用这种认证方式。

{<4>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-06-06%20at%209.53.21%20PM.png)

The BA mechanism provides no confidentiality protection for the transmitted credentials. They are merely encoded with Base64 in transit, but not encrypted or hashed in any way. 

### Base64

Convert 8-bit-padded (256-based) ASCII characters into Base64 scheme. Which is to say, convert 3 ASCII letters (24 bits) will be encoded into 4 Base64 letter (4 * 6 = 26). 'Man' converts to 'TWFu'. 

{<5>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-06-06%20at%2010.02.13%20PM.png)

在 HTTP 等非加密通信的线路上进行 BASIC 认证的过程中, 如果被人窃听,被盗的可能性极高。另外，browser无
法实现认证注销操作。

Basic Authentication is, therefore, typically used over HTTPS.

## DIGEST 认证

since HTTP/1.1

{<6>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-06-06%20at%2010.23.21%20PM.png)

1. when requested, server 会随着状态码 401 Authorization Required,返回带 WWW-Authenticate 首部字段, which 包含 realm 和 nonce 这两个字段的信息。(nonce 是一种任意随机字符串)。

1. client will return DIGEST 认证必须的首部字段 Authorization 信息, which 包含 username、realm、nonce、uri 和response 的字段信息。其中,realm 和 nonce 就是之前从服务器接收到的响应中的字段。__response 也可叫做 Request-Digest,存放经过 MD5 运算后 的密码字符串,形成响应码__。

1. server 接收到包含首部字段 Authorization 请求, 确认 认证信息，并返回包含 Request-URI 资源的响应。

Technically, digest authentication is an application of MD5 cryptographic hashing with usage of nonce values to prevent replay attacks. It uses the HTTP protocol. 

[Digest access authentication is vulnerable to](http://en.wikipedia.org/wiki/Digest_access_authentication#Disadvantages) a man-in-the-middle (MitM) attack.

## SSL 客户端证书

1. 事先将客户端证书分发给客户 端,且客户端必须安装此证书。
1. when requested, server 发送 Certificate Request 报文,要求客户端提供客户端证书。
1. client send __Client Certificate__.
1. server validate and __retrieve public key of client__, then they start HTTPS.

## Form-based 认证

由于使用上的便利性及安全性问题,HTTP 协议标准提供的 BASIC 认证和 DIGEST 认证几乎不怎么使用。另外,SSL 客户端认证虽然具有 高度的安全等级,但因为导入及维持费用等问题,还尚未普及。

反观，SSH 和 FTP, 服务器与客户端之间的认证是合乎标准规范的, 并且满足了基本的安全需求,因此 widely 使用。

对于 Web 网站的认证功能,能够满足 其安全使用级别的标准规范并不存在,所以只好使用由 Web 应用程序 各自实现基于表单的认证方式。

Form-based 认证的标准规范尚未有定论,__一般会使用 Cookie 来管理 Session(会话)__。

## Session 管理及 Cookie 应用

我们使用 Cookie 来管理 Session,以弥补 HTTP 协议中不存在的状态管理功能。

Usign session id in Cookie is pretty easy process:

{<7>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-06-07%20at%2010.01.47%20AM.png)

1. 客户端把用户 ID 和密码等登录信息放入报文的实体部分, 通常是以 POST 方法把请求发送给服务器。而这时__会使用 HTTPS 通信来进行__ HTML 表单画面的显示和用户输入 数据的发送。

1. 服务器会发放用以识别用户的 Session ID (首部字段 Set-Cookie 内写入 Session ID 如 PHPSESSID=028a8c)。然后把用户的认 证状态与 Session ID 绑定后记录在服务器端(maybe a database, develop end will manage)。

1. 客户端将 Cookie 保存在本地。浏览器下次 会自动发送 Cookie,所以 Session ID 也随之发送到服务器。

You must not lose your session id, otherwise someone can act like they were you. 

Web server will manage __expiration of sessions__. 

To avoid 跨站脚本攻击(XSS), set HTTPonly as TRUE, for session cookie. 

另外

> 一种安全的保存方法是,先利用给密码加盐(salt)的方式
增加额外信息,再使用散列(hash)函数计算出散列值后保存。
>
> salt 其实就是由服务器随机生成的一个字符串,但是要保证长度足够长。把它和密码字符串相连接(前后都可以)生成散 列值。
>
> 当两个用户使用了同一个密码时,由于随机生成的 salt 值不同,对应 的散列值也将是不同的。这样一来,很大程度上减少了密码特征, 攻击者也 就很难利用自己手中的密码特征库进行破解。

## HTTPonly 

HttpOnly cookies can only be used when transmitted via HTTP (or HTTPS). They are not accessible through non-HTTP APIs such as JavaScript. 

[This limits the potential damage many cross site script attacks can cause](http://cookiecontroller.com/internet-cookies/secure-cookies/) – specifically, the attacks that target cookie data.

## Question

### Can we put session id in URL instead of in cookie?

Yes, but definitely not a good practise (even if we send these messages thru HTTPS). [Here is a great post discussing about it](http://security.stackexchange.com/questions/14093/why-is-passing-the-session-id-as-url-parameter-insecure):

1. if you send over a link to someone, he might use your session id and have full access to your account.

1. possibility of __session fixation attacks__, which means hackers send a prepared URL with a known session id to the user, and entice the user to log in. Once user does, hacker would have a session with priviledges. It's not possible with cookies. 

1. putting anything in the URL makes it more likely that it will leak. This can be through a Referer header in a linked resource, from access to the endpoint with browser history records, from brute force history sniffing, inappropriately protected web logs, and so on. 

A little history.

> the reason (session-in-URL) was typically done in the past was to support browsers without cookies enabled. This is less and less a concern these days, and the usability problems of not being to share links, in addition to the session fixation attacks, mean that session-in-URL is usually avoided today.

### Can we sent session id via non-encrypted HTTP?

[For Google, the SSIDcookie is marked with the Secure flag](http://security.stackexchange.com/questions/81998/should-a-session-id-ever-be-sent-over-an-unencrypted-connection). This means that it won't be sent by the browser over a plain HTTP connection.

> [Google] store the important stuff (for example, HSID, NID and SSID) as HTTPonly

However, __(HTTP transfer) may be acceptable for Session IDs that do not allow access to sensitive information__. For example, you may set a cookie so you can let a user add items to their basket. When they proceed to checkout, the insecure session is transferred to secure session over HTTPS. An attacker can only intercept the insecure session and possibly add or change basket items, but once transferred to HTTPS, user can review the basket before placing order. Additionally, all personal details are considered anonymous until the HTTPS checkout is reached.

Google use non secure and non-http only cookies for items in a similar way.

[A suggestion is](http://stackoverflow.com/questions/709085/secure-cookies-and-mixed-https-http-site-usage):

> you should never trust any content sent over a non-secured connection. privacy is seen as more important than ever, even for actions that aren't critical to the authentication, such as writing comments, uploading photos, and more.

> Google announced that HTTPS-only sites will benefit in search engine rankings.

> So... make the whole site use HTTPS. A few years back this might not have been feasible mainly because of CDNs not providing HTTPS support. However, today it's mainly a question of balancing development and operational costs.

### how to manage session if client disables cookie?

[Two way](http://stackoverflow.com/questions/1795998/manage-session-when-broswer-has-disable-cookies). First of which is more standard, that is to __pass session id thru URLs__. This requires developer to append session id to EVERY url. eg. 

    /path/to/page

becomes

    /path/to/page?sessionid=ASDFG-ASDFG-ASDFG-ASDFG-ASDFG

Second way, if to use info in the HTTP header as identifier of the user, i.e: 

> By combining the Http UserAgent, RemoteIp and RemoteXfip you can get close to uniquely identifying a user, but there is no guarantees that this key is 100% unique.

## attacks

### XSS

Cross-site scripting (XSS) is a type of computer security vulnerability typically found in Web applications. XSS enables attackers to inject client-side script into Web pages viewed by other users. 

### Man-in-the-middle attack

Man-in-the-middle attack (MitM) is an attack where the attacker secretly relays and possibly alters the communication between two parties who believe they are directly communicating with each other. 

### Session fixation

Session fixation attacks attempt to exploit the vulnerability of a system which allows one person to fixate (set) another person's session identifier (SID). 

Most session fixation attacks are web based, and most rely on session identifiers being accepted from URLs (query string) or POST data.

example

>Mallory visits http://vulnerable.example.com/ and checks which SID is returned. For example, the server may respond: Set-Cookie: SID=0D6441FEA4496C2.
>
>Mallory is now able to send Alice an e-mail: "Check out this new cool feature on our bank, http://vulnerable.example.com/?SID=0D6441FEA4496C2."
>
>Alice logs on, with fixated session identifier SID=0D6441FEA4496C2.
>
>Mallory visits http://vulnerable.example.com/?SID=0D6441FEA4496C2 and now has unlimited access to Alice's account.
