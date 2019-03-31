import java.net.InetSocketAddress

import com.twitter.finagle.Service
import com.twitter.finagle.builder.{Server, ServerBuilder}
import com.twitter.finagle.http.Http
import com.twitter.finagle.stats.OstrichStatsReceiver
import com.twitter.ostrich.admin.config.ServerConfig
import com.twitter.ostrich.admin.{RuntimeEnvironment, Service => OstrichService}
import com.twitter.util.Future
import org.apache.log4j.{Level, Logger}
import org.jboss.netty.buffer.ChannelBuffers
import org.jboss.netty.handler.codec.http._
import org.slf4j.LoggerFactory

class HttpConfig extends ServerConfig[HttpServer] {
  var serverPort = 8000
  var log4jLevel = Level.DEBUG

  def apply(runtime: RuntimeEnvironment): HttpServer = {
    Logger.getRootLogger.setLevel(log4jLevel)
    new HttpServer(this);
  }
}

class HttpServer(config:HttpConfig) extends OstrichService {
  var http: Server = _
  var https : Server = _
  val log = LoggerFactory.getLogger(getClass)

  // TODO(dirlt): your service.
  val service : Service[HttpRequest, HttpResponse] = new Service[HttpRequest, HttpResponse] {
    def apply(request: HttpRequest): Future[HttpResponse] = {
      val response = new DefaultHttpResponse(HttpVersion.HTTP_1_1, HttpResponseStatus.OK)
      response.setContent(ChannelBuffers.copiedBuffer("OK".getBytes))
      Future(response)
    }
  }

  def start() {
    log.debug("start service...")
    log.debug("http on port " + config.serverPort)
    http = ServerBuilder()
      .codec(Http())
      .bindTo(new InetSocketAddress(config.serverPort))
      .reportTo(new OstrichStatsReceiver())
      .name("http")
      .build(service)

    log.debug("https on port " + (config.serverPort + 1000))
    https = ServerBuilder()
      .codec(Http())
      .bindTo(new InetSocketAddress(config.serverPort + 1000))
      .reportTo(new OstrichStatsReceiver())
      .tls("/tmp/keys/server.crt", "/tmp/keys/server.key")
      .name("https")
      .build(service)
  }

  def shutdown() {
    log.debug("shutdown service...")
    http.close()
    https.close()
  }
}

object HttpServer {
  def main(args: Array[String]) {
    val runtime = RuntimeEnvironment(this, args);
    val server = runtime.loadRuntimeConfig[HttpServer]()
    server.start()
  }
}
