import sbtprotobuf.{ProtobufPlugin=>PB}
import AssemblyKeys._

// seq(PB.protobufSettings: _*)

assemblySettings

// ====================

name := "finagle"

organization := "com.dirlt.scala"

version := "1.0-SNAPSHOT"

scalaVersion := "2.10.2"

val protobufVersion = "2.5.0"

// fix the issue : package daemon contains object and package with same name: supervisor
// TODO: why is work. -> http://comments.gmane.org/gmane.comp.java.clojure.storm/2426

scalacOptions += "-Yresolve-term-conflict:package"

libraryDependencies ++= {
  val finagleVersion = "6.6.2"
  val utilVersion = "6.6.0"
  Seq(
    "com.twitter" %% "finagle-core" % finagleVersion,
    "com.twitter" %% "finagle-ostrich4" % finagleVersion,
    "com.twitter" %% "finagle-mysql" % finagleVersion,
    "com.twitter" %% "finagle-http" % finagleVersion,
    "com.twitter" %% "util-core" % utilVersion,
    "com.twitter" %% "util-logging" % utilVersion,
    "com.google.protobuf" % "protobuf-java" % protobufVersion
  )
}

// ====================

// Test Suite

testFrameworks += new TestFramework("org.specs2.runner.SpecsFramework")

parallelExecution in Test := false

publishArtifact in Test := false

// // Protocol-Buffers

// sourceDirectory in PB.protobufConfig := new java.io.File("src/main/proto")

// version in PB.protobufConfig := protobufVersion

// // idea takes generated/com as source root, and I can't do nothing about it but manually change it in IDE:(
// javaSource in PB.protobufConfig <<= (sourceDirectory in Compile)(_ / "generated")
