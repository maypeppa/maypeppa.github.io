import org.apache.log4j.Logger

/**
 * Created by dirlt on 9/4/15.
 */
object TestLog4j {
  def main(args: Array[String]): Unit = {
    val logger1 = Logger.getLogger("TestLog4j")
    logger1.info("a info message from test")
    logger1.warn("a warning message from test")

    val rootLogger = Logger.getRootLogger
    rootLogger.info("a info message from root logger")
    rootLogger.warn("a warning message from root logger")
  }
}
