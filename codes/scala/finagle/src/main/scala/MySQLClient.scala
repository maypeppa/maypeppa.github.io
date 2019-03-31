import com.twitter.finagle.exp.mysql.{Client, StringValue}
import com.twitter.finagle.stats.OstrichStatsReceiver
import com.twitter.logging.Level
import com.twitter.util.Await


/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 11/14/13
 * Time: 7:49 AM
 * To change this template use File | Settings | File Templates.
 */
object MySQLClient extends App {
  val client = Client(host = "localhost:3306",
  username = "root", password = "123", dbname = "sandbox", logLevel = Level.ALL,
  statsReceiver = new OstrichStatsReceiver());

  val result = client.prepare("select * from t1").flatMap(ps => {
    ps.parameters = Array.empty
    client.select(ps) {
      row =>
        val StringValue(name) = row("name").get
        val StringValue(pass) = row("pass").get
        (name,pass)
    }.ensure(client.closeStatement(ps))
  })
  result.onSuccess {
    res =>
      res.foreach{
        x => println(x._1,x._2)
      }
      Await.result(client.close())
  }
}
