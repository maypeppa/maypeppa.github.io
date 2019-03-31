import org.slf4j.LoggerFactory

/**
 * Created by dirlt on 9/4/15.
 */
object TestSlf4j {
  def main(args: Array[String]): Unit = {
    val logger1 = LoggerFactory.getLogger("TestSlf4j")
    logger1.info("a info message from test")
    logger1.warn("a warning message from test")

    val rootLogger = LoggerFactory.getLogger("")
    rootLogger.info("a info message from root logger")
    rootLogger.warn("a warning message from root logger")
  }
}
