run:
	echo "make app.zip"; zip -rq app.zip entry share
	rm -rf outputs
	spark-submit --master "spark://mac:7077" --conf "spark.pyspark.appMasterEnv.PYSPARK_PYTHON=pyvenv/bin/python" --archives "venv.zip#pyvenv" --py-files app.zip  entry/main.py file:///Users/dirlt/codes/py/test_pyspark/data.json file:///Users/dirlt/codes/py/test_pyspark/outputs

package:
	echo "make venv.zip"; cd venv; zip -rq ../venv.zip *; cd ..
