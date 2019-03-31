import java.net.InetSocketAddress

import com.twitter.finagle.Service
import com.twitter.finagle.builder.{Server, ServerBuilder}
import com.twitter.finagle.http.Http
import com.twitter.finagle.stats.OstrichStatsReceiver
import com.twitter.logging.Logger
import com.twitter.ostrich.admin.config.ServerConfig
import com.twitter.ostrich.admin.{RuntimeEnvironment, Service => OstrichService}
import com.twitter.util.Future
import org.jboss.netty.handler.codec.http._

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 11/6/13
 * Time: 12:13 PM
 * To change this template use File | Settings | File Templates.
 */

class BasicServerConfig extends ServerConfig[BasicServer] {
  var serverPort: Int = 8000

  def apply(runtime: RuntimeEnvironment): BasicServer = {
    new BasicServer(this);
  }
}

class BasicServer(config: BasicServerConfig) extends OstrichService {
  val log = Logger.get()
  var server: Server = _

  def start() {
    val service: Service[HttpRequest, HttpResponse] = new Service[HttpRequest, HttpResponse] {
      def apply(request: HttpRequest) = Future(new DefaultHttpResponse(HttpVersion.HTTP_1_1, HttpResponseStatus.OK))
    }
    server = ServerBuilder()
      .codec(Http())
      .bindTo(new InetSocketAddress(config.serverPort))
      .reportTo(new OstrichStatsReceiver())
      .name("HttpServer")
      .build(service)
    log.debug("start...");
  }

  def shutdown() {
    log.debug("stop...");
    server.close()
  }
}

object BasicServer {
  val log = Logger.get;

  def main(args: Array[String]) {
    val runtime = RuntimeEnvironment(this, args);
    val server = runtime.loadRuntimeConfig[BasicServer]()
    log.info("server start...")
    try {
      server.start()
    } catch {
      case ex: Exception => {
        ex.printStackTrace()
      }
    }
  }
}
