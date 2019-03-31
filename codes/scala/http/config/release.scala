// coding:utf-8
// Copyright (C) dirlt

import com.twitter.logging.config._
import org.apache.log4j.{Level => Log4jLevel}
import com.twitter.ostrich.admin.config.{TimeSeriesCollectorConfig, StatsConfig, AdminServiceConfig}

new HttpConfig {
  serverPort = 8000

  log4jLevel = Log4jLevel.INFO

  admin = new AdminServiceConfig {
    httpPort = 8888
    statsNodes = new StatsConfig {
      reporters = new TimeSeriesCollectorConfig
    }
  }

  loggers = new LoggerConfig {
    level = Level.INFO
    handlers = new FileHandlerConfig {
      filename = "./log/http-fg.log"
        roll = Policy.Daily
      } :: Nil
  }
}
