import akka.actor.{Actor, ActorSystem, Props}
import org.apache.log4j.Logger

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 11/21/13
 * Time: 11:30 AM
 * To change this template use File | Settings | File Templates.
 */

object Hello extends App {
  val system = ActorSystem("system")
  val hello = system.actorOf(Props[Hello], "hello")
  hello ! "start"
}

class Hello extends Actor {
  val log = Logger.getLogger(getClass)
  val sub = context.actorOf(Props[Worker], "worker")

  override def preStart() {
    log.debug("hello start...")
  }

  override def postStop() {
    log.debug("hello stop...")
  }

  def receive = {
    case "start" => sub ! "masturbation"
    case s =>
      println("worker done with " + s)
      log.debug("shutdown system...")
      context.system.shutdown()
  }
}

class Worker extends Actor {
  def receive = {
    case s =>
      println("worker working with " + s)
      sender ! s
  }
}
