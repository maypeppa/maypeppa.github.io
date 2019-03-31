import AssemblyKeys._

assemblySettings

// ====================

name := "akka"

organization := "com.dirlt.scala"

version := "1.0-SNAPSHOT"

scalaVersion := "2.10.2"

val protobufVersion = "2.4.1"

// fix the issue : package daemon contains object and package with same name: supervisor
// TODO: why is work. -> http://comments.gmane.org/gmane.comp.java.clojure.storm/2426

scalacOptions += "-Yresolve-term-conflict:package"

scalacOptions in Test ++= Seq("-Yrangepos")

libraryDependencies ++= {
  val finagleVersion = "6.6.2"
  val utilVersion = "6.6.0"
  Seq(
    "com.twitter" %% "finagle-core" % finagleVersion,
    "com.twitter" %% "finagle-ostrich4" % finagleVersion,
//    "com.twitter" %% "finagle-mysql" % finagleVersion,
    "com.twitter" %% "finagle-http" % finagleVersion,
    "com.twitter" %% "util-core" % utilVersion,
    "com.twitter" %% "util-logging" % utilVersion,
//   "org.hbase" % "asynchbase" % "1.4.1",
    "com.google.protobuf" % "protobuf-java" % protobufVersion,
    "com.google.guava" % "guava" % "13.0.1",
    "com.google.code.findbugs" % "jsr305" % "1.3.9",
    "log4j" % "log4j" % "1.2.17",
    "com.typesafe.akka" %% "akka-actor" % "2.2.3",
    "org.specs2" %% "specs2" % "2.3.4" % "test"
    )
}

// ====================

// Test Suite

testFrameworks += new TestFramework("org.specs2.runner.SpecsFramework")

parallelExecution in Test := false

publishArtifact in Test := false
